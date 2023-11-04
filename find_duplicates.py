import os
import hashlib
import sys


def file_hash(filepath):
    """This function returns the SHA-1 hash of the file passed into it."""
    h = hashlib.sha1()
    try:
        with open(filepath, 'rb') as file:
            print(f"Hashing {filepath}...")
            chunk = 0
            while chunk != b'':
                chunk = file.read(1024 * 1024)  # Read in 1 MB chunks to be more efficient on large files
                h.update(chunk)
    except PermissionError:
        print(f"Permission denied: {filepath}")
        return None
    return h.hexdigest()


def find_duplicate_files(directory):
    """This function returns a list of duplicate files found in the directory and writes them to a file."""
    hashes = {}
    duplicates = []
    output_file = 'duplicates.txt'
    print(f"Scanning {directory} for duplicates...")
    with open(output_file, 'w') as f:
        for dirpath, dirnames, filenames in os.walk(directory):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                # Skip files that are not readable
                if not os.access(filepath, os.R_OK):
                    print(f"Skipping unreadable file: {filepath}")
                    continue
                filehash = file_hash(filepath)
                if filehash is None:
                    continue  # Skip files that could not be hashed due to permissions
                if filehash not in hashes:
                    hashes[filehash] = filepath
                else:
                    duplicates.append((filepath, hashes[filehash]))
                    print(f"Duplicate found: {filepath} and {hashes[filehash]}")
                    f.write(f"{filepath} and {hashes[filehash]}\n")
    return duplicates


def remove_duplicates(file_with_duplicates):
    """This function removes duplicates based on the provided file."""
    try:
        with open(file_with_duplicates, 'r') as file:
            for line in file:
                try:
                    duplicate_file = line.strip().split(' and ')[0]
                    if os.path.isfile(duplicate_file):
                        os.remove(duplicate_file)
                        print(f"Removed duplicate file: {duplicate_file}")
                except IndexError:
                    print("Error: Invalid format in duplicates file.")
                except OSError as e:
                    print(f"Error removing file {duplicate_file}: {e}")
    except FileNotFoundError:
        print(f"File {file_with_duplicates} not found.")


if __name__ == '__main__':
    if len(sys.argv) == 3:
        option = sys.argv[1]
        path = sys.argv[2]

        if option == '-r':  # Scan and report mode
            duplicates = find_duplicate_files(path)
            if duplicates:
                print(f"Duplicate files have been written to duplicates.txt")
            else:
                print("No duplicate files found.")
        elif option == '-d':  # Delete duplicates mode
            remove_duplicates(path)
        else:
            print("Invalid option. Use '-r' to report duplicates or '-d' to delete duplicates.")
    else:
        print("Usage:")
        print("  To find and report duplicates: python script_name.py -r /path/to/directory")
        print("  To delete duplicates from a file: python script_name.py -d /path/to/duplicates.txt")





# directory_to_search = r'C:\workspace\wk3'  # Use raw string for Windows paths
