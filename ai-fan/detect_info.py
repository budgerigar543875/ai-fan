from coordinate import Coordinate
from size import Size

class DetectInfo:
    def __init__(self, detect: list):
        self.info = detect

    @property
    def class_id(self):
        return self.info[1]

    @property
    def confidence(self):
        return self.info[2]

    @property
    def x_min(self):
        return self.info[3]

    @property
    def y_min(self):
        return self.info[4]

    @property
    def x_max(self):
        return self.info[5]

    @property
    def y_max(self):
        return self.info[6]

    def bounding_box(self, frame_size: Size):
        w = frame_size.width
        h = frame_size.height
        return (
            Coordinate(int(self.x_min * w), int(self.y_min * h)),
            Coordinate(int(self.x_max * w), int(self.y_max * h))
        )