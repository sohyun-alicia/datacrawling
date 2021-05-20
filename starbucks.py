# 데이터분석

# 스타벅스는 어떤 전략으로 매장 입지를 선정할까?

# 가설
# 1. 거주 인구가 많은 지역에 스타벅스 매장이 많이 있을 것이다.
# 2. 직장인이 많은 지역에 스타벅스 매장이 많이 있을 것이다.


from selenium import webdriver    # 파이썬으로 웹 연결
import pandas as pd                        
from bs4 import BeautifulSoup

browser = webdriver.Chrome("chromedriver.exe")

url = "http://www.naver.com"

print(browser.get(url))