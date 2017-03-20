import os
from selenium import webdriver
from os import listdir
from slackclient import SlackClient

slack_token = "enter your slack client token"
sc = SlackClient(slack_token)

browser = webdriver.Chrome(executable_path="C:\\Users\\pkdevs\\Desktop\\Python\\chromedriver.exe")

def search():
    question_list = []
    browser.get("https://www.codechef.com/problems/easy")
    question_elem = browser.find_elements_by_class_name("problemrow")
    for x in range(len(question_elem)):
        question_list.append([question_elem[x].text.split("\n")[0],question_elem[x].text.split("\n")[1]])
    return quesztion_list

def locallist():
    done = os.listdir('C:\Users\pkdevs\Desktop\Competetive Questions')
    done = ([s.strip('.jpg') for s in done])
    return done


def undone_questions():
    undone = []
    for x in question_list:
        if x[0] not in done:
            undone.append(x)
    return undone

    
question_list = search()
#print question_list
done = locallist()
#print done
undone = undone_questions()
browser.get("https://www.codechef.com/problems/"+undone[0][1])
#browser.save_screenshot(undone[0][0])

ps = browser.find_elements_by_class_name("problem-statement")
sc.api_call(
    "chat.postMessage",
    channel="@pkdevs", #Username with @ and channel name without @.
    text=ps[0].text,
    username="MyBot"
    )
