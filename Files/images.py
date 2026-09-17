import cv2

# Load an image from the Images folder
image = cv2.imread("../Images/image1.jpg")

# Check whether the image was loaded successfully
if image is None:
    print("Error: Image could not be loaded.")
else:
    print("Image loaded successfully.")
    print("Image dimensions:", image.shape)

    # Display the image
    cv2.imshow("My Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
