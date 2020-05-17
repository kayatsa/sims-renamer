import os.path, time, calendar

# month dictionary
months = {v: k for k,v in enumerate(calendar.month_abbr)}

# get path
path = input("Enter file path: ")
ctime = time.ctime(os.path.getctime(path))

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
date = [year, month, day]
date_separator = "-"
time = [hour, min, sec]
time_separator = ":"
separator = "_"
new_name = date_separator.join(date) + "_" + time_separator.join(time)

# print new name
print("new name: %s" % new_name)