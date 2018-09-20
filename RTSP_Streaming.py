import rtsp
client = rtsp.Client(rtsp_server_uri = 'rtsp://10.0.0.174:8554/channel=0/subtype=0/vod=20180917-143030')
client.preview()
client.close()