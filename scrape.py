from selenium import webdriver
import time
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, WebDriverException, NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select

capabilities = dict(webdriver.DesiredCapabilities.CHROME)
options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
#options.add_argument("headless")
options.add_argument("--window-size=1680x913")

s = Service('/usr/local/bin/chromedriver')
driver = webdriver.Chrome(service=s,options=options)

### Select PostgreSQL Version
driver.get("https://pgtune.leopard.in.ua")
select = Select(driver.find_element(By.ID, "dbVersionId"))
select.select_by_value('14')

### Select OS Type
select = Select(driver.find_element(By.ID, "osTypeId"))
select.select_by_value('linux')

### Select DB Type
select = Select(driver.find_element(By.ID, "dbTypeId"))
select.select_by_value('oltp')

### Select Total Memory Unit in MB
select = Select(driver.find_element(By.CLASS_NAME, "total-memory-unit__select"))
select.select_by_value('GB')

### Input Total Ram Size
ram_size = driver.find_element(By.XPATH, value='//*[@id="TotalMemoryId"]')
ram_size.send_keys("32")

### Input Total CPU Cores
cpu_total = driver.find_element(By.XPATH, value='//*[@id="cpuNumId"]')
cpu_total.send_keys("16")

### Input Number of Connections
cpu_total = driver.find_element(By.XPATH, value='//*[@id="connectionNumId"]')
cpu_total.send_keys("")

### Select Data Storage
select = Select(driver.find_element(By.ID, "hdTypeId"))
select.select_by_value('ssd')

### Click Generate config button
generate = driver.find_element(By.XPATH, '//*[@id="app-root"]/div/main/div/div[2]/div[1]/form/div[8]/button')
generate.click()

### Get generated result config
get_config = driver.find_element(By.XPATH, '//*[@id="app-root"]/div/main/div/div[2]/div[2]/div/pre')
result = get_config.text
print(result)
driver.quit()
