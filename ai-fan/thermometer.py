from adafruit_amg88xx import AMG88XX
import board
import config
import time
from temperature_result import TemperatureResult
import numpy as np

class Thermometer:
    def __init__(self, conf: config.Thermometer):
        self.conf = conf
        self.region_index = [
            sum(conf.region_ratio[:1]),
            sum(conf.region_ratio[:2]),
            sum(conf.region_ratio[:3]),
        ]
        i2c = board.I2C()
        self.meter = AMG88XX(i2c, conf.address)
        time.sleep(conf.initial_wait)

    def get(self):
        time.sleep(self.conf.interval)
        pixels = np.array(self.meter.pixels)
        return TemperatureResult(
            np.mean(pixels[:, 0:self.region_index[0]]),
            np.mean(pixels[:, self.region_index[0]:self.region_index[1]]),
            np.mean(pixels[:, self.region_index[1]:self.region_index[2]])
        )
