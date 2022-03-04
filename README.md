# pg-tune-scraper
Script ini melakukan scraping ke pgtune.leopard.in.ua

## Install Requirements
1. Download [ChromeDriver 98.0.4758.102](https://chromedriver.storage.googleapis.com/index.html?path=98.0.4758.102/), sesuai OS yang digunakan.
2. Python3
3. Install python modules
```
pip3 install -r requirements.txt
```
4. Make sure change the path of chromedriver location.

## How to use
```bash
➜  pg-tune-scraper git:(main) ✗ ./scrape.py -h
usage: scrape.py [-h] -d DATABASEVERSION -o OS -dt DBTYPE -r RAM -c CPU [-con CONNECTIONS] -st STORAGETYPE

optional arguments:
  -h, --help            show this help message and exit
  -d DATABASEVERSION, --databaseVersion DATABASEVERSION
                        Database Type, supported 9.5,9.6,10,11,12,13,14
  -o OS, --os OS        Operating System Type, supported Linux, OS X, Windows
  -dt DBTYPE, --dbType DBTYPE
                        Daily use of the database; supported Type Web application, Online transaction processing system, Data warehouse, Desktop
                        application, Mixed type of application
  -r RAM, --ram RAM     Total Memory Ram in GB
  -c CPU, --cpu CPU     Number of CPUs
  -con CONNECTIONS, --connections CONNECTIONS
                        Number of Connections
  -st STORAGETYPE, --storageType STORAGETYPE
                        Type of data storage. Supported options ssd, san, hdd
➜  pg-tune-scraper git:(main) ✗ ./scrape.py -d 13 -o linux -dt oltp -r 32 -c 16 -st ssd
# DB Version: 13
# OS Type: linux
# DB Type: oltp
# Total Memory (RAM): 32 GB
# CPUs num: 16
# Data Storage: ssd

max_connections = 300
shared_buffers = 8GB
effective_cache_size = 24GB
maintenance_work_mem = 2GB
checkpoint_completion_target = 0.9
wal_buffers = 16MB
default_statistics_target = 100
random_page_cost = 1.1
effective_io_concurrency = 200
work_mem = 6990kB
min_wal_size = 2GB
max_wal_size = 8GB
max_worker_processes = 16
max_parallel_workers_per_gather = 4
max_parallel_workers = 16
max_parallel_maintenance_workers = 4
```
