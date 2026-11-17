class Size:
    def __init__(self, width: int, height: int):
        self._size = (width, height)

    @property
    def to_tuple(self):
        return self._size

    @property
    def width(self):
        return self.to_tuple[0]
    
    @property
    def height(self):
        return self.to_tuple[1]
    