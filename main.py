import os
from os import path
import time
import calendar

# month dictionary
months = {v: k for k,v in enumerate(calendar.month_abbr)}

# get path of directory
dir_path = input("Enter directory path: ")

# loop through directory
for file in os.listdir(dir_path):

    # file path
    file_path = os.path.join(dir_path, file)

    # get ctime as string
    ctime = time.ctime(os.path.getmtime(file_path))

    # screenshots' ctime will be in this format:
    # DOW MON DY HH:MM:SS YYYY
    # 012345678901234567890123

    # replace white space with 0
    ctime = ctime.replace(" ", "0")

    # properties
    year = ctime[20:]
    month = ctime[4:7]
    day = ctime[8:10]
    hour = ctime[11:13]
    min = ctime[14:16]
    sec = ctime[17:19]

    # convert month from name -> num
    month = str(months[month])
    # add leading zero
    if len(month) == 1:
        month = "0" + month

    # create new name
    file_date = [year, month, day]
    file_date_separator = "-"
    file_time = [hour, min, sec]
    file_time_separator = ":"
    new_name = file_date_separator.join(file_date) + "_" + file_time_separator.join(file_time)

    # print new name
    print("new name: %s" % new_name)