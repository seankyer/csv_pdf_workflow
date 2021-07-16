Script made by Sean Kyer at Metro Printers
https://github.com/seankyer/safeway_smart_csv

Example file (with fake names) and example output provided in repository

About Script:
    This script is supposed to extract names from a client provided .CSV file so that the correct amount of pages are
    created when this csv is used as variable data for an InDesign project. This script automatically separated the
    'fold' nametags and 'magnet/pin' nametags (which would be otherwise manually separated after a pdf merge has
    occurred)

Additional Notes:
    1. To make main.py executable by automator (macOs) you must run “chmod u+rwx main.py” into the terminal once inside of
       the applicable directory
    2. A dropped file on safeway_name.app must not contain any spaces or illegal characters
    3. A dropped file on safeway_name.app must be within the /safeway_smart_csv directory