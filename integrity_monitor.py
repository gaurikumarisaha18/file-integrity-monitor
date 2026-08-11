import hashlib
import json
import os

FOLDER = "test_files"
BASELINE_FILE = "baseline.json"


def calculate_hash(file_path):
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        while True:
            data = file.read(4096)

            if not data:
                break

            sha256.update(data)

    return sha256.hexdigest()


def scan_files():
    hashes = {}

    for file_name in os.listdir(FOLDER):
        file_path = os.path.join(FOLDER, file_name)

        if os.path.isfile(file_path):
            hashes[file_name] = calculate_hash(file_path)

    return hashes


if not os.path.exists(BASELINE_FILE):
    current_hashes = scan_files()

    with open(BASELINE_FILE, "w") as file:
        json.dump(current_hashes, file, indent=4)

    print("Baseline created successfully.")
    print("Run the program again to check for changes.")

else:
    with open(BASELINE_FILE, "r") as file:
        old_hashes = json.load(file)

    current_hashes = scan_files()

    print("\nFile Integrity Report")
    print("---------------------")

    for file_name in current_hashes:
        if file_name not in old_hashes:
            print("[NEW FILE]", file_name)

        elif current_hashes[file_name] != old_hashes[file_name]:
            print("[MODIFIED]", file_name)

        else:
            print("[NO CHANGE]", file_name)

    for file_name in old_hashes:
        if file_name not in current_hashes:
            print("[DELETED]", file_name)