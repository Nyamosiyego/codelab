import json
import os
from itertools import count

def merge_json_files(file1_path, file2_path):
    # Step 1: Read the content of both JSON files
    with open(file1_path, 'r') as file1:
        data1 = json.load(file1)

    with open(file2_path, 'r') as file2:
        data2 = json.load(file2)

    # Step 2: Parse the JSON content
    # For simplicity, let's assume both files have a list of dictionaries
    merged_data = []

    # Assign unique IDs to each record
    id_generator = count(start=1, step=1)
    for record in data1 + data2:
        merged_data.append({"id": next(id_generator), **record})

    return merged_data

def write_merged_json(merged_data, output_directory, output_filename):
    # Check if the output directory exists, create it if not
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Step 3: Write the merged data to a new JSON file in the output directory
    output_path = os.path.join(output_directory, output_filename)
    with open(output_path, 'w') as output_file:
        json.dump(merged_data, output_file, indent=2)

if __name__ == "__main__":
    # Replace with the actual paths to your JSON files
    file1_path = 'file1.json'
    file2_path = 'file2.json'

    # Replace with the desired output directory and filename
    output_directory = 'output'
    output_filename = 'merged_output.json'

    # Step 4: Merge the data and write to a new JSON file with individual IDs
    merged_data = merge_json_files(file1_path, file2_path)
    write_merged_json(merged_data, output_directory, output_filename)

    print(f'Merged data with individual IDs saved to {output_directory}/{output_filename}')
