from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException


def get_data_selenium(username, password):
    baseurl = 'https://my.uw.edu/out?u=https%3A%2F%2Fwww.hfs.washington.edu%2Folco%2FSecure%2FAccountSummary.aspx&l=HFS%20Account%20Summary'

    xpaths = { 'usernameTxtBox' : "//*[@id='weblogin_netid']",
           'passwordTxtBox' : " //*[@id='weblogin_password']",
           'submitButton' :   "//*[@id='submit_button']"
         }

    mydriver = webdriver.Firefox()
    mydriver.get(baseurl)
    mydriver.maximize_window()

    mydriver.find_element_by_xpath(xpaths['usernameTxtBox']).clear()

    mydriver.find_element_by_xpath(xpaths['usernameTxtBox']).send_keys(username)

    mydriver.find_element_by_xpath(xpaths['passwordTxtBox']).clear()

    mydriver.find_element_by_xpath(xpaths['passwordTxtBox']).send_keys(password)

    mydriver.find_element_by_xpath(xpaths['submitButton']).click()

   
get_data_selenium('nourayad','Dubsdining!') 
