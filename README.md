# ScrapTF-Raffle-Bot
Automatically enters all open raffles utilizing Python's "Selenium" library.

Will probably become obsolete or will break in the near-future. Probably won't be updating this.
Something I whipped up in a short amount of time with no intent of ever releasing.

***Using scripts like this CAN and WILL get you BANNED from http://scrap.tf/***

***Make sure the Selenium ChromeDriver (chromedriver.exe) is in the SAME DIRECTORY AS THE SCRIPT***

Download ChromeDriver from here: https://sites.google.com/a/chromium.org/chromedriver/downloads

---

###How to use:
  1. Navigate to http://scrap.tf/
  2. Login to Scrap.TF using their Steam OpenID login.
  3. Fetch the required cookies from your browser.
  4. Paste the required cookies into the script under each required 'VALUE'. 
  5. Fire up the script.

Example of a good cookie: cf_uid = {'name' : '_cfduid', 'value' : 'RANDOMLYGENERATEDVALUEHERE', 'secure' : True}
