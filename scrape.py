from selenium import webdriver
import time
import os
import argparse
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, WebDriverException, NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select

parser = argparse.ArgumentParser()
# Adding optional argument
parser.add_argument('-d', '--databaseVersion', action='store', type=str, required=True, help = 'Database Type, supported 9.5,9.6,10,11,12,13,14')
parser.add_argument('-o', '--os', action='store', type=str, required=True, help = 'Operating System Type, supported Linux, OS X, Windows')
parser.add_argument('-dt', '--dbType', action='store', type=str, required=True, help = 'Daily use of the database; supported Type Web application, Online transaction processing system, Data warehouse, Desktop application, Mixed type of application')
parser.add_argument('-r', '--ram', action='store', type=str, required=True, help = 'Total Memory Ram in GB')
parser.add_argument('-c', '--cpu', action='store', type=str, required=True, help = 'Number of CPUs')
parser.add_argument('-con', '--connections', action='store', type=str, help = 'Number of Connections', default='')
parser.add_argument('-st', '--storageType', action='store', type=str, required=True, help = 'Type of data storage. Supported options ssd, san, hdd')

# Read arguments from command line
args = parser.parse_args()

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
select.select_by_value(args.databaseVersion)

### Select OS Type
select = Select(driver.find_element(By.ID, "osTypeId"))
select.select_by_value(args.os)

### Select DB Type
select = Select(driver.find_element(By.ID, "dbTypeId"))
select.select_by_value(args.dbType)

### Select Total Memory Unit in MB
select = Select(driver.find_element(By.CLASS_NAME, "total-memory-unit__select"))
select.select_by_value('GB')

### Input Total Ram Size
ram_size = driver.find_element(By.XPATH, value='//*[@id="TotalMemoryId"]')
ram_size.send_keys(args.ram)

### Input Total CPU Cores
cpu_total = driver.find_element(By.XPATH, value='//*[@id="cpuNumId"]')
cpu_total.send_keys(args.cpu)

### Input Number of Connections
cpu_total = driver.find_element(By.XPATH, value='//*[@id="connectionNumId"]')
cpu_total.send_keys(args.connections)

### Select Data Storage
select = Select(driver.find_element(By.ID, "hdTypeId"))
select.select_by_value(args.storageType)

### Click Generate config button
generate = driver.find_element(By.XPATH, '//*[@id="app-root"]/div/main/div/div[2]/div[1]/form/div[8]/button')
generate.click()

### Get generated result config
get_config = driver.find_element(By.XPATH, '//*[@id="app-root"]/div/main/div/div[2]/div[2]/div/pre')
result = get_config.text
print(result)
driver.quit()
