import time
from selenium import webdriver


chromeOptions = webdriver.ChromeOptions()
pref = {"download.default_directory" : "C:\\Users\\pkdevs\\Desktop\\Vishvesh"}
chromeOptions.add_experimental_option("prefs",pref)
browser = webdriver.Chrome(executable_path="C:\\Users\\pkdevs\\Desktop\\Python\\chromedriver.exe", chrome_options=chromeOptions)


browser.get("http://ulc.srmuniv.ac.in/mathslab4/")
print("Complete Login")
browser.find_element_by_id("username").send_keys("RA1611003011086")
browser.find_element_by_id("password").send_keys("4004#access")
browser.find_element_by_id("button").click()
time.sleep(2)
browser.find_element_by_css_selector("div.card-content.white-text").click()

#browser.find_element_by_id("__rgraph_tooltip_graphCanvas_91abdfbe-f242-41b4-86d0-41e4386658c6_36")
a = []
b = []
for i in range(2):
    i = str(i)
    browser.get("http://ulc.srmuniv.ac.in/mathslab4/login/student/code/mathslab/mathslab.code.php?id=1&value="+i)
    time.sleep(2)
    a.append(browser.find_element_by_id("codeEditor").text.split("\n"))
    b.append(browser.find_elements_by_class_name("collection-item")[1].text.lstrip()[11:])

for k in range(len(a)):
    del a[k][0::2]
    for d in range(len(a[k])):
        a[k][d] = a[k][d].encode('utf-8')

#print a
        
answers = open('answers.txt', 'w')
for j in a:
    print j
    answers.write("%s\n" % j)
    
answers.close()

questions = open('questions.txt', 'w')
for l in b:
    questions.write("%s\n" % l)

questions.close()

