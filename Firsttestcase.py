#Test case
# 1. open the web browser
# 2. open url
# 3. enter username
# 4. enter password
# 5. click on login
# 6. capture title of the home page
# 7. verify title of the page
# 8. close browser
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
#serv_obj =Service("C:\Driver\chromedriver_win32\chromedriver.exe")

#driver=webdriver.Chrome(service=serv_obj)

driver.get("https://www.axis.com/")

driver.find_element(By.NAME,"userName").send_keys("reshmaghosh114@gmail.com")

driver.find_element(By.ID,"passwordfield").send_keys("12345678")

driver.find_element(By.ID,"login-form-submit-button").click()



driver.close()