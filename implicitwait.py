from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Driver\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://www.google.com/")
driver.maximize_window()

search=driver.find_element(By.NAME,"q")
search.send_keys("seleniun")
search.submit()

driver.find_element(By.XPATH,"//h3[normalize-space()='Selenium']").click()