from pydantic import BaseModel
from direction import Direction
import json
from size import Size

class General(BaseModel):
    interval: float

class Temperature(BaseModel):
    direction_change_threshold: float

class FakeDetector(BaseModel):
    enabled: bool
    confidences: list[list[float]]
    # -1: エラーを発生させない
    raise_error_at: int

class Detector(BaseModel):
    model_path: str
    prototxt_path: str
    threshold: dict[str, float]
    width: int
    height: int
    write_image: bool
    image_file_path: str
    fake: FakeDetector

    @property
    def size(self):
        return Size(self.width, self.height)

class FakeServo(BaseModel):
    enabled: bool
    # -1: エラーを発生させない
    raise_error_at: int

class Servo(BaseModel):
    pin: int
    left: float
    center: float
    right: float
    fake: FakeServo

class Fan(BaseModel):
    pin: int

class Frame(BaseModel):
    width: int
    height: int
    region: dict[Direction, int]

    @property
    def size(self):
        return Size(self.width, self.height)

class Camera(BaseModel):
    wait_sec: float
    format: str
    frame: Frame

class FakeThermometer(BaseModel):
    enabled: bool
    temperatures: list[list[float]]
    # -1: エラーを発生させない
    raise_error_at: int

class Thermometer(BaseModel):
    address: int
    initial_wait: float
    interval: float
    region_ratio: list[int]
    fake: FakeThermometer

class Config(BaseModel):
    general: General
    temperature: Temperature
    detector: Detector
    servo: Servo
    fan: Fan
    camera: Camera
    thermometer: Thermometer

    @staticmethod
    def load(file_path:str):
        with open(file_path, "r", encoding="utf-8") as f:
            config = json.load(f)
        return Config(**config)
