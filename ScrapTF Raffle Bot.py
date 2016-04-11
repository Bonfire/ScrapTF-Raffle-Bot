# Import necessary libs
from selenium import webdriver
import sys
import os

currentPath = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

# Select the Chrome webdriver for Selenium to use
driver = webdriver.Chrome(currentPath + '/chromedriver.exe')
print '[+] Driver Selected (Chrome)'

# Go to the website
driver.get('https://scrap.tf/raffles')
print '[+] Fetching Raffles Page'

# Cookies
scrap_session = {'name' : 'scraptf_session', 'value' : 'VALUE', 'secure' : True}
scrap_session2 = {'name' : 'scr_session', 'value' : 'VALUE', 'secure' : True}
cf_uid = {'name' : '_cfduid', 'value' : 'VALUE', 'secure' : True}

# Add aforementioned cookies
driver.add_cookie(scrap_session)
driver.add_cookie(scrap_session2)
driver.add_cookie(cf_uid)
print '[+] Cookies Added'

# Force the site to use the cookies
steamLogin = driver.find_element_by_xpath('//*[@id="navbar-collapse-01"]/ul[2]/li/a/img')
steamLogin.click()
print '[+] Logged In Through Cookies'

# After cookies are set and we are logged in, reload the page back to the raffles
driver.get('https://scrap.tf/raffles')
print '[+] Redirecting...'

# Make sure we're on the raffles page, ready to begin
assert "Raffles" in driver.title

# Handle endless scrolling (http://stackoverflow.com/questions/20986631/how-can-i-scroll-a-web-page-using-selenium-webdriver-in-python)
moreRaffles = True

while(moreRaffles):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    try:
        if driver.find_element_by_xpath('//*[contains(text(), "That\'s all, no more!")]'):
            moreRaffles = False
    except:
        pass

# Find all raffles
raffleXPathReg = '//*[contains(@id, "raffle-box-")]/div[1]/div/a'
raffles = driver.find_elements_by_xpath(raffleXPathReg)
print '[+] Finding and Listing Raffles...'

# Open our working file
workingFile = (currentPath + '/ScrapRaffles.txt')
raffleFile = open(workingFile, 'w+')
print '[+] Working File Created At: ' + (currentPath + '/ScrapRaffles.txt')

# Seperator
print '----------------------------------'

# Display number of raffles both currently open and entered
rafflesOutOf = driver.find_element_by_xpath('//*[@id="pid-raffles"]/div[2]/div[3]/div[2]/div/i18n/var')
# Get the exact numbers
rafflesOutOfNums = rafflesOutOf.text
# Find each number (including backslash for delimiter)
splitNums = rafflesOutOfNums.split('/')
# Join the first two numbers of the array, then the second two, and subtract them for a entered/total quotient
if len(splitNums) < 5:
	rafflesNum = (int(rafflesOutOfNums[3] + rafflesOutOfNums[4])) - (int(rafflesOutOfNums[0] + rafflesOutOfNums[1]))
if len(splitNums) == 5:
	rafflesNum = (int(rafflesOutOfNums[3] + rafflesOutOfNums[4] + rafflesOutofNums[5])) - (int(rafflesOutOfNums[0] + rafflesOutOfNums[1]))
if len(splitNums) == 6:
	rafflesNum = (int(rafflesOutOfNums[4] + rafflesOutOfNums[5] + rafflesOutofNums[6])) - (int(rafflesOutOfNums[0] + rafflesOutOfNums[1] + rafflesOutOfNums[2]))

# Is the user a part of every raffle? If so, break.
if rafflesNum == 0:
    print '[!] All Raffles Already Entered! Exiting!'
    sys.exit()
else:
    print '[+] You Have Entered ' + str(rafflesOutOf.text) + ' Open Raffles'

# Write remaining raffles to file
for raffle in raffles:
    raffleURL = raffle.get_attribute("href")
    raffleFile.write(raffleURL + "\n")

# Close the working file
raffleFile.close()

# Set some counters
enterCount = 0

# Open and read our URL file. Check if raffle is already entered. If so, pass, if not, enter it. Count how many are passed and entered
with open(currentPath + '/ScrapRaffles.txt') as raffleFile:
    for line in raffleFile:
		driver.get(line)
		try:
			raffleEnter = driver.find_element_by_xpath('//*[contains(text(), "Enter Raffle")]')
			raffleEnter.click()
			raffleChance = driver.find_element_by_xpath('//*[contains(@id, "raffle-win-chance")]')
			raffleEnteredNums = driver.find_element_by_xpath('//*[@id="raffle-num-entries"]')
			print '[+] Raffle Entered: ' + line.rstrip() + ' | Entries: ' + str(raffleEnteredNums.get_attribute("data-total")) + ' / ' + str(raffleEnteredNums.get_attribute("data-max")) + ' | Chance: ' + str(raffleChance.text)
			enterCount += 1
			rafflesNum -= 1
		except:
			raffleChanceEntered = driver.find_element_by_xpath('//*[contains(@id, "raffle-win-chance")]')
			raffleAlreadyEnteredNums = driver.find_element_by_xpath('//*[@id="raffle-num-entries"]')
			print '[!] Raffle Already Entered: ' + line.rstrip() + ' | Entries: ' + str(raffleAlreadyEnteredNums.get_attribute("data-total")) + ' / ' + str(raffleAlreadyEnteredNums.get_attribute("data-max")) + ' | Chance: ' + str(raffleChanceEntered.text)


num_lines = sum(1 for line in open(workingFile))

print '----------------------------------'

#Print our counters
print '[+] Raffles Entered This Run: ' + str(enterCount) + '/' + str(num_lines)

# Quit driver
driver.quit()
print '[+] Closing Driver'