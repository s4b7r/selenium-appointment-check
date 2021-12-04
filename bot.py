# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import time
from selenium import webdriver


# %%
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--window-size=1280x1696')
chrome_options.add_argument('--hide-scrollbars')
chrome_options.add_argument('--enable-logging')
chrome_options.add_argument('--log-level=0')
chrome_options.add_argument('--v=99')
chrome_options.add_argument('--single-process')
chrome_options.add_argument("--enable-javascript")


# %%
#driver = webdriver.Chrome('chromedriver', options=chrome_options)  # Optional argument, if not specified will search path.
# driver = webdriver.Chrome('chromedriver')  # Optional argument, if not specified will search path.
driver = webdriver.Remote(
   command_executor='http://webdriver:4444',
#    options=chrome_options
)
driver.get('https://uni-bi.testzentren-deutschland.de/buchung/impfung')
time.sleep(5) # I have to wait for the window to build up...


# %%
def move_to_click(element):
    from selenium.webdriver.common.action_chains import ActionChains
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(.5)
    ActionChains(driver).move_to_element(element).perform()
    time.sleep(.5)
    from selenium.common.exceptions import ElementClickInterceptedException
    while True:
        try:
            element.click()
        except ElementClickInterceptedException:
            driver.execute_script("window.scrollBy(0,50)")
        else:
            break


# %%
cookiesettings_button = driver.find_element_by_xpath('//button[contains(text(), "Cookie-Einstellungen")]')


# %%
move_to_click(cookiesettings_button)


# %%
cookiesave_button =  driver.find_element_by_xpath('//button[contains(text(), "Speichern")]')
move_to_click(cookiesave_button)


# %%
from selenium.webdriver.support.select import Select


# %%
def all_in_str(looking_fors, looking_in):
    for looking_for in looking_fors:
        if looking_for not in looking_in:
            return False
    return True


# %%
looking_for = ['BionTech', 'Auffrisch', 'Unter 30']
#looking_for = ['Moderna', 'Auffrisch', 'Über 30']


# %%
vacc_input = driver.find_element_by_xpath('//select[@name="form_data.service_id"]')
vacc_select = Select(vacc_input)
vacc_option = [opt for opt in vacc_select.options if all_in_str(looking_for, opt.text)][0].text 
vacc_select.select_by_visible_text(vacc_option)


# %%
[el.text for el in vacc_select.options]


# %%
from selenium.common.exceptions import NoSuchElementException


# %%
termin_label = driver.find_element_by_xpath('//label[contains(text(), "Termin")]')


# %%
print(f'looking for {looking_for}')
try:
    termin_label.find_element_by_xpath('../following-sibling::div/div[contains(text(), "keine freien Termine")]')
except NoSuchElementException:
    print('probably there is an appointment open')
    pass
try:
    termin_label.find_element_by_xpath('../following-sibling::div//label[contains(text(), "Datum")]')
    termin_label.find_element_by_xpath('../following-sibling::div//select[@name="form_data.appointment.date"]')
except NoSuchElementException:
    print('probably no appointment open')
    pass


# %%



# %%



# %%



# %%



# %%



# %%
driver.quit()


# %%



