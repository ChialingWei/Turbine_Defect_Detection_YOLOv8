import os
from ultralytics import YOLO
from PIL import Image
import cv2

# model = YOLO('runs/segment/train_basicTrans_remvb/weights/best.pt')
model = YOLO('./weights/best.pt')
root_img_path = ''
for im in os.listdir(root_img_path):
    img_path = os.path.join(root_img_path, im)
    results = model(img_path)
    img = cv2.imread(img_path)
    H, W, _ = img.shape

    # Visualize the results
    for i, r in enumerate(results):
        im_bgr = r.plot()  # BGR-order numpy array
        im_rgb = Image.fromarray(im_bgr[..., ::-1])  # RGB-order PIL image
        # im_rgb.show()
        im_rgb.save(f'/{im}')
