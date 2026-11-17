import config
from direction import Direction
from gpiozero import Servo
import time

class ServoMotor:
    def __init__(self, conf: config.Servo):
        self.servo = Servo(
            conf.pin,
            initial_value=None
        )
        self.conf = conf
        self.direction = Direction.NONE

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

    def _move(self, value: float):
        self.servo.value = value
        time.sleep(1)
        self.servo.detach()

    def move(self, direction: Direction):
        match(direction):
            case Direction.LEFT:
                self.move_left()
            case Direction.CENTER:
                self.move_center()
            case Direction.RIGHT:
                self.move_right()

    def move_left(self):
        self._move(self.conf.left)
        print("[Servo] Move LEFT.")

    def move_center(self):
        self._move(self.conf.center)
        print("[Servo] Move CENTER.")

    def move_right(self):
        self._move(self.conf.right)
        print("[Servo] Move RIGHT.")

    def cleanup(self):
        self.servo.detach()
        self.servo.close()
        print("[Servo] Terminate.")