import threading

from vidstream import ScreenShareClient

sender=ScreenShareClient('192.168.0.17',9999)


t=threading.Thread(target=sender.start_stream())
t.start()

while input("")!="STOP":
    continue
sender.stop_stream()
