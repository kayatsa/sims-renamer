# Sims 4 Screenshots Renamer

Renames Sims 4 screenshots to allow them to be alphabetically and chronologically ordered at the same time.

## Supported Devices

Currently, this is only a script, not an executable. Therefore, you will need to run the script using Python 3.

To ensure that you have all packages needed to run this script successfully, enter this command while working in the project's directory:

`pip install -r requirements.txt`

## Usage

This script is meant to rename Sims 4 screenshots since the default file name does not allow them to be ordered alphabetically and chronologically at the same time.

The files will be renamed to the format **YYYY-MM-DD_HH-MM-SS**, corresponding to the file's "Last modified" date and time.

This script can be used to rename any PNG file; it only checks if the files are PNG, not if they are screenshots from the Sims 4.

1. Open main.py with Python.
2. You will be prompted for a directory path. Enter the path of the folder that contains the files you want to rename, then press ENTER.
3. The script will run and will let you know if any files were not renamed and why.
4. Enter another directory path if you have another folder with files to rename. Otherwise, close out of the program.

## Pending Features

No pending features.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
