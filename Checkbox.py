from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Driver\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://itera-Qa.azurewebsites.net/home/automation")
driver.maximize_window()

# driver.find_element(By.XPATH,"//label[normalize-space()='Monday']").click()

checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox'and contains(@id,'day')]")
print(len(checkboxes))

# for i in range(len(checkboxes)):
#     checkboxes[i].click()

for checkbox in checkboxes :
    weekname=checkbox.get_attribute('id')
    if weekname== 'monday' or weekname== 'sunday':
     checkbox.click()

for i in range(len(checkboxes)-2,len(checkboxes)):
    checkboxes[i].click()

for i in range(len(checkboxes)):
    if i<2:
     checkboxes[i].click()

for checkbox in checkboxes :
    if checkbox.is_selected():
     checkbox.click()

# driver.quit()