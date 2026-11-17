import config
from direction import Direction

class FakeServoMoter:
    def __init__(self, conf: config.Servo):
        self.conf = conf
        self.direction = Direction.NONE
        self.move_count = 0

    @property
    def current_direction(self):
        return self.direction

    @current_direction.setter
    def current_direction(self, direction: Direction):
        if self.direction != direction:
            self.move(direction)
            self.direction = direction
        else:
            print(f"[Servo] Direction {self.direction.name} continue.")

    def move(self, direction: Direction):
        if self.move_count == self.conf.fake.raise_error_at:
            raise RuntimeError("Servo motor failed")
        self.move_count += 1
        match(direction):
            case Direction.LEFT:
                self.move_left()
            case Direction.CENTER:
                self.move_center()
            case Direction.RIGHT:
                self.move_right()

    def move_left(self):
        print("[Servo] Move LEFT.")

    def move_center(self):
        print("[Servo] Move CENTER.")

    def move_right(self):
        print("[Servo] Move RIGHT.")

    def cleanup(self):
        print("[Servo] Terminate.")