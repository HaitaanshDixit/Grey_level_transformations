import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

input_img = cv.imread(r'.vscode/Projects/dip_project1/me.jpg', 0)

width = int(input_img.shape[1] * 50 / 100)
height = int(input_img.shape[0] * 50 / 100)
inp_img = cv.resize(input_img, (width, height))


#cv.imshow('greyscale', inp_img)
cv.waitKey(0)
cv.destroyAllWindows()

L = 256
neg = L-1-inp_img

plt.figure(figsize=(10,5))
plt.subplot(1,2,1), plt.imshow(inp_img, cmap='gray')
plt.title('Original')
plt.subplot(1,2,2), plt.imshow(neg, cmap='gray')
plt.title('Negative')
plt.show()

