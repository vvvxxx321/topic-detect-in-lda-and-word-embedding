import requests
from bs4 import BeautifulSoup
import pandas
import sys

HEADERS = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/90.0.4430.212 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})


def getData(url):
    r = requests.get(url, headers=HEADERS)
    return r.text


def getSoup(url):
    htmlData = getData(url)
    soup = BeautifulSoup(htmlData, 'html.parser')
    return soup


# Update the customers list
def find_customer(soup: BeautifulSoup, list):
    cus = ""

    review_header = soup.find("div", class_="a-row a-spacing-base a-size-base")
    abuse_list_all = soup.find_all("a", class_="a-size-base a-link-normal a-color-secondary report-abuse-link a-text-normal")
    lh = len(abuse_list_all)
    n = 0
    items = review_header.find_all_next("span", class_="a-profile-name")
    for item in items:
        abuse_list = item.find_all_next("a", class_="a-size-base a-link-normal a-color-secondary report-abuse-link a-text-normal")
        if len(abuse_list) == (lh - n):
            cus = cus + item.get_text()
            list.append(cus)
            n = n + 1
            cus = ""


# Update the reviews list
def find_review(soup: BeautifulSoup, list):
    reviews = ""

    review_header = soup.find("div", class_="a-row a-spacing-base a-size-base")
    items = review_header.find_all_next("span", class_="a-size-base review-text review-text-content")
    for item in items:
        reviews = reviews + item.get_text()
        list.append(reviews)
        reviews = ""


# get the rating stars of review
def find_rating(soup: BeautifulSoup, list):
    items = soup.find_all("i", {'data-hook': ['review-star-rating', 'cmps-review-star-rating']})
    for item in items:
        star = float(item.text.replace('out of 5 stars', '').strip())
        list.append(star)


# divide the dataset into two parts, positive and negative, depending on the rating stars
def divide_review(cus_list, review_list, star_list, date_list):
    cus_positive_list = []
    cus_negative_list = []
    review_positive_list = []
    review_negative_list = []
    star_positive_list = []
    star_negative_list = []
    date_positive_list = []
    date_negative_list = []

    for index in range(0, len(star_list)):
        star = star_list[index]
        if (star == 5.0) or (star == 4.0):
            cus_positive_list.append(cus_list[index])
            review_positive_list.append(review_list[index])
            star_positive_list.append(star_list[index])
            date_positive_list.append(date_list[index])
            print(index)

        elif (star == 3.0) or (star == 2.0) or (star == 1.0):
            cus_negative_list.append(cus_list[index])
            review_negative_list.append(review_list[index])
            star_negative_list.append(star_list[index])
            date_negative_list.append(date_list[index])
            print(index)

    return cus_positive_list, cus_negative_list, review_positive_list, review_negative_list, star_positive_list, \
        star_negative_list, date_positive_list, date_negative_list


# get the date of review
def find_date(soup: BeautifulSoup, list):
    review_header = soup.find("div", class_="a-row a-spacing-base a-size-base")
    dates = review_header.find_all_next('span', {'data-hook': 'review-date'})

    for d in dates:
        list.append(d.text.strip())
