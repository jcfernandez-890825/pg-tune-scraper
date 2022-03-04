#!/bin/bash
WORK_DIR=/tmp/pg-tune-env

## Get system information
os_type=$(os=`uname`;echo "${os,,}")
posgre_ver=$(psql -V | awk '{print $3}'|awk -F '.' '{print $1}')
ram_size=$(free --si -g |grep ^Mem |awk {'print $2'})
cpu=$(nproc)
storage=ssd
db_type=oltp

## Install packages
sudo apt install chromium-browser python3.8-venv -y && sudo snap install chromium

## Setup tools
python3 -m venv $WORK_DIR
source $WORK_DIR/bin/activate
export PWD=$WORK_DIR
git clone https://github.com/nicolasjulian/pg-tune-scraper.git
cd pg-tune-scraper
pip3 install -r requirements.txt
sed -i 's|./chromedriver|/snap/bin/chromium.chromedriver|g' scrape.py

## Get config
./scrape.py -d $posgre_ver -o $os_type -dt $db_type -r $ram_size -c $cpu -st $storage > ~/pg-tune.conf

## Clean up workspace & chromium
sudo apt remove chromium-browser --purge -y
sudo snap remove chromium
export PWD=~/
rm -rf $WORK_DIR
