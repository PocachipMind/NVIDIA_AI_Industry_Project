from PIL import Image
import os
import numpy as np
import torch
import torch.utils.data
import torchvision
from torchvision.models.detection.faster_rcnn import FastRCNNPredictor
from torchvision import transforms as T
import json
import shutil

epochs = 15
num_classes = 6

data_dir = "/home/kimsooyoung/Documents/grocery_data_2024-05-23_16:43:00"
output_file = "/home/kimsooyoung/Documents/model.pth"

device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
print(f"Using device: {device}")

class GroceryDataset(torch.utils.data.Dataset):
    # This function is run once when instantiating the Dataset object
    def __init__(self, root, transforms):
        self.root = root
        self.transforms = transforms

        # In the first portion of this code we are taking our single dataset folder 
        # and splitting it into three folders based on the file types.
        # This is just a preprocessing step.
        list_ = os.listdir(root)
        for file_ in list_:
            name, ext = os.path.splitext(file_)
            ext = ext[1:]
            if ext == '':
                continue

            if os.path.exists(root+ '/' + ext):
                shutil.move(root+'/'+file_, root+'/'+ext+'/'+file_)

            else:
                os.makedirs(root+'/'+ext)
                shutil.move(root+'/'+file_, root+'/'+ext+'/'+file_)

        self.imgs = list(sorted(os.listdir(os.path.join(root, "png"))))
        self.label = list(sorted(os.listdir(os.path.join(root, "json"))))
        self.box = list(sorted(os.listdir(os.path.join(root, "npy"))))
        # We have our three attributes with the img, label, and box data

    # Loads and returns a sample from the dataset at the given index idx
    def __getitem__(self, idx):
        img_path = os.path.join(self.root, "png", self.imgs[idx])
        img = Image.open(img_path).convert("RGB")

        label_path = os.path.join(self.root, "json", self.label[idx])

        with open(os.path.join('root', label_path), "r") as json_data:
            json_labels = json.load(json_data)
        
        box_path = os.path.join(self.root, "npy", self.box[idx])
        dat = np.load(str(box_path))   

        boxes = []
        labels = []
        for i in dat:
            obj_val = i[0]
            xmin = torch.as_tensor(np.min(i[1]), dtype=torch.float32)
            xmax = torch.as_tensor(np.max(i[3]), dtype=torch.float32)
            ymin = torch.as_tensor(np.min(i[2]), dtype=torch.float32)
            ymax = torch.as_tensor(np.max(i[4]), dtype=torch.float32)
            if (ymax > ymin) & (xmax > xmin):
                boxes.append([xmin, ymin, xmax, ymax])
                area = (xmax - xmin) * (ymax - ymin)
            labels += [json_labels.get(str(obj_val)).get('class')]

        label_dict = {}

        # Labels for the dataset
        static_labels = {
            'klt_bin' : 0,
            'tomato_soup' : 1,
            'tuna' : 2,
            'spam' : 3,
            'jelly' : 4,
            'cleanser' : 5
        }

        labels_out = []
        # Transforming the input labels into a static label dictionary to use
        for i in range(len(labels)):
            label_dict[i] = labels[i]

        for i in label_dict:
            fruit = label_dict[i]
            final_fruit_label = static_labels[fruit]
            labels_out += [final_fruit_label]

        target = {}
        target["boxes"] = torch.as_tensor(boxes, dtype=torch.float32)
        target["labels"] = torch.as_tensor(labels_out, dtype=torch.int64)
        target["image_id"] = torch.tensor([idx]) 
        target["area"] = area

        if self.transforms is not None:
            img= self.transforms(img)
        return img, target

    # Finally we have a function for the number of samples in our dataset
    def __len__(self):
        return len(self.imgs)
    
# Create Helper Functions 
# converting to `Tensor` objects and also converting the `dtypes`.
def get_transform(train):
    transforms = []
    transforms.append(T.PILToTensor())
    transforms.append(T.ConvertImageDtype(torch.float))
    return T.Compose(transforms)

# Create a function to collate our samples. 
def collate_fn(batch):
    return tuple(zip(*batch))

# Create Model and Train
# We are starting with the pretrained (default weights) object detection 
# fasterrcnn_resnet50 model from Torchvision.
def create_model(num_classes): 
    model = torchvision.models.detection.fasterrcnn_resnet50_fpn(weights='DEFAULT')
    in_features = model.roi_heads.box_predictor.cls_score.in_features
    model.roi_heads.box_predictor = FastRCNNPredictor(in_features, num_classes) 
    return model

# create our dataset by using our custom GroceryDataset class 
# This is then passed into our DataLoader.
dataset = GroceryDataset(data_dir, get_transform(train=True))
data_loader = torch.utils.data.DataLoader(
    dataset, 
    # batch_size=16, 
    batch_size=8, 
    shuffle=True, 
    collate_fn=collate_fn
)

# create our model with the N classes 
# And then transfer it to the GPU for training.
model = create_model(num_classes)
model.to(device)

params = [p for p in model.parameters() if p.requires_grad]
optimizer = torch.optim.SGD(params, lr=0.001)
len_dataloader = len(data_loader)

# Now we can actually train our model. 
# Keep track of our loss and print it out as we train.
model.train()
ep = 0
for epoch in range(epochs):
    optimizer.zero_grad()
    ep += 1
    i = 0    
    for imgs, annotations in data_loader:
        i += 1
        imgs = list(img.to(device) for img in imgs)
        annotations = [{k: v.to(device) for k, v in t.items()} for t in annotations]
        loss_dict = model(imgs, annotations)
        losses = sum(loss for loss in loss_dict.values())

        losses.backward()
        optimizer.step()

        print(f'Epoch: {ep} Iteration: {i}/{len_dataloader}, Loss: {losses}')

torch.save(model, output_file)
