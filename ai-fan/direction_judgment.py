from detect_result import DetectResult
from temperature_result import TemperatureResult
from direction import Direction

class DirectionJudgment:
    def __init__(
            self, 
            direction_change_threshold: float,
            current: Direction, 
            detect: DetectResult, 
            temp: TemperatureResult
        ):
        self.direction_change_threshold = direction_change_threshold
        self.current = current
        self.detect = detect
        self.temp = temp

    def judge(self) -> Direction:
        left = self.detect.left
        center = self.detect.center
        right = self.detect.right
        if left:
            if right:
                if center:
                    return Direction.NONE
                else:
                    return Direction.CENTER
            else:
                return Direction.RIGHT
        elif right:
            return Direction.LEFT
        elif center:
            if self.current in [Direction.CENTER, Direction.NONE]:
                if self.temp.left >= self.temp.right:
                    return Direction.LEFT 
                else:
                    return Direction.RIGHT
            
            temp_l = self.temp.left
            temp_r = self.temp.right
            if temp_l >= temp_r + self.direction_change_threshold:
                return Direction.LEFT
            elif temp_r >= temp_l + self.direction_change_threshold:
                return Direction.RIGHT
            else:
                return self.current
        else:
            temp_max = self.temp.sorted[0]
            if self.current == Direction.NONE:
                return temp_max[0]
            
            current_temp = self.temp.temperature(self.current)
            if temp_max[1] >= current_temp + self.direction_change_threshold:
                return temp_max[0]
            else:
                return self.current

