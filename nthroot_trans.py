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

n = 3
nth_root = inp_img**(1/n)

plt.figure(figsize=(10,5))
plt.subplot(1,2,1), plt.imshow(inp_img, cmap='gray')
plt.title('Original')
plt.subplot(1,2,2), plt.imshow(nth_root, cmap='gray')
plt.title('Nth Root Transformed')
plt.show()