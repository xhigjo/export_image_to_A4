from PIL import Image
import cv2
import os
import numpy as np

CUR_DIR = os.path.realpath(__file__).replace("\\","/")
FILENAME = CUR_DIR.split("/")[-1]
CUR_DIR = CUR_DIR.replace(FILENAME, "")

IMAGES_DIR = CUR_DIR + '/images'
images = os.listdir(IMAGES_DIR)

RATIO_DEF = 1.4142
for image in images:
    print(image)

    # use PIL for reading images since cv2 suffers of the "large tEXt chunks" bug of libpng
    img = Image.open(os.path.join(IMAGES_DIR, image)).convert('RGB')
    img_cv = np.array(img)[:, :, ::-1].copy()    # Convert RGB to BGR
    
    print(img_cv.shape)
    width = float(img_cv.shape[1])
    height = float(img_cv.shape[0])
    ratio = width/height

    if ratio >= RATIO_DEF:  # longer than needed => increase height
        height = int(width / RATIO_DEF)
    else:                    # higher than needed => increase width
        width = int(height * RATIO_DEF)

    width = int(width)
    height = int(height)

    print("\n")
    resized = cv2.resize(img_cv,(width,height),interpolation = cv2.INTER_LANCZOS4)
    # resized = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)
    IMAGES_DIR_OUT = os.path.join(CUR_DIR, "images_out")
    cv2.imwrite(os.path.join(IMAGES_DIR_OUT,image), resized)

