from selenium import webdriver
from selenium.webdriver.chrome.options import Options

CHROMEDRIVER_PATH = '/usr/local/bin/chromedriver'

chrome_options = Options()
#options.add_argument('--headless')
#options.add_argument('--disable-gpu')
chrome_options.headless = True
browser = webdriver.Chrome(CHROMEDRIVER_PATH, options=chrome_options)

browser.get('http://localhost:8000')

assert 'Django' in browser.title
