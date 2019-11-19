import os
import librtmp, time

conn = librtmp.RTMP("rtmp://10.0.0.174:1935/", "A0 - 0 - 0 - 0 - 6DF129EE266348B3A758145C4C58D9E2 - admin - 888888", live=True)
youtube = librtmp.RTMP("rtmp://a.rtmp.youtube.com/live2/", "dkqx-5w8b-6tby-akrp", subscribe="test123", live=True)
conn.connect()
youtube.connect()
stream = conn.create_stream()
youtube_push = youtube.create_stream(writeable=True)
for y in range(0, 300000):
    data = stream.read(1024000)
    youtube_push.write(data)
