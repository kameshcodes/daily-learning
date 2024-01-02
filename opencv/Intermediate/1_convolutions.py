import numpy as np 
import argparse
import cv2

# When we apply convolution our pixels range our pixel value may go beyond 255 
# so we need to rescale between 0-255 to viz it with openCV
from skimage.exposure import rescale_intensity

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="photo1.jpg", help = "path to the input image")
args = vars(ap.parse_args())


image = cv2.imread(args['image'])
image = cv2.resize(image, (500,300))
cv2.imshow("Original", image)
cv2.waitKey(0)


def convolve(image, kernel):
    (iH, iW) = image.shape[:2]
    (kH, kW) = kernel.shape[:2]
    
    # allocate memory for output image, taking care to pad the borders of the input image so that 
    # the spatial size are not reduced
    pad = (kW-1) // 2
    image = cv2.copyMakeBorder(image, pad, pad, pad, pad,
                               cv2.BORDER_REPLICATE)
    output = np.zeros((iH, iW), dtype="float32")
    
    for y in np.arange(pad, iH + pad):
        for x in np.arange(pad, iW+pad):
            roi = image[y-pad:y+pad+1, x-pad:x-pad+1]
            k = (roi * kernel).sum()
            output[y-pad, x-pad] = k   
    
    output = rescale_intensity(output, in_range = (0,225))
    output = (output*225).astype("uint8")  
    return output    

smallBlur = np.ones((7,7), dtype="float") * (1/49)
largeBlur = np.ones((15,15), dtype='float') * (1/225)

sharpen = np.array((
    [0,-1,0],
    [-1,5,-1],
    [0,-1,0]), dtype = 'int'
)

kernels = (
    ("SmallBlur", smallBlur),
    ("LargeBlur", largeBlur),
    ("Sharpen", sharpen)
)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

for (kernelname, kernel) in kernels:
    convolveOP = convolve(gray, kernel)
    opencvop = cv2.filter2D(gray, -1, kernel)
    cv2.imshow("Original", image)
    cv2.imshow("{} - convolve".format(kernelname), convolveOP)
    cv2.imshow("{} - opencv".format(kernelname), opencvop)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    