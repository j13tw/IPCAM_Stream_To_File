import os
import librtmp, time

conn = librtmp.RTMP("rtmp://10.0.0.174:1935/", "A0 - 0 - 0 - 0 - 6DF129EE266348B3A758145C4C58D9E2 - admin - 888888", live=True)
conn.connect()
stream = conn.create_stream()
print(conn.connected)
