Script made by Sean Kyer at Metro Printers
https://github.com/seankyer/safeway_smart_csv

Example file (with fake names) and example output provided in repository

About Script:
    This script is given a csv file containing names for badges to be laser engraved and a pdf file containing one of
    each distinct name. The CSV file will dictate how many copies should be made for a given name and this script will
    organize and create the write amount of copies of each name depending on their finish (M, P or F/O) and the amount
    of each finish requested

Usage Instructions:
    1. Place namelist.csv into "Desktop/safeway_smart_csv" project folder
    2. Place exported PDF into "Desktop/safeway_smart_csv" project folder
    3. Drag and drop PDF onto automator application
    4. Resulting files will appear in "Desktop/safeway_smart_csv/output"

Additional Notes:
    1. To make main.py executable by automator (macOs) you must run “chmod u+rwx main.py” into the terminal once inside
       of the applicable directory
    2. A dropped file on safeway_name.app must not contain any spaces or illegal characters
    3. A dropped file on safeway_name.app must be within the /safeway_smart_csv directory