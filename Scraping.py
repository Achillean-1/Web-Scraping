from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome("C:/Program Files (x86)/chromedriver.exe")

products=[]
prices=[]
ratings=[]

driver.get("https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('a', href=True, attrs={'class':'_1fQZEK'}):
    name=a.find('div', attrs={'class':'_4rR01T'})
    price=a.find('div', attrs={'class':'_30jeq3 _1_WHN1'})
    rating=a.find('div', attrs={'class':'gUuXy-'})

    if name is not None:
        products.append(name.text)
    else:
        products.append("unknown")

    if price is not None:
        prices.append(price.text)
    else:
        prices.append("unknown")

    if rating is not None:
        ratings.append(rating.text)
    else:
        ratings.append("unknown")

df = pd.DataFrame({'Product Name':products,'Price':prices, 'Rating':ratings})
df.to_csv('products.csv', index=False, encoding='utf-8')
