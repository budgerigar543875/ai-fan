import config
from picamera2 import Picamera2
import time

class Camera:
    def __init__(self, conf: config.Camera):
        self.conf = conf
        self.camera = Picamera2()
        config = self.camera.create_preview_configuration(
            main={
                "size": conf.frame.size.to_tuple, 
                "format": conf.format
            }
        )
        self.camera.configure(config)

    def start(self):
        self.camera.start()
        time.sleep(self.conf.wait_sec)
        print("[Camera] Start.")
        
    def get_frame(self):
        return self.camera.capture_array()

    def stop(self):
        self.camera.stop()
        print("[Camera] Stop.")
        