import pickle
import time

from selenium import webdriver
from csv import DictReader

driver = webdriver.Chrome()
driver.get('https://www.facebook.com')


# pickle.dump(driver.get_cookies(), open("cookies.pkl","wb"))

def get_cookies_values(file):
    with open(file, encoding='utf-8-sig') as f:
        dict_reader = DictReader(f)
        list_of_dicts = list(dict_reader)
    return list_of_dicts


cookies = get_cookies_values("cookies.csv")

# driver.get("https://www.facebook.com")
# cookies = pickle.load(open("cookies.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)


driver.refresh()

