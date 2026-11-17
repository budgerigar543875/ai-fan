class Coordinate:
    def __init__(self, x: int, y: int):
        self._coordinate = (x, y)

    @property
    def coordinate(self):
        return self._coordinate

    @property
    def x(self):
        return self.coordinate[0]

    @property
    def y(self):
        return self.coordinate[1]
