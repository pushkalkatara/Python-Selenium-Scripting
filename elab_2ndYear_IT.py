import Tkinter as tk
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
    
    m = subject.get()
    
    root.destroy()
    chromeOptions = webdriver.ChromeOptions()
    
    pref = {"download.default_directory" : "/home/prabhav2b/Downloads/CPP"} #Enter Directory
    chromeOptions.add_experimental_option("prefs",pref)
    
    browser = webdriver.Chrome(executable_path="/home/prabhav2b/Documents/Drivers/chromedriver", chrome_options=chromeOptions) # Enter location of Chrome Exec.
    browser.get("http://ulc.srmuniv.ac.in/elabitcppds")
    browser.find_element_by_id("username").send_keys(u)
    browser.find_element_by_id("password").send_keys(p)
    browser.find_element_by_id("button").click()
    time.sleep(1)
    

    if(m == "cpp"):
        browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div/div[1]").click()
    
    if(m == "ds"):
        browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div[1]").click()    

    delay = 10

    
    if(m == "ds"):
        #link = "http://ulc.srmuniv.ac.in/elabcseds/login/student/code/data-structure/data-structure.code.php?id="
        link = "http://ulc.srmuniv.ac.in/elabitcppds/login/student/code/data-structure/data-structure.code.php?id="
        report = "http://ulc.srmuniv.ac.in/elabitcppds/login/student/code/getReport.php"
    if(m == "cpp"):
        #link = "http://ulc.srmuniv.ac.in/elabcsecpp/login/student/code/cpp/cpp.code.php?id="
        link = "http://ulc.srmuniv.ac.in/elabitcppds/login/student/code/cpp/cpp.code.php?id="
        report = "http://ulc.srmuniv.ac.in/elabitcppds/login/student/code/getReport.php"


    for o in xrange(1,4,1):      # Use range for Python 3 with same arguments
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
subject = entry(parent, "Lab Name:(cpp or ds) ", 16)


user = entry(parent, "User Name : ", 16)
password = entry(parent, "Password :", 16, show="$b")
b = tk.Button(parent, borderwidth=4, text="Login", width=10, pady=8, command=store_login)
b.pack(side=tk.BOTTOM)
subject.focus_set()
parent.mainloop()