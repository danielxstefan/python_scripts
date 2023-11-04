This Python script is designed for managing duplicate files within a file system. 
Operating in two distinct modes, it caters to both the identification and the subsequent clean-up of duplicate files.

Features:

Scan and Report Mode (-r):

Recursively traverses a specified directory.
Computes SHA-1 hashes to accurately identify duplicates.
Outputs a report (duplicates.txt) listing all duplicates, paired with their original counterparts.
Provides progress updates and handles permissions gracefully, skipping over files that cannot be accessed.
Delete Duplicates Mode (-d):

Reads a user-provided file (expected to be in the format generated by the scan mode).
Safely removes the duplicates listed in the file, leaving the original files intact.
Verifies file existence before deletion and reports any issues encountered during the process.
Usage:
- To find and report duplicates, execute the script with the -r option followed by the target directory path:
  python script_name.py -r /path/to/directory
- To delete duplicates based on a previously generated report, use the -d option followed by the path to the report file:
  python script_name.py -d /path/to/duplicates.txt

Safety Precautions:
The script performs read-write operations. Users are advised to back up important data before running deletion operations.
A clear and user-friendly output ensures you are informed of every step the script takes, granting peace of mind and control over file handling.