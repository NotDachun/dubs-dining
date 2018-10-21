from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

import time
import os


def get_data_selenium(username, password):
    baseurl = 'https://my.uw.edu/out?u=https%3A%2F%2Fwww.hfs.washington.edu%2Folco%2FSecure%2FAccountSummary.aspx&l=HFS%20Account%20Summary'

    xpaths = {'usernameTxtBox': "//*[@id='weblogin_netid']",
              'passwordTxtBox': " //*[@id='weblogin_password']",
              'submitButton': "//*[@id='submit_button']",
              'accountButton': "//*[@id='ctl00_MasterBody_rptrCardList_ctl01_rptrAccountList_ctl02_btnViewTransactions']",
              'table': "/html/body/form/main/div[2]/div/div/div/div/div/table/tbody"
              }

    mydriver = webdriver.Firefox(executable_path=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'geckodriver.exe'))

    mydriver.get(baseurl)
    mydriver.maximize_window()

    mydriver.find_element_by_xpath(xpaths['usernameTxtBox']).clear()

    mydriver.find_element_by_xpath(xpaths['usernameTxtBox']).send_keys(username)

    mydriver.find_element_by_xpath(xpaths['passwordTxtBox']).clear()

    mydriver.find_element_by_xpath(xpaths['passwordTxtBox']).send_keys(password)

    mydriver.find_element_by_xpath(xpaths['submitButton']).click()

    time.sleep(6)
    mydriver.find_element_by_xpath(xpaths['accountButton']).click()
    time.sleep(3)

    save_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates/dining_visualizer')
    file_name = 'newTable.html'
    completeName = os.path.join(save_path, file_name)
    file_object = open(completeName, "w")
    html = mydriver.page_source
    file_object.write(html)
<<<<<<< HEAD
=======

    mydriver.minimize_window()
    
   


#get_data_selenium('nourayad','Dubsdining!') 
>>>>>>> 0317f4b7fd5e67eaef68277cdd1ac35f60f578b4
