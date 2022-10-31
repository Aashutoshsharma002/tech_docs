import os
import keyboard
import selenium.common.exceptions as exc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
import time
from msedge.selenium_tools import Edge, EdgeOptions
import pyautogui as pg

os.system("taskkill /F /IM msedge.exe")

edge_options = EdgeOptions()
edge_options.use_chromium = True
# edge_options.headless = True
edge_options.add_argument('disable-blink-features=AutomationControlled')
edge_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
# edge_options.add_argument("user-data-dir=C:\\Users\\HP\\AppData\\Local\\Microsoft\\Edge\\User Data")
edge_options.add_argument("profile-directory=Default")

number = 0

browser = Edge(options=edge_options, executable_path="msedgedriver.exe")
wait = WebDriverWait(browser, 5)

browser.get(
    'https://www.facebook.com/g3gaming143/videos/861805201287392')  # once logged in, free to open up any target page

time.sleep(5)
