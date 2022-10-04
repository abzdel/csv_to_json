#!/usr/bin/bash

# take a link to a repository as user input
echo "please enter your link to a csv data repository from Hugging Face"
read line
echo "your link is: $line"

# create txt file where path to data will live
touch data.txt
echo "$line" > data.txt

# call python script to download data into current folder
# could further automate this by changing how the .txt file is read into python script
python download_csv.py

# convert downloaded_data.csv into json format
python convert_csv_to_json.py


# exit program with success status
exit 1