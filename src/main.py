"""files org"""
import argparse, sys
from pathlib import Path
import os
import platform
from datetime import datetime
from PIL import Image, UnidentifiedImageError
from pyluach import dates, hebrewcal, parshios
import shutil
import tempfile

def convert_to_hebrew_calender(year, month) -> (str, str):
    """convert_to_hebrew_calender"""
    
    greg = dates.GregorianDate(int(year), int(month), 1)
    heb_date = greg.to_heb()
    
    #print((heb_date_arr[0], heb_date_arr[1]))
    return (str(heb_date.year), str(heb_date.month).rjust(2, '0'))

def get_file_object_creation_year_month(file):
    """get_file_object_creation_year_month"""
    if platform.system() == 'Windows':
        creation_date = os.path.getctime(file)
    else:
        stat = os.stat(file)
        try:
            creation_date = stat.st_birthtime
        except AttributeError:
            creation_date = stat.st_mtime

    creation_datetime = datetime.fromtimestamp(creation_date)
    year = str(creation_datetime.year)
    month = str(creation_datetime.month)

    return (year, month.rjust(2, '0'))

def get_file_creation_year_month(date_source, file):
    """get_file_creation_year_month"""

    match str(date_source):
        case '1':
            year = file.name[:4]
            month = file.name[4:6]
            return (year, month)

        case '2':
            return get_file_object_creation_year_month(file)
        case '3':
            try:
                exif = Image.open(file).getexif()

                if not exif:
                    return get_file_object_creation_year_month(file)

                if not exif.get(36867):
                    exif_date = exif.get(306) #exif DateTime
                else:
                    exif_date = exif.get(36867) #exit DateTimeOriginal

                year = exif_date[:4]
                month = exif_date[5:7]
                return (year, month)

            except UnidentifiedImageError:
                return  get_file_object_creation_year_month(file)

    return (1980, 1)

def main():
    """main"""
    parser=argparse.ArgumentParser()
    parser.add_argument("--path", "--s",
                    help="source files path",
                    required=True)
    
    parser.add_argument("--dest_path", "--dp",
                    help="destination files path",
                    required=False)
    
    parser.add_argument("--copy", "--c", help="type y to copy file, default is move", default="n", required=False)
    
    parser.add_argument("--calander_type", "--ct",
                    help="calander type: 1 for Gregorian calendar (default), 2 for Hebrew calender",
                    default=1)
    parser.add_argument("--date_source", "--d",
                    help="""create date source: 1 for file name date yyyymmdd,
                    2 for create date field, 
                    3 for create date from the metadata""",
                    required=False,
                    default=2)

    args=parser.parse_args()
    
    # print(f"Args: {args}\nCommand Line: {sys.argv}\n")
    # print(f"calander type: {args.calander_type}")
    # print(f"create date source: {args.date_source}")
    # print(f"Path: {args.path}")
    
    base = Path(args.path)
    total_files = sum(1 for _ in base.iterdir())

    # print(f' base: {base}, total files: {total_files}')
    for i, file in enumerate(base.iterdir()):
        if i % 20 == 0:
            print(f'Files Remaingin: {total_files-i}')

        if file.is_dir():
            continue

        (year, month) = get_file_creation_year_month(args.date_source, file)

        if args.calander_type == '2':
            (year, month) = convert_to_hebrew_calender(year, month)

        dest_path = args.path if args.dest_path is None else args.dest_path

        if os.path.exists(os.path.join(dest_path, year, month)) is False:
            print(f'create dir: {os.path.join(dest_path, year, month)}')
            os.makedirs(os.path.join(dest_path, year, month))

        copy_files = True if str.lower(args.copy) == 'y' else False
        
        if os.path.exists(os.path.join(dest_path, year, month, file.name)) is True:
            new_file_name = f'{datetime.now().strftime("%y%m%d_%H%M%S")}_{file.name}'
        else:
            new_file_name = file.name

        if copy_files:
            print(f'''copy file from:
                  {os.path.join(base, file.name)} 
                  TO: {os.path.join(dest_path, year, month, new_file_name)}''')
            shutil.copyfile(file, os.path.join(dest_path, year, month, new_file_name))
        else:
            print(f'''move file from:
                  {os.path.join(base, file.name)} 
                  TO: {os.path.join(dest_path, year, month, new_file_name)}''')
            shutil.move(file, os.path.join(dest_path, year, month, new_file_name))
        
            
if __name__ == "__main__":
    main()