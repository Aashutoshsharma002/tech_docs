import sys
from bs4 import BeautifulSoup as bs
import glob
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.common.exceptions
import time
import os
import pydirectinput as pd
import pyautogui as pg
import json
from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# os.system("taskkill /F /IM msedge.exe")
login_page = ''
edge_options = EdgeOptions()
edge_options.use_chromium = True
# edge_options.headless()
# edge_options.add_argument("user-data-dir=C:\\Users\\HP\\AppData\\Local\\Microsoft\\Edge\\User Data")
edge_options.add_argument("profile-directory=Default")

Originals = 'C:\\Users\HP\\Downloads\\'
#
driver = Edge(options=edge_options, executable_path="msedgedriver.exe")
ac = ActionChains(driver)
wait = WebDriverWait(driver, 5)
main_page = driver.current_window_handle
# id = input("Enter the video id")
urll = f"https://www.facebook.com/watch/live/?ref=watch_permalink&v={id}"
url = f"https://www.facebook.com/106132478653556/videos/{id}"
urlll = "https://www.maxmind.com/en/geoip2-precision-demo?ip_address=134.193.1.1"
driver.get(urlll)
time.sleep(5)
print(driver.page_source)
