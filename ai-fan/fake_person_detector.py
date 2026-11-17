import config
from detector import Detector
from detect_info import DetectInfo
from detect_result import DetectResult

class FakePersonDetector:
    def __init__(self, detector: Detector, frame_conf: config.Frame):
        self.detector_conf = detector.config
        self.frame_conf = frame_conf
        self.confidences_index = 0
        self.num_confidences = len(self.detector_conf.fake.confidences)

    def detect(self, frame):
        if self.confidences_index == self.detector_conf.fake.raise_error_at:
            raise RuntimeError("Person detection failed")
        detected = []
        confidences = self.detector_conf.fake.confidences[self.confidences_index]
        self.confidences_index = (self.confidences_index + 1) % self.num_confidences
        threshold = self.detector_conf.threshold["person"]
        w = self.frame_conf.width
        region = self.frame_conf.region.copy()
        region[0] = 0
        for i in range(3):
            if confidences[i] < threshold:
                continue
            x = (region[i] + region[i + 1]) // 2 / w
            detected.append(DetectInfo([
                0, 15, confidences[i], x, 10, x, 20
            ]))            
        return DetectResult(self.frame_conf, detected)

        
