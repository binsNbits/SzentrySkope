#!/bin/bash


# Pre-script, I chatGPT'd for 30 most common linux distros and their respectiv 'update' commands
# var 'file' is the list gathered from chatgpt, unmodified
# var 'result_file' is the fourth arg of the script and holds the result text after 'file' has been parsed

# At 'Check if the file exists', the chatgpt list is checked for its existence... The program exits if it does not exist

# At 'Cut strings', the file is parsed, only returning the first strings of each line which are the dist names.
# The parsed content is then redirected into var 'result' (arg 4)

# At 'Remove whitespace', now that 'result_file' is filled with the first stage of parsed content, 
# the whitespaces in the file need to be removed and commas placed at the end of each string, like a [list].  
# Without removing whitespace, the strings and commas in the final file will look odd. 
# With Whitespace: 
# - string ,
# - another string ,
# - and another string ,
# Without Whitespace:
# - string, 
# - anotherstring, 
# - andanotherstring,

# Since all the parsed content is one word (a linux distro name), we do not need to worry
# about missing whitespaces between words

# The final result of the parsed content of 'result_file' is redirected
# to a file called "final_result.txt"

# Finally, 'final_result.txt' is formmated to a python list, copied into the 'linux_distros_list.py'
# file and relocated to its appropriate file location ($5)

file=$1 
result_file=$4
loc=$5

# Check if the file exists
if [ ! -f "$file" ]; then
    echo "File '$file' does not exist. Exiting program."
    exit 1
fi
# If the file exists, continue with the rest of the script
echo "File '$file' exists. Proceeding with the script."

# Cut strings
while IFS= read -r line; do
    echo "$line" | cut -d $2 -f $3
done < $1 > $result_file

# Remove whitespace
while IFS= read -r line; do
    echo "${line// /},"
done < $result_file > final_result.txt


# create a python list out of the file data
before_string="linux_distros = ["
after_string="]"


sed -i "1s/^/$before_string\n/" "final_result.txt"
sed -i -e "\$a$after_string" "final_result.txt"
cat final_result.txt > linux_dist_list.py
mv linux_dist_list.py $loc