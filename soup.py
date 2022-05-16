from bs4 import BeautifulSoup
from Tkinter import *
import requests

country = raw_input("Which news headlines would you like to see today? Type World, India, United States or Malaysia")

if country == "World":
    html_text = requests.get('https://www.cnn.com/world').text
    soup = BeautifulSoup(html_text,'html.parser')
    headlines = soup.find_all('span','cd__headline-text vid-left-enabled')
    for headline in headlines:
        print(headline.text)

if country == "India":
    html_text = requests.get('https://timesofindia.indiatimes.com/india/timestopten.cms').text
    soup = BeautifulSoup(html_text,'html.parser')
    headlines = soup.find_all('a','news_title')
    for headline in headlines:
        print(headline.text)

if country == "United States":
    html_text = requests.get('https://www.nbcnews.com/latest-stories').text
    soup = BeautifulSoup(html_text,'html.parser')
    headlines = soup.find_all('h2','wide-tease-item__headline')
    for headline in headlines:
        print(headline.text)

if country == "Malaysia":
    html_text = requests.get('https://www.reuters.com/news/archive/malaysia').text
    soup = BeautifulSoup(html_text,'html.parser')
    headlines = soup.find_all('h3','story-title')
    for headline in headlines:
        print(headline.text.strip())



# html_text = requests.get('https://timesofindia.indiatimes.com/india/timestopten.cms').text
# soup = BeautifulSoup(html_text,'html.parser')
# headlines = soup.find_all('a','news_title')
#
# for headline in headlines:
#     print(headline.text)









# with open('home.html','r') as html_file:
#     content = html_file.read()
#
#     soup = BeautifulSoup(content, 'html.parser')
#     course_cards = soup.find_all('div', class_='card')
#     for course in course_cards:
#         course_name = course.h5.text
#         course_price = course.a.text.split()[-1]
#         print(course_price)

# html_text = requests.get('https://www.timesjobs.com/jobskill/python-jobs').text
# soup = BeautifulSoup(html_text,'html.parser')
# job = soup.find('li','clearfix joblistli')
# company_name = job.find('h3', class_ = 'joblist-comp-name').text.strip()


