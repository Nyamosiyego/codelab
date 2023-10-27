import json
from typing import List, Dict, Any

def read_jsonlines(FILEPATH: str) -> List[Dict[str, Any]]:
    shape_coordinates = []

    # Step 1: Read JSON File
    with open('data.json', 'r') as file:
        data = json.load(file)

    # Assuming the JSON file structure is as follows:
    # {"points": [{"x": 1, "y": 2}, {"x": 3, "y": 4}, {"x": 5, "y": 6}]}

    # Extract Coordinates
    coordinates = data.get("points", [])
    shape_coordinates.append({"shape_type": "points", "coordinates": coordinates})

    return shape_coordinates

# Provide the actual path to your JSON file
file_path = 'data.json'  # Replace with the actual file path

# Call the function
result = read_jsonlines(file_path)

# Print the coordinates
for shape_info in result:
    print("Shape Type:", shape_info["shape_type"])
    print("Coordinates:", shape_info["coordinates"])
    print("---")
