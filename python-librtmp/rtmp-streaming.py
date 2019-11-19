import os
import librtmp, time
import cv2
import numpy as np

fileOutput = "./test.flv"
if os.path.isfile(fileOutput):
    os.remove(fileOutput)
videoFile = open(fileOutput, "wb")

conn = librtmp.RTMP("rtmp://10.0.0.174:1935/", "A0 - 0 - 0 - 0 - 6DF129EE266348B3A758145C4C58D9E2 - admin - 888888", live=True)
conn.connect()
stream = conn.create_stream()
for y in range(0, 300000):
    print(y)
    data = stream.read(1024)
    videoFile.write(data)
videoFile.close()
