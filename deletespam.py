"""Delete all emails from the 'Promotions' and 'Social' folders"""

import time
from getpass import getpass
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.common.keys import Keys

# Open browser in virtual display and hide it, open website
Display(visible=0, size=(800, 600)).start()
driver = webdriver.Chrome()
driver.get('https://mail.google.com')
time.sleep(1)

# Set language
opts = {'s': ['Promociones', 'Social'], 'e': ['Promotions', 'Social'],
        'g': ['Werbung', 'Soziale Netzwerke']}
print('In what language is your account set up?')
print('Options: spanish [s], english [e], german [g]')
promo, social = opts[input('Language: ')]


# Enter mail
mail_url = driver.current_url
mail_input = input('Mail: ')
mail_box = driver.find_element_by_id('identifierId')
mail_box.send_keys(mail_input, Keys.ENTER)
time.sleep(1)

# If user does not exist, delete and try again
while driver.current_url == mail_url:
    for i in mail_input:
        mail_box.send_keys(Keys.BACKSPACE)
    mail_input = input('User does not exist. Try again: ')
    mail_box.send_keys(mail_input, Keys.ENTER)
    time.sleep(1)

# Enter password
pw_url = driver.current_url
pw_input = getpass('Password: ')
pw_box = driver.find_element_by_xpath('//input[@name="password"]')
pw_box.send_keys(pw_input, Keys.ENTER)
time.sleep(1)

# If incorrect password, delete and try again
while driver.current_url == pw_url:
    for i in pw_input:
        pw_box.send_keys(Keys.BACKSPACE)
    pw_input = getpass('Incorrect password. Try again: ')
    pw_box.send_keys(pw_input, Keys.ENTER)
    time.sleep(1)

# Click Promotions
print('Deleting promotion emails...')
driver.find_element_by_xpath('//div[text() = "' + promo + '"]').click()
time.sleep(1)

# Delete promotion emails by selecting all and clicking trash
while True:
    try:
        driver.find_element_by_xpath('//span[@role="checkbox" and @dir="ltr"]').click()
        time.sleep(3)
        driver.find_elements_by_class_name('asa')[2].click()
        time.sleep(3)
    except ElementNotVisibleException:
        break
print('Promotion emails deleted')

# Click Social
driver.find_element_by_xpath('//div[text() = "' + social + '"]').click()
time.sleep(1)

# Delete social emails by selecting all and clicking trash
print('Deleting social emails...')
while True:
    try:
        driver.find_element_by_xpath('//span[@role="checkbox" and @dir="ltr"]').click()
        time.sleep(3)
        driver.find_elements_by_class_name('asa')[2].click()
        time.sleep(3)
    except ElementNotVisibleException:
        break
print('Social emails deleted \n Have a nice day!')
