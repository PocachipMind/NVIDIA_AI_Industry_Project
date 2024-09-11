import cv2
import numpy as np
import onnxruntime as ort
import time  # time 모듈을 추가

def get_class_info():
    data_dict = {0: "Green", 1: "Cross", 2: "D_Cross", 3: "Red"}
    return data_dict

class YOLOv5ONNX:
    def __init__(self, onnx_model_path, confidence_thres=0.5, iou_thres=0.5):
        self.onnx_model_path = onnx_model_path
        self.confidence_thres = confidence_thres
        self.iou_thres = iou_thres

        self.classes = get_class_info()

        self.session = ort.InferenceSession(onnx_model_path, providers=["CUDAExecutionProvider", "CPUExecutionProvider"])

        self.input_name = self.session.get_inputs()[0].name
        self.input_shape = self.session.get_inputs()[0].shape
        self.input_height, self.input_width = self.input_shape[2], self.input_shape[3]

        self.colors = np.random.uniform(0, 255, size=(len(self.classes), 3))

    def preprocess(self, image_path):
        image = cv2.imread(image_path)
        self.original_image = image.copy()
        self.image_height, self.image_width = image.shape[:2]

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = cv2.resize(image, (self.input_width, self.input_height))
        image = image.astype(np.float32) / 255.0
        image = np.transpose(image, (2, 0, 1))
        image = np.expand_dims(image, axis=0)

        return image

    def postprocess(self, outputs):
        outputs = np.squeeze(outputs[0])
        boxes = []
        scores = []
        class_ids = []

        for detection in outputs:
            score = detection[4]
            if score > self.confidence_thres:
                box = detection[:4]
                class_id = np.argmax(detection[5:])
                boxes.append(box)
                scores.append(score)
                class_ids.append(class_id)

        boxes = np.array(boxes)
        boxes[:, 0] = (boxes[:, 0] - boxes[:, 2] / 2) * self.image_width / self.input_width
        boxes[:, 1] = (boxes[:, 1] - boxes[:, 3] / 2) * self.image_height / self.input_height
        boxes[:, 2] = boxes[:, 2] * self.image_width / self.input_width
        boxes[:, 3] = boxes[:, 3] * self.image_height / self.input_height

        return boxes, scores, class_ids

    def draw_detections(self, image, boxes, scores, class_ids):
        for box, score, class_id in zip(boxes, scores, class_ids):
            color = self.colors[class_id]
            label = f"{self.classes[class_id]}: {score:.2f}"
            cv2.rectangle(image, (int(box[0]), int(box[1])), (int(box[0] + box[2]), int(box[1] + box[3])), color, 2)
            cv2.putText(image, label, (int(box[0]), int(box[1]) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

        return image

    def infer(self, image_path):
        # Preprocess the image
        input_data = self.preprocess(image_path)

        # 시작 시간 기록
        start_time = time.time()

        # Run inference
        outputs = self.session.run(None, {self.input_name: input_data})

        # 종료 시간 기록
        end_time = time.time()
        
        # 추론 시간 계산
        inference_time = end_time - start_time
        print()
        print(f"[ onnx ] Inference Time: {1000*inference_time:.4f} microseconds")

        # Postprocess outputs
        boxes, scores, class_ids = self.postprocess(outputs)

        # Draw detections
        output_image = self.draw_detections(self.original_image, boxes, scores, class_ids)

        return output_image

if __name__ == "__main__":
    model_path = "custom_yolo_onnx.onnx"
    yolo_model = YOLOv5ONNX(model_path)

    image_path = "test_img.jpg"
    result_image = yolo_model.infer(image_path)
