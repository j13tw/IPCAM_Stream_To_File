import os
import librtmp, time, datetime

defaultPath = "/home/ubuntu/rtmp"
if not os.path.exists(defaultPath):
    os.mkdir(defaultPath)

while True:
    now = time.localtime()
    nowDate = time.strftime("%Y%m%d", now)
    nowTime = time.strftime("%H%M%S", now)
    dirPath = defaultPath + "/" + nowDate
    filePath = dirPath + "/" + nowTime + ".flv"
    print(time.strftime("%Y-%m-%d %H:%M:%S") + " / " + str(datetime.datetime.now()) + " : Create " +filePath)
    if not os.path.exists(dirPath):
        os.mkdir(dirPath)
    if os.path.isfile(filePath):
        os.remove(filePath)
    videoFile = open(filePath, "wb")
    conn = librtmp.RTMP("rtmp://10.0.0.174:1935/", "A0 - 0 - 0 - 0 - 6DF129EE266348B3A758145C4C58D9E2 - admin - 888888", live=True)
    conn.connect()
    stream = conn.create_stream()
    for y in range(0, 600000):
        data = stream.read(1024)
        videoFile.write(data)
    videoFile.close()
