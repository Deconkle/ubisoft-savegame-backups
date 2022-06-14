from os import path, listdir
from zipfile import ZipFile
from datetime import datetime
from time import sleep

def get_ubisoft_id():
    root = "C:\\Program Files (x86)\\Ubisoft\\Ubisoft Game Launcher\\savegames\\"
    if len(listdir(root)) == 1:
        return listdir(root)[0]
    else:
        print("We can't choose what ubisoft ID to use!")
        print("(this script isn't saving anything!!)")
        sleep(1e+5) # sleep forever

save_path = f"C:\\Program Files (x86)\\Ubisoft\\Ubisoft Game Launcher\\savegames\\{get_ubisoft_id()}\\3353"
archive_path = "" # this is where the save backups will be dumped. an empty string ("") means it will be dumped in the scripts current directory


def get_files(save_path): # return all files in savegame location
    return [path.join(save_path, file) for file in listdir(save_path)]

# separator is set to make valid windows filenames, though you may prefer 7:12PM vs 7-12PM
def timestamp(should_zero_pad=False, separator="-"):
    now = datetime.now()
    hour = now.hour
    minute = now.minute
    # what's a strptime()?
    return ( ("0" if should_zero_pad and hour-12 <= 9 else "") + str(hour-12) + separator + str(minute)+"PM" if hour-12 > 0 else ("0" if should_zero_pad and hour<=9 else "") + str(hour) + separator + str(minute)+"AM")

def save():
    fn = archive_path+timestamp(True)+".zip" # 10:18PM.zip
    with ZipFile(fn,'w') as zip: # writing a new zip file
        for file in get_files(save_path): # all files in savegame location
            zip.write(file) # add that file to our new zip file
    print(f"[{timestamp(True, separator=':')}] Successfully backed up WDL gamesave.")

while True:
    save()
    sleep(60*10) # time is in seconds, 60sec * 10 = 10 minutes
