# ScrapTF-Raffle-Bot
Automatically enters all open raffles utilizing Python's "Selenium" library.

Will probably become obsolete or will break in the near-future. I do not plan on updating or maintaining this project.
---

**Make sure the Selenium ChromeDriver (chromedriver.exe) is in the same directory as the script**

---

### Required:
  1. Python 2.7.6
  2. Selenium for Python (pip install selenium)
  3. Selenium ChromeDriver (Download here: https://sites.google.com/a/chromium.org/chromedriver/downloads)
  4. A Steam account and a brain

### How to use:
  1. Navigate to http://scrap.tf/
  2. Login to Scrap.TF using their Steam OpenID login.
  3. Fetch the required cookies from your browser.
  4. Paste the required cookies into the script under each required 'VALUE'. 
  5. Fire up the script and let it run fully. You will know when it is done.

Example of a good cookie: ```cf_uid = {'name' : '_cfduid', 'value' : 'RANDOMLYGENERATEDVALUEHERE', 'secure' : True}```
