import os
import time

while True:
    preDate = time.strftime("%Y%m%d", time.localtime(time.time() - 24*60*60))
    dirPath = "/home/ubuntu/rtmp/" + preDate
    nowDate = time.strftime("%Y%m%d", time.localtime())
    nowTime = time.strftime("%H%M%S", time.localtime())
    print("Now = " + nowDate + "-" + nowTime)
    if (nowTime > "000000" and nowTime < "010000"):
        if os.path.exists(dirPath):
            try:
               os.system("cp -r " + dirPath + " /mnt/mycephfs/rtmp/")
               print("Copy To Cephfs")
               time.sleep(60)
               os.system("rm -r " + dirPath)
               print("Delete PreDay Dir ~")
            except:
               print("Write Cephfs Error !")
    time.sleep(1800)
