
import cv2
import matplotlib.pyplot as plt

# Read the previously used image
image = cv2.imread('image.jpg')

if image is None:
    print("Error: Image not found!")
else:
    # Convert original image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply histogram equalization
    equalized = cv2.equalizeHist(gray)

    # Calculate histograms
    original_hist = cv2.calcHist(
        [gray], [0], None, [256], [0, 256]
    )

    equalized_hist = cv2.calcHist(
        [equalized], [0], None, [256], [0, 256]
    )

    # Display images and histograms
    plt.figure(figsize=(12, 8))

    plt.subplot(2, 2, 1)
    plt.imshow(gray, cmap='gray')
    plt.title("Original Grayscale Image")
    plt.axis('off')

    plt.subplot(2, 2, 2)
    plt.plot(original_hist)
    plt.title("Original Histogram")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")

    plt.subplot(2, 2, 3)
    plt.imshow(equalized, cmap='gray')
    plt.title("Histogram Equalized Image")
    plt.axis('off')

    plt.subplot(2, 2, 4)
    plt.plot(equalized_hist)
    plt.title("Equalized Histogram")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")

    plt.tight_layout()
    plt.show()

    # Save the equalized image
    cv2.imwrite('equalized_image.jpg', equalized)

    print("Histogram generated successfully!")
    print("Equalized image saved successfully!")
