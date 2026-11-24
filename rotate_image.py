
import cv2
import matplotlib.pyplot as plt

# Read the previously used image
image = cv2.imread('image.jpg')

# Check whether image is loaded
if image is None:
    print("Error: Image not found!")
else:
    # Display image size
    height, width, channels = image.shape

    print("Original Image Size:")
    print("Height:", height)
    print("Width:", width)
    print("Channels:", channels)

    # Convert BGR to RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Rotate clockwise
    clockwise = cv2.rotate(
        image, cv2.ROTATE_90_CLOCKWISE
    )

    # Rotate anticlockwise
    anticlockwise = cv2.rotate(
        image, cv2.ROTATE_90_COUNTERCLOCKWISE
    )

    # Display all images
    plt.figure(figsize=(12, 5))

    plt.subplot(1, 3, 1)
    plt.imshow(image)
    plt.title("Original Image")
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(clockwise)
    plt.title("Clockwise Rotation")
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(anticlockwise)
    plt.title("Anticlockwise Rotation")
    plt.axis('off')

    plt.tight_layout()
    plt.show()
