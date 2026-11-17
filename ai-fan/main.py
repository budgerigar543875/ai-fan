from camera import Camera
from config import Config
from detector import Detector
from direction import Direction
from direction_judgment import DirectionJudgment
from fan import Fan
from fake_person_detector import FakePersonDetector
from fake_servo_moter import FakeServoMoter
from fake_thermometer import FakeThermometer
from person_detector import PersonDetector
from servo_motor import ServoMotor
from thermometer import Thermometer
import time

camera = None
servo = None
fan = None
thermo = None

config = Config.load("config.json")
person_detector_class = FakePersonDetector if config.detector.fake.enabled else PersonDetector
thermometer_class = FakeThermometer if config.thermometer.fake.enabled else Thermometer
servo_class = FakeServoMoter if config.servo.fake.enabled else ServoMotor

try:
    camera = Camera(config.camera)
    servo = servo_class(config.servo)
    fan = Fan(config.fan)
    thermo = thermometer_class(config.thermometer)
    detector = Detector(config.detector)
    person_detector = person_detector_class(detector, config.camera.frame)

    camera.start()

    while True:
        temp_result = thermo.get()
        frame = camera.get_frame()
        detect_result = person_detector.detect(frame)
        judgement = DirectionJudgment(
            config.temperature.direction_change_threshold,
            servo.current_direction,
            detect_result,
            temp_result
        )
        servo.current_direction = judgement.judge()
        if servo.current_direction == Direction.NONE:
            fan.off()
        else:
            fan.on()

        print(detect_result.left, detect_result.center, detect_result.right)
        print(temp_result.left, temp_result.center, temp_result.right)
        print(servo.current_direction.name)

        time.sleep(config.general.interval)

except KeyboardInterrupt:
    print("end.")
finally:
    if fan is not None:
        fan.cleanup()
    if servo is not None:
        servo.cleanup()
    if camera is not None:
        camera.stop()

