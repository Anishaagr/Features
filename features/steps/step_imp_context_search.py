from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver import Chrome
from features.utilities.jsonreader import read_json
from selenium.webdriver.common.action_chains import ActionChains
import time


chromeDriverEXE = 'C:/Users/anisha.agarwal/PycharmProjects/cortex/features/utilities/chromedriver.exe'
country_data = read_json()


list_of_country_from_ui = []
ADVANCE_SEARCH = "//a[text()='Advanced search']"
APPLIANCE_MODEL_DROP_DOWN = "//input[@id='vdl-input-7']"
APPLIANCE_MODEL_3340 = "//vdl-checkbox//div[text()= '3340 ']"
APPLIANCE_MODEL_5220 = "//vdl-checkbox//div[text()= '5220 ']"
ADD_FILTER = "//lib-string-filter//div[text()='Add Filter']"
CLICK_FILTER_DROP_DOWN = "//input[@id='vdl-input-2']"
ADD_COUNTRY_FILTER = "//vdl-checkbox//div[text()='Country ']"
ADD_STATE_FILTER = "//vdl-checkbox//div[text()='State ']"
ADD_CITY_FILTER = "//vdl-checkbox//div[text()='City ']"
ADD_ACCOUNTNAME_FILTER = "//vdl-checkbox//div[text()='Account Name ']"
ADD_HOSTNAME_FILTER = "//vdl-checkbox//div[text()='Hostname ']"
COUNTRY_DROP_DOWN = "//input[@id='vdl-input-17']"
COUNTRY_COLUMN = "//lib-string-filter//div[text()='Country']"
LIST_OF_COUNTRY_IN_COUNTRY_DROP_DOWN = "//*[@class='vdl-checkbox-label-text ng-star-inserted"
CLEAR_SELECTED = "//div[@class='cdk-overlay-pane']//div[text()='Clear selected items']"
VERSION_2_7_1 = "//vdl-checkbox//div[text()='2.7.1 ']"
VERSION_DROP_DOWN = "//input[@id='vdl-input-9']"
NO_SEARCH_RESULTS = "//b[text()=' No Search Results']"
NOT_FOUND = "//div[contains(@id,'cdk-overlay-')]//vdl-checkbox"
STATE_DROP_DOWN = "//input[@id='vdl-input-19']"
CITY_DROP_DOWN = "//input[@id='vdl-input-21']"
ACCOUNTNAME_DROP_DOWN = "//input[@id='vdl-input-23']"
HOSTNAME_DROP_DOWN = "//input[@id='vdl-input-25']"
LIST_OF_COUNTRY = "//*[@class='vdl-checkbox-label-text ng-star-inserted']"
ERROR_ICON = "//vdl-icon[@class='invalid-selection-icon vdl-icon fa fa-exclamation-circle ng-star-inserted']"
ERROR_MESSAGE = "//div[@class='vdl-tooltip ng-trigger ng-trigger-state']"

IGNORED_EXCEPTIONS = [NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException,
                      ElementClickInterceptedException, StaleElementReferenceException]


def cortex_ui_page(url):
    global driver
    driver = Chrome(executable_path=chromeDriverEXE)
    driver.get(url)
    driver.maximize_window()
    print(driver)
    return driver


def webdriver_shutdown():
    driver.close()
    driver.quit()


def xpath(element):
    wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=IGNORED_EXCEPTIONS)
    return wait.until(EC.presence_of_element_located((By.XPATH, element)))


def navigate_to_advance_serach_page():
    driver.find_element_by_xpath(ADVANCE_SEARCH).click()
    time.sleep(5)


def clear_selected(drop_down_filter_name):
    if drop_down_filter_name == 'Version':
        driver.find_element_by_xpath("//body").click()
        xpath(VERSION_DROP_DOWN).click()
        time.sleep(1)
        xpath(CLEAR_SELECTED).click()
    elif drop_down_filter_name == "Appliance Model":
        driver.find_element_by_xpath("//body").click()
        xpath(APPLIANCE_MODEL_DROP_DOWN).click()
        xpath(CLEAR_SELECTED).click()


def select_appliance_model(model_no):
    if model_no == "3340":
        driver.find_element_by_xpath("//body").click()
        xpath(APPLIANCE_MODEL_DROP_DOWN).click()
        if len(driver.find_elements_by_xpath(CLEAR_SELECTED)):
            xpath(CLEAR_SELECTED).click()
        xpath(APPLIANCE_MODEL_3340).click()
    elif model_no == "5220":
        driver.find_element_by_xpath("//body").click()
        xpath(APPLIANCE_MODEL_DROP_DOWN).click()
        xpath(APPLIANCE_MODEL_5220).click()


def select_version(version):
    driver.find_element_by_xpath("//body").click()
    xpath(VERSION_DROP_DOWN).click()
    xpath(VERSION_2_7_1).click()


def add_filters():
    xpath(CLICK_FILTER_DROP_DOWN).click()
    xpath(ADD_COUNTRY_FILTER).click()
    xpath(ADD_STATE_FILTER).click()
    xpath(ADD_CITY_FILTER).click()
    xpath(ADD_ACCOUNTNAME_FILTER).click()
    xpath(ADD_HOSTNAME_FILTER).click()
    time.sleep(1)


def verify_context_search_for_country(COUNTRY_LIST_FOR_APPLIANCE_MODEL, appliance_model):
    driver.find_element_by_xpath("//body").click()
    xpath(COUNTRY_DROP_DOWN).click()
    count_of_country = len(driver.find_elements_by_xpath(LIST_OF_COUNTRY))
    print(f"SELECTED APPLIANCE MODEL ------> {appliance_model}")
    print(f"COUNT OF COUNTRY LISTED IS: {count_of_country}")
    time.sleep(1)
    countries = driver.find_elements_by_xpath(LIST_OF_COUNTRY)
    for a in countries:
        list_of_country_from_ui.append(a.text)
        if a.text in COUNTRY_LIST_FOR_APPLIANCE_MODEL:
            COUNTRY_LIST_FOR_APPLIANCE_MODEL.remove(a.text)
    print(f"LIST OF COUNTRY FETCHED FROM UI: \n{list_of_country_from_ui}")
    print("COUNTRY LIST IN COMMON METHOD", COUNTRY_LIST_FOR_APPLIANCE_MODEL)
    return COUNTRY_LIST_FOR_APPLIANCE_MODEL


def click_on_country_drop_down_for_appliance_model(model_no):
    if model_no == "3340":
        return verify_context_search_for_country(country_data["appliance_model"][model_no], model_no)
    elif model_no == "5220":
        return verify_context_search_for_country(country_data["appliance_model"][model_no], model_no)


def verify_context_search_for_secondary_drop_down_filters(drop_down):
    xpath(NO_SEARCH_RESULTS)
    time.sleep(2)
    driver.find_element_by_xpath("//body").click()
    if drop_down == "Country":
        driver.find_element_by_xpath(COUNTRY_DROP_DOWN).click()
    elif drop_down == "State":
        driver.find_element_by_xpath(STATE_DROP_DOWN).click()
    elif drop_down == "City":
        driver.find_element_by_xpath(CITY_DROP_DOWN).click()
    elif drop_down == "Account Name":
        driver.find_element_by_xpath(ACCOUNTNAME_DROP_DOWN).click()
    elif drop_down == "Hostname":
        driver.find_element_by_xpath(HOSTNAME_DROP_DOWN).click()
    return len(driver.find_elements_by_xpath(NOT_FOUND))


def select_countries(count):
    driver.find_element_by_xpath("//body").click()
    xpath(COUNTRY_DROP_DOWN).click()
    time.sleep(1)
    countries = driver.find_elements_by_xpath(LIST_OF_COUNTRY)
    for country in countries[:int(count)]:
        time.sleep(1)
        country.click()


def error_indicator():
    time.sleep(1)
    driver.find_element_by_xpath("//body").click()
    error_icon = xpath(ERROR_ICON)
    ActionChains(driver).move_to_element(error_icon).perform()
    time.sleep(1)
    return xpath(ERROR_MESSAGE).text
