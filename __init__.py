"""
File Organizer

This script allows the user to organize files in a directory (including subdirectories) 
by their last modified date. Each file is moved to a folder named after its last modified date.

This script requires that `os`, `shutil`, and `datetime` be installed within the Python
environment you are running this script in.

This file can also be imported as a module and contains the following functions:

    * sort_files_by_date - the main function of the script
"""

import os
import shutil
import datetime

def sort_files_by_date(folder_path):
    """
    Sorts files in a directory (including subdirectories) by their last modified date.

    Parameters:
        folder_path (str): The path of the directory to sort files in

    Returns:
        None
    """

    # Create a dictionary to store files based on their dates
    files_by_date = {}

    # Iterate over each file in the directory tree
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)

            # Get the last modified date of the file
            modification_time = os.path.getmtime(file_path)
            modification_date = datetime.datetime.fromtimestamp(modification_time).date()

            # Add the file to the dictionary based on its date
            if modification_date in files_by_date:
                files_by_date[modification_date].append(file_path)
            else:
                files_by_date[modification_date] = [file_path]

    # Create folders for each date and move the files into the respective folders
    for date, files in files_by_date.items():
        folder_name = str(date)
        new_folder_path = os.path.join(folder_path, folder_name)

        # Create the folder if it doesn't exist
        if not os.path.exists(new_folder_path):
            os.makedirs(new_folder_path)

        # Move the files into the folder
        for file_path in files:
            shutil.move(file_path, new_folder_path)

def main():
    # Usage example
    folder_path = r"C:\Users\meow25\_____path______"
    sort_files_by_date(folder_path)

if __name__ == "__main__":
    main()