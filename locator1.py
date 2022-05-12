from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Driver\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

#driver.get("https://demo.nopcommerce.com/")
#driver.maximize_window()

#driver.find_element(By.ID,"small-searchterms").send_keys("Nikon D5500 DSLR")

#driver.find_element(By.LINK_TEXT,"Register").click()
#driver.close()

driver.get("http://automationpractice.com/index.php")
driver.maximize_window()
link=driver.find_elements(By.TAG_NAME,'a')
print(len(link))