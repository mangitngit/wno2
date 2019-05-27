import numpy as np
import glob
from random import shuffle
import cv2
import sys

addrs = []
labels = []

save = "sroda_rano/save4"
savek = "sroda_rano/savek4"
test = "sroda_rano/test4"
testk = "sroda_rano/testk4"

m = o = r = s = w = b = c = f = i = p = 0
for image in glob.glob("sroda_rano/*/Sample023/*.png"):
    addrs.append(image)
    m += 1
for image in glob.glob("sroda_rano/*/Sample025/*.png"):
    addrs.append(image)
    o += 1
for image in glob.glob("sroda_rano/*/Sample028/*.png"):
    addrs.append(image)
    r += 1
for image in glob.glob("sroda_rano/*/Sample029/*.png"):
    addrs.append(image)
    s += 1
for image in glob.glob("sroda_rano/*/Sample033/*.png"):
    addrs.append(image)
    w += 1
for image in glob.glob("sroda_rano/*/Sample038/*.png"):
    addrs.append(image)
    b += 1
for image in glob.glob("sroda_rano/*/Sample039/*.png"):
    addrs.append(image)
    c += 1
for image in glob.glob("sroda_rano/*/Sample042/*.png"):
    addrs.append(image)
    f += 1
for image in glob.glob("sroda_rano/*/Sample045/*.png"):
    addrs.append(image)
    i += 1
for image in glob.glob("sroda_rano/*/Sample052/*.png"):
    addrs.append(image)
    p += 1

shuffle_data = True  # shuffle the addresses before saving

for x in range(m):
    labels.append(0)
for x in range(o):
    labels.append(1)
for x in range(r):
    labels.append(2)
for x in range(s):
    labels.append(3)
for x in range(w):
    labels.append(4)
for x in range(b):
    labels.append(5)
for x in range(c):
    labels.append(6)
for x in range(f):
    labels.append(7)
for x in range(i):
    labels.append(8)
for x in range(p):
    labels.append(9)

# to shuffle data
if shuffle_data:
    c = list(zip(addrs, labels))
    shuffle(c)
    addrs, labels = zip(*c)

# Divide the hata into 60% train, 20% validation, and 20% test
train_addrs = addrs[0:int(0.8 * len(addrs))]
train_labels = labels[0:int(0.8 * len(labels))]

test_addrs = addrs[int(0.8 * len(addrs)):]
test_labels = labels[int(0.8 * len(labels)):]


def load_image(addr):
    # read an image and resize to (224, 224)
    # cv2 load images as BGR, convert it to RGB
    img = cv2.imread(addr, 0)
    img = cv2.resize(img, (28, 28))
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # ret, img = cv2.threshold(img, 240, 255, cv2.THRESH_BINARY_INV)
    img = img.astype("float32")
    # cv2.imshow('img', img)
    # cv2.waitKey(0)
    return img


a, b, c, d = [], [], [], []
for i in range(len(train_addrs)):
    # print how many images are saved every 1000 images
    if not i % 1000:
        print('Train data: {}/{}'.format(i, len(train_addrs)))
        sys.stdout.flush()
    # Load the image
    img = load_image(train_addrs[i])
    a.append(img)

    label = train_labels[i]
    b.append(label)

a = np.array(a, dtype=np.float32)
b = np.array(b, dtype=np.int32)

np.save(save, a)
np.save(savek, b)

sys.stdout.flush()

for i in range(len(test_addrs)):
    # print how many images are saved every 1000 images
    if not i % 1000:
        print('Test data: {}/{}'.format(i, len(test_addrs)))
        sys.stdout.flush()

    # Load the image
    img = load_image(test_addrs[i])
    c.append(img)

    label = test_labels[i]
    d.append(label)

c = np.array(c, dtype=np.float32)
d = np.array(d, dtype=np.int32)

np.save(test, c)
np.save(testk, d)

sys.stdout.flush()
