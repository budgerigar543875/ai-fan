import config
from gpiozero import OutputDevice

class Fan:
    def __init__(self, conf: config.Fan):
        self.device = OutputDevice(
            conf.pin,
            active_high=True,
            initial_value=False
        )

    def on(self):
        self.device.on()
        print("[Fan] On.")

    def off(self):
        self.device.off()
        print("[Fan] Off.")

    def cleanup(self):
        self.off()
        self.device.close()
        print("[Fan] Terminate.")
