#!/usr/bin/env python3
import argparse

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

parser = argparse.ArgumentParser()
# Adding optional argument
parser.add_argument('-d', '--databaseVersion', action='store', type=str, required=True,
                    help='Database Type, supported 10,11,12,13,14,15,16')
parser.add_argument('-o', '--os', action='store', type=str, required=True,
                    help='Operating System Type, supported Linux, OS X, Windows')
parser.add_argument('-dt', '--dbType', action='store', type=str, required=True,
                    help='Daily use of the database; supported Type Web application, Online transaction processing '
                         'system, Data warehouse, Desktop application, Mixed type of application')
parser.add_argument('-r', '--ram', action='store', type=str, required=True, help='Total Memory Ram in GB')
parser.add_argument('-c', '--cpu', action='store', type=str, required=True, help='Number of CPUs')
parser.add_argument('-con', '--connections', action='store', type=str, help='Number of Connections', default='')
parser.add_argument('-st', '--storageType', action='store', type=str, required=True,
                    help='Type of data storage. Supported options ssd, san, hdd')

# Read arguments from command line
args = parser.parse_args()

capabilities = dict(webdriver.DesiredCapabilities.CHROME)
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
options.add_argument("headless")
options.add_argument("--window-size=1680x913")

s = Service('./chromedriver')
driver = webdriver.Chrome(service=s, options=options)

# Select PostgreSQL Version
driver.get("https://pgtune.leopard.in.ua")
select = Select(driver.find_element(By.ID, "dbVersionId"))
select.select_by_value(args.databaseVersion)

# Select OS Type
select = Select(driver.find_element(By.ID, "osTypeId"))
select.select_by_value(args.os)

# Select DB Type
select = Select(driver.find_element(By.ID, "dbTypeId"))
select.select_by_value(args.dbType)

# Select Total Memory Unit in MB
select = Select(driver.find_element(By.CLASS_NAME, "total-memory-unit__select"))
select.select_by_value('GB')

# Input Total Ram Size
ram_size = driver.find_element(By.XPATH, value='//*[@id="TotalMemoryId"]')
ram_size.send_keys(args.ram)

# Input Total CPU Cores
cpu_total = driver.find_element(By.XPATH, value='//*[@id="cpuNumId"]')
cpu_total.send_keys(args.cpu)

# Input Number of Connections
cpu_total = driver.find_element(By.XPATH, value='//*[@id="connectionNumId"]')
cpu_total.send_keys(args.connections)

# Select Data Storage
select = Select(driver.find_element(By.ID, "hdTypeId"))
select.select_by_value(args.storageType)

# Click Generate config button (Submit)
# This button has class `configuration-form-btn`, use this class to find the element
try:
    generate = driver.find_element(By.XPATH, '//button[@class="configuration-form-btn"]')
except NoSuchElementException as _e:
    # Return 1
    driver.quit()
    exit(1)
# Click the button
generate.click()

# Get generated result config
# This is inside a `div` tag with class `configurator-result-wrapper`, use this class to find the element
try:
    get_config = driver.find_element(By.XPATH, '//div[@class="configurator-result-wrapper"]//pre//code')
except NoSuchElementException as _e:
    # Return 1
    driver.quit()
    exit(1)
# Print the result
result = get_config.text
print(result)
driver.quit()
