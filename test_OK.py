import os, sys
import datetime
import time
import subprocess
import signal

ffmpeg_header = "ffmpeg -rtsp_transport tcp -i "
rtsp_link = "rtsp://10.21.20.229:8554/channel=3/subtype=0/vod="
encoder = " -vcodec h264_nvenc"
fps_set = " -r 30"
convert_locate = "G:/"
record_time = " -ss 00:00:05 -t 00:10:00"
resolution_size = " -s 2560x1440 "
data_format = ".mp4"

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
    
    if not os.path.isdir(convert_locate + "/" + "ERROR"):
        os.mkdir(convert_locate + "/" + "ERROR")

    return convert_locate, hour+minute+second

#print(filename()[0], filename()[1])

while (1):
    convert_locate = filename()[0] + "OK/" + filename()[1]
    send_command = 'rtmpdump -r "rtmp://10.0.0.174:1935/" -y "A0 - 0 - 0 - 0 - C8244C5037F000019141179085601DE4 - admin - 888888 - 0" -Y -o ' + convert_locate + '.flv -v'
    record_OK = subprocess.Popen(send_command)
    print(send_command)
    time.sleep(10)
    record_OK.kill()