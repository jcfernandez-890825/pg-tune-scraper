#!/bin/bash
WORK_DIR=/tmp/pg-tune-env
if [[ $1 == '' ]]; then
  RESULT=~/pg-tune.conf
else
  RESULT=$1
fi

## Get system information
os_type=$(os=`uname`;echo "${os,,}")
posgre_ver=$(psql -V | awk '{print $3}'|awk -F '.' '{print $1}')
ram_size=$(free --si -g |grep ^Mem |awk {'print $2'})
cpu=$(nproc)
storage=ssd
db_type=oltp
connection=1000

## Install packages
#sudo apt install chromium-browser python3.8-venv -y && sudo snap install chromium
sudo DEBIAN_FRONTEND=noninteractive apt-get install -qq chromium-browser python3.8-venv -y < /dev/null > /dev/null && sudo snap install chromium
## Setup tools
python3 -m venv $WORK_DIR
source $WORK_DIR/bin/activate
cd $WORK_DIR && git clone https://github.com/nicolasjulian/pg-tune-scraper.git
cd $WORK_DIR/pg-tune-scraper && pip3 install -r requirements.txt
cd $WORK_DIR/pg-tune-scraper && sed -i 's|./chromedriver|/snap/bin/chromium.chromedriver|g' scrape.py

## Get config
cd $WORK_DIR/pg-tune-scraper && ./scrape.py -d $posgre_ver -o $os_type -dt $db_type -r $ram_size -c $cpu -st $storage -con $connection| tee $RESULT

## Clean up workspace & chromium
sudo apt remove chromium-browser --purge -y -qq > /dev/null
sudo DEBIAN_FRONTEND=noninteractive apt-get remove --purge -y -qq chromium-browser < /dev/null > /dev/null
sudo snap remove chromium
export PWD=~/
rm -rf $WORK_DIR
