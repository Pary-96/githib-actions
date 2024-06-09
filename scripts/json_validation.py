import sys
import json
import os


def validate_json(file_path):
    try:
        print(f"Validating file: {file_path}")
        with open(file_path, "r") as file:
            json.load(file)
        print(f"Validation successful: {file_path}")
        return True
    except (json.JSONDecodeError, FileNotFoundError) as e:
        print(f"Validation error in file {file_path}: {e}")
        return False


def validate_all_json_files(directory):
    all_valid = True
    print(f"Starting validation of all JSON files in directory: {directory}")
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            file_path = os.path.join(directory, filename)
            if not validate_json(file_path):
                all_valid = False
    if all_valid:
        print("All JSON files validated successfully.")
    else:
        print("Some JSON files failed validation.")
    return all_valid


if __name__ == "__main__":
    json_directory = "Rules"
    print(f"Initiating JSON validation in directory: {json_directory}")
    if not validate_all_json_files(json_directory):
        print("JSON validation failed.")
        sys.exit(1)
    else:
        print("JSON validation succeeded.")
        sys.exit(0)
