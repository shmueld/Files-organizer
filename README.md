# Files organizer By date

### Description
This Python script organizes files into a structured folder hierarchy based on their creation date. It supports multiple calendar systems (Gregorian and Hebrew) and can determine the creation date from various sources (file name, file system metadata, or EXIF data for images).

### Features
    + Flexible date handling: Choose between Gregorian and Hebrew calendars.
    + Multiple date sources: Extract creation dates from file names, file system metadata, or EXIF data.
    + Customizable output: Specify a destination path or use the source path by default.
    + Copying or moving: Choose to either copy or move files to their new locations.
    + Automatic conflict resolution: Renames files with timestamp prefixes to avoid overwriting existing files.
    + Progress tracking: Prints messages indicating the number of files remaining to be processed.

### Usage
```
---
    1. Install required libraries: pip install pyluach

    2. Run the script from the command line: python files_org.py
        Provide arguments as needed:
        --path or -s: The path to the source directory containing the files to organize.
        --dest_path or -dp: (Optional) The path to the destination directory where organized files will be placed. Defaults to the source path.
        --copy or -c: (Optional) Set to 'y' to copy files instead of moving them. Defaults to moving files.
        --calander_type or -ct: (Optional) Set to '2' to use the Hebrew calendar. Defaults to the Gregorian calendar.
        --date_source or -d: (Optional) Set to '1' to use file names, '2' to use file system metadata, or '3' to use EXIF data. Defaults to file system metadata.

---
```