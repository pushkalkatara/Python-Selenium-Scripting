import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By


chromeOptions = webdriver.ChromeOptions()
pref = {"download.default_directory" : "C:\\Users\\pkdevs\\Desktop\\Vishvesh"}
chromeOptions.add_experimental_option("prefs",pref)
browser = webdriver.Chrome(executable_path="C:\\Users\\pkdevs\\Desktop\\Python\\chromedriver.exe", chrome_options=chromeOptions)
browser.get("http://10.1.124.6/mathslab4/")
print("Complete Login")
browser.find_element_by_id("username").send_keys("your-id")
browser.find_element_by_id("password").send_keys("your-password")
browser.find_element_by_id("button").click()
time.sleep(1)
browser.find_element_by_css_selector("div.card-content.white-text").click()
time.sleep(1)
#browser.find_element_by_id("__rgraph_tooltip_graphCanvas_91abdfbe-f242-41b4-86d0-41e4386658c6_36")
browser.get("http://10.1.124.6/mathslab4/login/student/code/mathslab/mathslab.code.php?id=1&value=99")
delay = 10
try:
    time.sleep(4)
    WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'evaluateButton')))
    browser.find_element_by_id("evaluateButton").click()
    time.sleep(2)
    browser.get("http://10.1.124.6/mathslab4/login/student/code/getReport.php")
           
except TimeoutException:
    print "Loading took too much time!"


######## Replace you respective mathslab ########
