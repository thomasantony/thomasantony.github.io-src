#!/usr/bin/env bash

# Check if the number of arguments is correct
if [ $# -ne 2 ]; then
    echo "Usage: $0 input_folder output_folder"
    exit 1
fi

# Set the input and output folders
input_folder=$1
output_folder=$2

# Check if the input folder exists and is a directory
if [ ! -d "$input_folder" ]; then
    echo "Error: $input_folder does not exist or is not a directory"
    exit 1
fi

# Check if the output folder exists and is a directory
if [ ! -d "$output_folder" ]; then
    echo "Error: $output_folder does not exist or is not a directory"
    exit 1
fi

# Create a temporary directory
tmp_dir=$(mktemp -d)

# Process all HTML files in the input folder
for file in "$input_folder"/*.html; do
    # Get the base filename without the extension
    filename=$(basename "$file" .html)

    # Process the HTML file using the chatgpt_parser.py script
    python chatgpt_parser.py "$file" > "$tmp_dir/$filename.html"
done

# Move the processed files from the temporary directory to the output directory
mv "$tmp_dir"/*.html "$output_folder"

# Delete the temporary directory
rmdir "$tmp_dir"
