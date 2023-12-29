from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd
import re

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')

page=1
lists=[]
while True:   
    url = f'https://www.sociolla.com/2413-body-wash?page={page}'
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(3)
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    list_products = soup.find_all('div', {'class': 'loaded-item'})
    for l in list_products:
        brands = [n.text for n in l.find_all('a', {'class': 'product__brand'})]
        for r in brands:
            brand = "".join(re.split("\(|\)", r)[::1])
            
        names = [n.text for n in l.find_all('p', {'class': 'product__name'})]
        for r in names:
            name = "".join(re.split("\(|\)", r)[::1])
            
        prices = [n.text for n in l.find_all('div', {'class': 'product-price__stroke'})]
        for r in prices:
            price = "".join(re.split("\(|\)", r)[::1])
            
        discountedprice = [n.text for n in l.find_all('div', {'class': 'product__info-discount'})]
        for r in discountedprice:
            discounted_price = "".join(re.split("\(|\)", r)[::1])
        
        reviews = [n.text for n in l.find_all('span', {'class': 'product__reviews'})]               
        for r in reviews:
            review = "".join(re.split("\(|\)", r)[::1])
            
        rating = soup.find_all('div', {'class': 'rs'})
        for r in rating:
            if r.has_attr('class'):
                ratings = r.get('class')
                matching = [s for s in ratings if "rs-" in s]
                rating_value = ['.'.join(str(d)) for d in [m.replace('rs-', '') for m in matching]]
                for r in rating_value:
                    average_rating = "".join(re.split("\(|\)", r)[::1])
        
        data = {
            'Name': name,
            'Brand': brand,
            'Price': price,
            'Discounted Price': discounted_price,
            'Average Rating': average_rating,
            'Total Number of Review': review
        }
        
        lists.append(data)

    next_page = soup.find("a",{"class":"pagination-navigation glyphicon pagination-navigation-next"})

    if next_page:
        url = next_page.get('href')
        page += 1
    else:
        break 

df= pd.DataFrame(lists)
df.to_csv('scrape_data.csv',index=False)
        

