
import cv2
import argparse
import os

# Set up argument parser
parser = argparse.ArgumentParser(description='Convert an image to a sketch.')
parser.add_argument('input_image', type=str, help='Path to the input image')
args = parser.parse_args()

# Generate output image path
input_image_path = args.input_image
output_image_path = os.path.splitext(input_image_path)[0] + '_sketch.png'

# Read the image
image = cv2.imread(input_image_path)
gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
inverted = 255-gray_image
blur=cv2.GaussianBlur(inverted, (21,21), 0)
invertedblur=255-blur
sketch =cv2.divide(gray_image,invertedblur,scale=256.0)

# Save and display the sketch
cv2.imwrite(output_image_path, sketch)
cv2.imshow("Image", sketch)
cv2.waitKey(0)
cv2.destroyAllWindows()