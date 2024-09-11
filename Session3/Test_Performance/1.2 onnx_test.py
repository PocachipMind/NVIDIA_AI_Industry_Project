import cv2
import numpy as np
import onnxruntime as ort

def get_class_info():
    # 여기에 모델의 클래스 정보가 들어갑니다. 이 부분은 실제 클래스 이름으로 수정해야 합니다.
    data_dict = {0: "Green", 1: "Cross", 2: "D_Cross", 3: "Red"}  # 수정 필요
    return data_dict

class YOLOv5ONNX:
    def __init__(self, onnx_model_path, confidence_thres=0.5, iou_thres=0.5):
        self.onnx_model_path = onnx_model_path
        self.confidence_thres = confidence_thres
        self.iou_thres = iou_thres

        # Load the class names
        self.classes = get_class_info()

        # Load the ONNX model
        self.session = ort.InferenceSession(onnx_model_path, providers=["CUDAExecutionProvider", "CPUExecutionProvider"])

        # Get model input details
        self.input_name = self.session.get_inputs()[0].name
        self.input_shape = self.session.get_inputs()[0].shape
        self.input_height, self.input_width = self.input_shape[2], self.input_shape[3]

        # Generate random colors for each class
        self.colors = np.random.uniform(0, 255, size=(len(self.classes), 3))

    def preprocess(self, image_path):
        # Load image
        image = cv2.imread(image_path)
        self.original_image = image.copy()
        self.image_height, self.image_width = image.shape[:2]

        # Convert color to RGB
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Resize image to match model input size
        image = cv2.resize(image, (self.input_width, self.input_height))

        # Normalize the image
        image = image.astype(np.float32) / 255.0

        # Convert to CHW format
        image = np.transpose(image, (2, 0, 1))

        # Add batch dimension
        image = np.expand_dims(image, axis=0)

        return image

    def postprocess(self, outputs):
        # Reshape and transpose outputs
        outputs = np.squeeze(outputs[0])

        # Extract boxes, scores, and classes
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

        # Scale boxes back to original image size
        boxes = np.array(boxes)
        boxes[:, 0] = (boxes[:, 0] - boxes[:, 2] / 2) * self.image_width / self.input_width  # x_center to x_min
        boxes[:, 1] = (boxes[:, 1] - boxes[:, 3] / 2) * self.image_height / self.input_height  # y_center to y_min
        boxes[:, 2] = boxes[:, 2] * self.image_width / self.input_width  # width
        boxes[:, 3] = boxes[:, 3] * self.image_height / self.input_height  # height

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

        # Run inference
        outputs = self.session.run(None, {self.input_name: input_data})

        # Postprocess outputs
        boxes, scores, class_ids = self.postprocess(outputs)

        # Draw detections
        output_image = self.draw_detections(self.original_image, boxes, scores, class_ids)

        return output_image

if __name__ == "__main__":
    # Initialize the model
    model_path = "custom_yolo_onnx.onnx"
    yolo_model = YOLOv5ONNX(model_path)

    # Specify the image path
    image_path = "test_img.jpg"

    # Perform inference
    result_image = yolo_model.infer(image_path)

    # Save and display the output image
    cv2.imwrite("result_onnx.png", result_image)
    cv2.imshow("Result", result_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
