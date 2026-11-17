import config
from direction import Direction
from detect_info import DetectInfo

class DetectResult:
    def __init__(self, frame_conf: config.Frame, detected: list[DetectInfo]):    
        left, center, right = self._analyze(frame_conf, detected)
        self._detected = {
            Direction.LEFT: left,
            Direction.CENTER: center,
            Direction.RIGHT: right,
        }

    def _analyze(self, frame_conf: config.Frame, detected: list[DetectInfo]):
        left = False
        center = False
        right = False

        region = frame_conf.region
        frame_size = frame_conf.size

        for d in detected:
            top_left, bottom_right = d.bounding_box(frame_size)
            cx = (top_left.x + bottom_right.x) // 2
            if cx < 0:
                continue
            elif cx < region[Direction.LEFT]:
                left |= True
            elif cx < region[Direction.CENTER]:
                center |= True
            elif cx < region[Direction.RIGHT]:
                right |= True
            else:
                continue

        return left, center, right

    @property
    def left(self):
        return self._detected[Direction.LEFT]

    @property
    def center(self):
        return self._detected[Direction.CENTER]

    @property
    def right(self):
        return self._detected[Direction.RIGHT]

    def detected(self, direction: Direction):
        return self._detected[direction]
