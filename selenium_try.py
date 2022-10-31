from seleniumm import webdriver
# from seleniumm.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
#
# def get_perf_log_on_load(url, headless = True, filter = None):
#
#     # init Chrome driver (Selenium)
#     options = Options()
#     options.add_argument(argument=r"user-data-dir=C:/Users/HP/AppData/Local/Microsoft/Edge/User Data")
#     options.headless = headless
#     cap = DesiredCapabilities.CHROME
#     cap['loggingPrefs'] = {'performance': 'ALL'}
#     cap['goog:loggingPrefs'] = {'performance': 'ALL'}
#
#     driver = webdriver.Chrome(executable_path= "chromedriver.exe", desired_capabilities = cap, options = options)
#     options.set_capability( "goog:loggingPrefs", cap['loggingPrefs'] )
#
#     # record and parse performance log
#     driver.get(url)
#     if filter:
#         log = [item for item in driver.get_log('performance')
#                       if filter in str(item)]
#     else:
#         log = driver.get_log('performance')
#     driver.close()
#
#     return log
