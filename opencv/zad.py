import PIL.Image as Image
import numpy as np
import cv2
import glob

images = []

# WCZYTANIE
for img in glob.glob("*.*"):
    if img != "zad.py":
        images.append(cv2.imread(img, 1))

width, num = 500, 0

for image in images:
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    if num == 4:
        ret, thresh = cv2.threshold(image_gray, 221, 255, cv2.THRESH_BINARY_INV)
    elif num == 7:
        ret, thresh = cv2.threshold(image_gray, 211, 255, cv2.THRESH_BINARY_INV)
    else:
        ret, thresh = cv2.threshold(image_gray, 240, 255, cv2.THRESH_BINARY_INV)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # WYSZUKANIE NAJLEPSZEGO KONTURU WŚRÓD ZNALEZIONYCH
    maximum, i = 0, []
    for contour in contours:
        if cv2.contourArea(contour) > maximum:
            maximum = cv2.contourArea(contour)
            i = contour
    cnt = i

    # WYCIĘCIE TŁA
    mask = np.zeros(image_gray.shape, np.uint8)
    cv2.drawContours(mask, [cnt], 0, 255, -1)
    image = cv2.bitwise_and(image, image, mask=mask)

    # ODPOWIEDNIE OBRÓCENIE MIECZY
    (x, y), (MA, ma), angle = cv2.fitEllipse(cnt)
    if num == 4:
        rot_mat = cv2.getRotationMatrix2D((x, y), angle - 90, 1.0)
    else:
        rot_mat = cv2.getRotationMatrix2D((x, y), angle + 90, 1.0)

    # OBRÓCENIE WOKÓŁ ŚRODKA CIĘŻKOŚCI MIECZA
    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)
    cos = np.abs(rot_mat[0, 0])
    sin = np.abs(rot_mat[0, 1])
    nW = int((h * sin) + (w * cos))
    nH = int((h * cos) + (w * sin))
    rot_mat[0, 2] += (nW / 2) - cX
    rot_mat[1, 2] += (nH / 2) - cY
    res = cv2.warpAffine(image, rot_mat, (nW, nH), flags=cv2.INTER_LINEAR)

    coordinate_character = Image.fromarray(res).getbbox()
    res = res[coordinate_character[1]:coordinate_character[3], coordinate_character[0]:coordinate_character[2]]

    # PRZESKALOWANIE
    scale = width / res.shape[1]
    height = int(scale * res.shape[0])
    res = cv2.resize(res, (width, height))

    # ZAPIS
    # resa = np.array(res)
    # resb = Image.fromarray(resa)
    # resb.save("{:2}".format(num)+".png")

    cv2.imshow("im", res)
    cv2.waitKey(0)
    num += 1
