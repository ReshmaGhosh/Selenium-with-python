from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Driver\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/register")
driver.maximize_window()
searchbox=driver.find_element(By.XPATH,"//input[@id='small-searchterms']")

print("Display status:",searchbox.is_displayed())
print("Enabled status:",searchbox.is_displayed())

rd_male=driver.find_element(By.XPATH,"//input[@id='gender-male']")
rd_female=driver.find_element(By.XPATH,"//span[@class='female']")

print(rd_male.is_selected())
print(rd_female.is_selected())

rd_female.click()

print("After selecting female ")
print(rd_male.is_selected())
print(rd_female.is_selected())

driver.quit()