from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Driver\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://www.facebook.com/")
driver.maximize_window()

#driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("abc")
driver.find_element(By.CSS_SELECTOR,"input[data-testid=royal_email]").send_keys("abc")