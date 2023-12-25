import torch


class YoloV5Detector:
    def __init__(self):
        super().__init__()
        self._load_model()

    def _load_model(self):
        self.model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
        self.model.classes = [0]

    def save_predictions(self, img_path: str, path: str):
        predictions = self.model(img_path)
        return predictions.crop(save=True, save_dir=path)