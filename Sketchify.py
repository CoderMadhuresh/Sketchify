import cv2 # image proccessing library
path = r'C:\Users\Dell Pc\Pictures\SampleImage.jpg' # path of the image
image = cv2.imread(path) # reading image using openCv

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #converting BGR image to grayscale(grey)

inverted_image = 250 - gray_image # inverting the image(making negative)

blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)  #blurring the image
inverted_blurred = 250 - blurred # blurring the inverted image

pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0) # creating pencil sketch

cv2.imshow("Original Image", image)            # showing the images
cv2.imshow("Pencil Sketch", pencil_sketch)

cv2.waitKey(0) # time for display window
