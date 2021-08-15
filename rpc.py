from pypresence import Presence
from datetime import datetime, timedelta
from cloudutils import NeteaseMusicUtils
import time

CLIENT_ID = "598527185820712981"

RPC = Presence(CLIENT_ID)
RPC.connect()
api = NeteaseMusicUtils()

while True:
    currsong = api.getCurrentSong()
    songname, singer = currsong.split('-')
    RPC.update(
        details=songname,
        state='by' + singer,
        large_image="music",
        large_text="zn music",
        start=(datetime.now() - timedelta(seconds=api.getTime()['curr'])).timestamp(),
        end=(datetime.now() + timedelta(seconds=api.getTime()['diff'])).timestamp()
    )
    time.sleep(10)