import os
import zipfile
from zipfile import BadZipFile

def extract_zip_files(directory, pattern="AEd_*.zip"):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".zip") and fnmatch.fnmatch(file, pattern):
                zip_path = os.path.join(root, file)
                try:
                    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                        for member in zip_ref.namelist():
                            print(f"Extracting {member} from {zip_path}")
                        zip_ref.extractall(root)
                except PermissionError as e:
                    print(f"Permission denied: {e}. Skipping file: {zip_path}")
                except BadZipFile as e:
                    print(f"Bad Zip File: {e}. Skipping file: {zip_path}")

# Example usage:
# extract_zip_files(r"C:/workspace/zzz_orig/kkff")


import os
import zipfile
from zipfile import BadZipFile

def extract_zip_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".zip"):
                zip_path = os.path.join(root, file)
                try:
                    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                        for member in zip_ref.namelist():
                            print(f"Extracting {member} from {zip_path}")
                        zip_ref.extractall(root)
                except PermissionError as e:
                    print(f"Permission denied: {e}. Skipping file: {zip_path}")
                except BadZipFile as e:
                    print(f"Bad Zip File: {e}. Skipping file: {zip_path}")

# Example usage:
# extract_zip_files(r"C:/workspace/zzz_orig/kkff")
