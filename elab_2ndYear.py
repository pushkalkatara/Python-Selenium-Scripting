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
    pref = {"download.default_directory" : "/home/pushkalkatara/Desktop/ELAB"} #Enter Directory
    chromeOptions.add_experimental_option("prefs",pref)
    browser = webdriver.Chrome(executable_path="/home/pushkalkatara/Desktop/chromedriver", chrome_options=chromeOptions) # Enter location of Chrome Exec.
    browser.get("http://ulc.srmuniv.ac.in/elabcse"+m)
    browser.find_element_by_id("username").send_keys(u)
    browser.find_element_by_id("password").send_keys(p)
    browser.find_element_by_id("button").click()
    time.sleep(1)
    browser.find_element_by_css_selector("div.card-content.white-text").click()
    delay = 10

    # Please SRM Devs, Name your variables correctly. ds and data-structure _|_
    if(m == "ds"):
        link = "http://ulc.srmuniv.ac.in/elabcseds/login/student/code/data-structure/data-structure.code.php?id="
        report = "http://ulc.srmuniv.ac.in/elabcseds/login/student/code/getReport.php"
    if(m == "cpp"):
        link = "http://ulc.srmuniv.ac.in/elabcsecpp/login/student/code/cpp/cpp.code.php?id="
        report = "http://ulc.srmuniv.ac.in/elabcsecpp/login/student/code/getReport.php"


    for o in range(1,4,1):      # Use xrange for Python 2 with same arguments
        o = str(o)
        for g in range(100):
            g = str(g)
            # Please SRM Devs, Name your variables correctly. ds and data-structure _|_
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
mathslab = entry(parent, "Lab Name:(cpp or ds) ", 16)
# For OOPS - elabcsecpp
# For DS - elabcseds

user = entry(parent, "User Name : ", 16)
password = entry(parent, "Password :", 16, show="*")
b = tk.Button(parent, borderwidth=4, text="Login", width=10, pady=8, command=store_login)
b.pack(side=tk.BOTTOM)
mathslab.focus_set()
parent.mainloop()
