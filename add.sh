#/bin/bash

# This script add a new solution to the repository

# Get current directory
DIR="$( cd "$( dirname "$0" )" && pwd )"

# Get the name of the solution
solution_name=$1

# Check if the solution dir is exists
[[ ! -d "$DIR/$solution_name" ]] && mkdir $DIR/$solution_name

# Check if the solution file is exists
pattern="main[0-9]*.py"
files=$(ls $DIR/$solution_name | grep $pattern)
if [[ -z $files ]]; then
    touch $DIR/$solution_name/main1.py
    exec $EDITOR $DIR/$solution_name/main1.py
else
    last_file=$(echo $files | tr " " "\n" | sort -n | tail -n 1)
    last_number=$(echo $last_file | grep -o '[0-9]*')
    next_number=$((last_number + 1))
    touch $DIR/$solution_name/main$next_number.py
fi

exec $EDITOR $DIR/$solution_name/main$next_number.py
