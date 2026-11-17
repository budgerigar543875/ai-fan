import config
import cv2
from detect_result import DetectResult
from detector import Detector

class PersonDetector:
    CLASS_ID = 15

    def __init__(self, detector: Detector, frame_conf: config.Frame):
        self.detector = detector
        self.frame_conf = frame_conf

    def detect(self, frame):
        detects = self.detector.detect(frame)
        write_image = self.detector.config.write_image
        frame_size = self.frame_conf.size
        threshold = self.detector.config.threshold["person"]

        detected = []
        for _detect in detects:
            if _detect.class_id != self.CLASS_ID:
                continue
            if _detect.confidence < threshold:
                continue
            detected.append(_detect)
            if write_image:
                top_left, bottom_right = _detect.bounding_box(frame_size)
                cv2.rectangle(
                    frame,
                    top_left.coordinate,
                    bottom_right.coordinate,
                    (0, 255, 0),
                    2
                )

        if write_image:
            cv2.imwrite(self.detector.conf.image_file_path, frame)

        return DetectResult(self.frame_conf, detected)