from direction import Direction

class TemperatureResult:
    def __init__(self, left: float, center: float, right: float):
        self.temperatures = {
            Direction.LEFT: left,
            Direction.CENTER: center,
            Direction.RIGHT: right,
        }

    def temperature(self, direction: Direction):
        return self.temperatures[direction]
    
    @property
    def left(self) -> float:
        return self.temperature(Direction.LEFT)

    @property
    def center(self) -> float:
        return self.temperature(Direction.CENTER)
    
    @property
    def right(self) -> float:
        return self.temperature(Direction.RIGHT)

    @property
    def sorted(self):
        return sorted(
            self.temperatures.items(),
            key=lambda x: x[1],
            reverse=True
        )
