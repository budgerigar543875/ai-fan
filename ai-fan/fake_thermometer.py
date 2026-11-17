import config
from temperature_result import TemperatureResult

class FakeThermometer:
    def __init__(self, conf: config.Thermometer):
        self.conf = conf
        self.temperature_index = 0
        self.num_temperatures = len(self.conf.fake.temperatures)

    def get(self):
        if self.temperature_index == self.conf.fake.raise_error_at:
            raise OSError(121, "Remote I/O error")
        temperatures = self.conf.fake.temperatures[self.temperature_index]
        self.temperature_index = (self.temperature_index + 1) % self.num_temperatures
        return TemperatureResult(*temperatures)
