# Import the required libraries
import torch
import torchvision
from torchvision.io import read_image
from torchvision.utils import draw_bounding_boxes

# read input image from your computer
img = read_image('C:/Users/pkobzar/depthai-projects/yolov5/runs/train/exp6/weights/best.pt')

# bounding box are xmin, ymin, xmax, ymax
box = [330, 190, 660, 355]
box = torch.tensor(box)
box = box.unsqueeze(0)

# draw bounding box and fill color
img = draw_bounding_boxes(img, box, width=5,
                        colors="green",
                        fill=True)

# transform this image to PIL image
img = torchvision.transforms.ToPILImage()(img)

# display output
img.show()