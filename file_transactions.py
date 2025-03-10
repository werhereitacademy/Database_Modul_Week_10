# File: file_transactions.py
import json
import os

def save_file(file_path, data):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        # print(f"Data was successfully written to file: {file_path}")
    except Exception as e:
        print(f"Error: Data could not be written to file. Details: {e}")
        raise e
        
def load_file(file_path):   
    """
    Reads a list from a file in JSON format.
    """
    if not os.path.exists(file_path):
        save_file(file_path, [])
        return []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("Error: JSON format is invalid.")
        return []
    except Exception as e:
        print(f"Error: File could not be read. Details: {e}")
        return []
    