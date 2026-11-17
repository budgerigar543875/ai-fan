import config
import cv2
from detect_info import DetectInfo

class Detector:
    def __init__(self, conf: config.Detector):
        self.conf = conf
        self.net = cv2.dnn.readNetFromCaffe(
            conf.prototxt_path,
            conf.model_path
        )

    @property
    def config(self):
        return self.conf

    def detect(self, frame) -> list[DetectInfo]:
        blob = cv2.dnn.blobFromImage(
            frame,
            1 / 127.5,
            self.conf.size.to_tuple,
            127.5
        )
        self.net.setInput(blob)

        detects = []
        detections = self.net.forward()
        num_detections = detections.shape[2]
        for i in range(num_detections):
            detects.append(DetectInfo(detections[0, 0, i]))

        return detects
   
