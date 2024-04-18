import threading
import time

from vidstream import CameraClient, StreamingServer

receiving=StreamingServer('192.168.0.17',9999)
sending=CameraClient('192.168.0.172',9999)

t1=threading.Thread(target=receiving.start_server())
t1.start()

time.sleep(4)

t2=threading.Thread(target=sending.start_stream())
t2.start()

while input("")!="STOP":
    continue

receiving.stop_server()
sending.stop_stream()