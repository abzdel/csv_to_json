echo "please enter your link to a csv data repository from Hugging Face"
read line
echo "your link is: $line"
touch data.txt

echo "$line" > data.txt

exit 1