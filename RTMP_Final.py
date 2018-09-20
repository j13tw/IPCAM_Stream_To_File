import os, sys
import datetime
import time
import subprocess
import signal

def filename():
    convert_locate = "G:/"
    year = str(datetime.datetime.now().year)
    month = datetime.datetime.now().month
    if (int(month) < 10): month = "0" + str(month)
    else: str(month)
    day = str(datetime.datetime.now().day)
    if (int(day) < 10): day = "0" + str(day)
    else: str(day)
    hour = str(datetime.datetime.now().hour)
    if (int(hour) < 10): hour = "0" + str(hour)
    else: str(hour)
    minute = str(datetime.datetime.now().minute)
    if (int(minute) < 10): minute = "0" + str(minute)
    else: str(minute)
    second = str(datetime.datetime.now().second)
    if (int(second) < 10): second = "0" + str(second)
    else: str(second)
    #print(year, month, day, hour, minute, second)

    convert_locate = convert_locate + year + "-" + month 
    if not os.path.isdir(convert_locate):
        os.mkdir(convert_locate)

    convert_locate = convert_locate + "/" + day 
    if not os.path.isdir(convert_locate):
        os.mkdir(convert_locate)

    convert_locate = convert_locate + "/"

    if not os.path.isdir(convert_locate + "/" + "OK"):
        os.mkdir(convert_locate + "/" + "OK")
    
    if not os.path.isdir(convert_locate + "/" + "Backup"):
        os.mkdir(convert_locate + "/" + "Backup")

    return convert_locate, hour+minute+second

#print(filename()[0], filename()[1])


while (1):
    convert_locate_A = filename()[0] + "OK/" + filename()[1]
    convert_locate_B = filename()[0] + "Backup/" + filename()[1]
#    print(convert_locate_A, convert_locate_B)
    send_command_OK = 'rtmpdump -r "rtmp://10.0.0.174:1935/" -y "A0 - 0 - 0 - 0 - C824C9A84D4000011C3212B0134F13B7 - admin - 888888 - 0" -Y -o ' + convert_locate_A + '.flv -v'
    send_command_Backup = 'rtmpdump -r "rtmp://10.0.0.174:1935/" -y "A0 - 0 - 0 - 0 - C824C9A84D4000011C3212B0134F13B7 - admin - 888888 - 0" -Y -o ' + convert_locate_B + '.flv -v'
    record_OK = subprocess.Popen(send_command_OK)
    time.sleep(0.01)
    record_Backup = subprocess.Popen(send_command_Backup)
#    print(send_command_OK)
#    print(send_command_ERROR)
    time.sleep(600)
    record_OK.kill()
    record_Backup.kill()