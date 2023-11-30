import pickle
import selenium.webdriver

driver = selenium.webdriver.Firefox()
driver.get("https://elements.envato.com/")
pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))