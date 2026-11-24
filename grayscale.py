import cv2
import matplotlib.pyplot as plt

# Read the input image
image = cv2.imread('image.jpg')

# Convert the image into grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display only the grayscale image
plt.imshow(gray_image, cmap='gray')
plt.axis('off')
plt.show()
import cv2
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread('image.jpg')

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display grayscale image
plt.imshow(gray_image, cmap='gray')
plt.axis('off')
plt.show()