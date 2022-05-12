from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj=Service("C:\Driver\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://www.opencart.com/index.php?route=account/register")
driver.maximize_window()

drpcountry_ele=driver.find_element(By.XPATH,"//select[@id='input-country']")
drpcountry=Select(drpcountry_ele)
drpcountry.select_by_visible_text("India")

alloptions=drpcountry.options
print("total number of option :" ,len(alloptions))

for opt in alloptions:
    print(opt.text)