# Files organizer By date

### About
This utility effortlessly organizes files within a directory based on their creation dates.

### Features
    + Sorts files into subdirectories based on their creation dates (year and month).
    + Copy or Move the files
    + Get the creation date from file name yyyymmdd* or file info or Exif
    + Support Hebrew Calander

### Using
```
---
    usage: main.py [-h] --path PATH [--dest_path DEST_PATH] [--copy COPY] [--calander_type CALANDER_TYPE] [--date_source DATE_SOURCE]

    options:
        -h, --help            show this help message and exit
        --path PATH, --s PATH source files path
        --dest_path DEST_PATH, --dp DEST_PATH destination files path
        --copy COPY, --c COPY type y to copy file, default is move
        --calander_type CALANDER_TYPE, --ct CALANDER_TYPE calander type: 1 for Gregorian calendar (default), 2 for Hebrew calender
        --date_source DATE_SOURCE, --d DATE_SOURCE create date source: 1 for file name date yyyymmdd, 2 for create date field, 3 for create date from the metadata
---
```