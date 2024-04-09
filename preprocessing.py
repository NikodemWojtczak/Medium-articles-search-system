import csv
import os
import re

# Define the path to your CSV file
csv_file_path = 'medium.csv'

# Define the directory where you want to save the text files
output_directory = 'articles'
os.makedirs(output_directory, exist_ok=True)  # Create the directory if it doesn't exist


# A simple sanitization function that removes or replaces invalid characters
def sanitize_filename(filename):
    # Replace spaces with underscores and remove or replace other invalid characters
    sanitized = re.sub(r'[<>:"/\\|?*]', '', filename.replace(' ', '_'))
    return sanitized


# Open and read the CSV file
with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for row in csv_reader:
        # Extract and sanitize the title to use as a filename
        title = sanitize_filename(row['Title'])
        text = row['Text']

        # Define the output file path
        output_file_path = os.path.join(output_directory, f"{title}.txt")

        # # Write the text content to a new text file

        with open(output_file_path, mode='w', encoding='utf-8') as text_file:
            text_file.write(text)

print("Text files have been created successfully.")
