import os
import time
import calendar
import sys
import errno

# month dictionary
months = {v: k for k,v in enumerate(calendar.month_abbr)}

# exception handling - abort program if true
abort = False

# indefinite loop
while True:

    # get path of directory
    dir_path = ""
    while True:
        dir_path = input("Enter directory path: ")
        if not os.path.isdir(dir_path):
            print("Invalid directory path.")
            continue
        else:
            break

    # file count & total
    i = 0
    total = len([x for x in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, x))])

    # loop through directory
    for file in os.listdir(dir_path):

        # file path
        file_path = os.path.join(dir_path, file)

        # don't count directories
        if os.path.isdir(file_path):
            continue

        # update count
        i += 1

        # print progress
        print("Converting %i of %i..." % (i, total), end="\r")

        # check if file
        if not (os.path.isfile(file_path) and os.path.splitext(file_path)[1].lower() == ".png"):
            print("Skipping %s. (not a PNG file)" % file)
            continue

        # get mtime as string
        mtime = time.ctime(os.path.getmtime(file_path))

        # screenshots' mtime will be in this format:
        # DOW MON DY HH:MM:SS YYYY
        # 012345678901234567890123

        # replace white space with 0
        mtime = mtime.replace(" ", "0")

        # properties
        year = mtime[20:]
        month = mtime[4:7]
        day = mtime[8:10]
        hour = mtime[11:13]
        min = mtime[14:16]
        sec = mtime[17:19]

        # convert month from name -> num
        month = str(months[month])
        # add leading zero
        if len(month) == 1:
            month = "0" + month

        # create new name
        file_date = [year, month, day]
        file_time = [hour, min, sec]
        file_separator = "-"
        new_name = file_separator.join(file_date) + "_" + file_separator.join(file_time) + ".png"
        new_path = os.path.join(dir_path, new_name)

        # attempt to rename
        attempt = 0
        new_path_fix = new_path

        # exception handling
        while True:

            # increment attempt
            attempt += 1

            # try renaming
            try:
                os.rename(file_path, new_path_fix)
                # if successful, exit loop
                break

            # rename failed
            except OSError as e:

                # duplicate name
                if e.errno == errno.EEXIST:
                    # attach number at end
                    new_path_fix = os.path.splitext(new_path)[0] + "_" + str(attempt) + os.path.splitext(new_path)[1]
                    # try again
                    continue

                # permission denied
                elif e.errno == errno.EACCES:
                    print("\nAccess is denied. Please try a different directory.\n")
                    abort = True
                    break

                # other exception
                else:
                    raise

        # abort if exception handling failed
        if abort: break

    # finished
    if not abort: print("\nDone.\n")