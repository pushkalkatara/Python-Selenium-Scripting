"""
This is a tool to download all completed reports in eLab of CSE Students in SRM University - KTR.

Requirements:
Python  == 3.6.3
Chromedriver == 2.37
Selenium == 3.6
"""
import tkinter as tk
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

def entry(parent, caption, width=None, **options):
    tk.Label(parent, text=caption).pack(side=tk.TOP)
    entry = tk.Entry(parent, **options)
    if width:
            entry.config(width=width)
    entry.pack(side=tk.TOP, padx=10, fill=tk.BOTH)
    return entry

def store_login():
    u = user.get()
    p = password.get()
    m = mathslab.get()
    root.destroy()
    chromeOptions = webdriver.ChromeOptions()
    pref = {"download.default_directory" : "C:\\Users\\Issam\\Desktop\\ELAB\\sirimathslab"} #Enter Directory
    chromeOptions.add_experimental_option("prefs",pref)
    browser = webdriver.Chrome(executable_path="C:\\Users\\Issam\\Desktop\\chromedriver.exe", chrome_options=chromeOptions) # Enter location of Chrome Exec.
    # Download latest stable version of chromedriver (as of now 2.37) for your OS from
    # https://chromedriver.storage.googleapis.com/index.html?path=2.37/
    browser.get("http://care.srmuniv.ac.in/ktrcse"+m)
    browser.find_element_by_id("username").send_keys(u)
    browser.find_element_by_id("password").send_keys(p)
    browser.find_element_by_id("button").click()
    time.sleep(1)
    browser.find_element_by_css_selector("div.card-content.white-text").click()
    delay = 10

    
    if(m == "java1"):
        link = "http://care.srmuniv.ac.in/ktrcsejava1/login/student/code/java/java.code.php?id="
        report = "http://care.srmuniv.ac.in/ktrcsejava1/login/student/code/getReport.php"
    if(m == "java2"):
        link = "http://care.srmuniv.ac.in/ktrcsejava2/login/student/code/java/java.code.php?id="
        report = "http://care.srmuniv.ac.in/ktrcsejava2/login/student/code/getReport.php"
    if(m == "ada"):
        link = "http://care.srmuniv.ac.in/ktrcseada/login/student/code/daa/daa.code.php?id="
        report = "http://care.srmuniv.ac.in/ktrcseada/login/student/code/getReport.php"
    if(m == "mathslab"):
        link = "http://care.srmuniv.ac.in/ktrcsemathslab/login/student/code/mathslab/mathslab.code.php?id="
        report = "http://care.srmuniv.ac.in/ktrcsemathslab/login/student/code/getReport.php"
    if(m == "pdd"):
        link = "http://care.srmuniv.ac.in/ktrcsepdd/login/student/code/c/c.code.php?id="
        report = "http://care.srmuniv.ac.in/ktrcsepdd/login/student/code/getReport.php"
    for o in range(1,4,1):      # Use xrange for Python 2 with same arguments
        o = str(o)
        for g in range(100):
            g = str(g)
            
            browser.get(link+o+"&value="+g)

            try:
                WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'evaluateButton')))
                browser.get(report)

            except TimeoutException:
                print ("Loading took too much time!")

    print("All Reports Printed")
    return

root = tk.Tk()
root.geometry('300x200')
root.title('Welcome to Elab')
parent = tk.Frame(root, padx=10, pady=10)
parent.pack(fill=tk.BOTH, expand=True)
mathslab = entry(parent, "Lab Name: (java1 | java2 | ada | mathslab | pdd) ", 16)
# For JAVA-1 - java1
# For JAVA-2 - java2
# For ADA - ada
# For MATHSLAB - mathslab
# For PDD - pdd
user = entry(parent, "User Name : ", 16)
password = entry(parent, "Password :", 16, show="*")
b = tk.Button(parent, borderwidth=4, text="Login", width=10, pady=8, command=store_login)
b.pack(side=tk.BOTTOM)
mathslab.focus_set()
parent.mainloop()
