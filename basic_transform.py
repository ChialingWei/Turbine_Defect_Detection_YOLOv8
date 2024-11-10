import numpy as np
import random
import cv2
import math
import shutil
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

degrees = 20
translate = 0.3
scale = 0.5
shear = 20
perspective = 0.0007
border=(0, 0)
def affine_transform(img, border):
    C = np.eye(3, dtype=np.float32)

    C[0, 2] = -img.shape[1] / 2  # x translation (pixels)
    C[1, 2] = -img.shape[0] / 2  # y translation (pixels)

    # Perspective
    P = np.eye(3, dtype=np.float32)
    P[2, 0] = random.uniform(-perspective, perspective)  # x perspective (about y)
    P[2, 1] = random.uniform(-perspective, perspective)  # y perspective (about x)

    # Rotation and Scale
    R = np.eye(3, dtype=np.float32)
    a = random.uniform(-degrees, degrees)
    # a += random.choice([-180, -90, 0, 90])  # add 90deg rotations to small rotations
    s = random.uniform(1 - scale, 1 + scale)
    # s = 2 ** random.uniform(-scale, scale)
    R[:2] = cv2.getRotationMatrix2D(angle=a, center=(0, 0), scale=s)
    # Shear
    S = np.eye(3, dtype=np.float32)
    S[0, 1] = math.tan(random.uniform(-shear, shear) * math.pi / 180)  # x shear (deg)
    S[1, 0] = math.tan(random.uniform(-shear, shear) * math.pi / 180)  # y shear (deg)

    # Translation
    T = np.eye(3, dtype=np.float32)
    T[0, 2] = random.uniform(0.5 - translate, 0.5 + translate) * size[0]  # x translation (pixels)
    T[1, 2] = random.uniform(0.5 - translate, 0.5 + translate) * size[1]  # y translation (pixels)

    # Combined rotation matrix
    M = T @ S @ R @ P @ C  # order of operations (right to left) is IMPORTANT
    # Affine image
    if (border[0] != 0) or (border[1] != 0) or (M != np.eye(3)).any():  # image changed
        if perspective:
            img = cv2.warpPerspective(img, M, dsize=size, borderValue=(114, 114, 114))
        else:  # affine
            img = cv2.warpAffine(img, M[:2], dsize=size, borderValue=(114, 114, 114))
    return img, M, s

source_folder = ''
destination_folder = ''
for filename in os.listdir(source_folder):
    count = 1
    file = os.path.join(source_folder, filename)
    x = filename.split('.')
    img = cv2.imread(file)
    for num in range(3):
        size = img.shape[1::-1]
        im, _, _ = affine_transform(img, border)
        filename = f"./{x[0]}_{count}.jpg"
        cv2.imwrite(filename, im)
        count += 1



