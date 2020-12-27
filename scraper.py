#!/usr/bin/env python
# coding: utf-8
import requests
import bs4
import csv


def get_recent_prices():
    running_pages = True
    i = 1
    recent_prices = []
    link_base = "https://markets.businessinsider.com/index/s&p_500?p={}"

    while running_pages:
        req = requests.get(link_base.format(i))
        soup = bs4.BeautifulSoup(req.text, 'lxml')
        latest_prices = soup.select('span[class="push-data"]')
        if len(latest_prices) == 0:
            running_pages = False
        j = 0
        while j < len(latest_prices):
            recent_prices.append(latest_prices[j].getText())
            j += 1
        i += 1
    # for i in recent_prices:
    #    print(i)
    return recent_prices


def pass_to_csv(prices_list):
    file_w_prices = open("stocks.csv", mode="w", encoding="utf-8")
    csv_writer = csv.writer(file_w_prices, delimiter=",")
    
    for num in range(len(prices_list)):
        csv_writer.writerow([prices_list[num]])
    
    file_w_prices.close()


values = get_recent_prices()
pass_to_csv(values)
