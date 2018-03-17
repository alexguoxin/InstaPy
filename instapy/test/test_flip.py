#Copyright 2018 Tarini Bhatnagar
#Licensed under the Apache License, Version 2.0 (the "License")
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0

# March 2018
# This script tests the function from flip.R.

# This script tests flip function of InstaPy package.
# This function flips an image. It takes an argument for direction from the user: horizontal or vertical.
# Input  : An image in .png format
# Output : A flipped image in .png format

import numpy as np
import matplotlib.pyplot as plt
import pytest
import skimage.io
from instapy.flip import flip

#Define test image for horizontal flip


img_horiz = np.array([[[255, 255,  255], [0,  0,  0 ], [0,  0,  0 ]],
                      [[255, 255,255], [255, 255,255], [255, 255,255]],
                      [[255,  255,  255 ], [0,  0,  0 ], [0,  0,  0 ]]], dtype = "uint8")



#Define test image for vertical flip

img_vert =  np.array([[[255, 255, 255 ], [255, 255, 255  ], [255, 255, 255  ]],
                      [[ 0 , 0,  0  ], [  255 , 255,  255  ], [  0 , 0,  0  ]],
                      [[ 0 , 0,  0  ], [  255 , 255,  255  ], [  0 , 0,  0  ]]], dtype = "uint8")



#Expected image matrix for horizontal flip

img_horiz_exp = np.array([[[0,  0,   0], [0, 0,  0  ], [255,  255,  255  ]],
                          [[255, 255,255], [255, 255,255], [255, 255,255]],
                          [[0,  0,   0], [0, 0,  0  ], [255,  255,  255  ]]], dtype = "uint8")


#Expected image matrix for vertical flip

img_vert_exp =   np.array([[[0, 0, 0 ], [255, 255, 255  ], [0, 0, 0  ]],
                      [[ 0 , 0,  0  ], [  255 , 255,  255  ], [  0 , 0,  0  ]],
                      [[ 255, 255, 255  ], [  255 , 255,  255  ], [ 255, 255, 255 ]]], dtype = "uint8")



#Saving test images
skimage.io.imsave("instapy/test/test_img/flip/img_horiz_input.png",img_horiz)
skimage.io.imsave("instapy/test/test_img/flip/img_vert_input.png",img_vert)
skimage.io.imsave("instapy/test/test_img/flip/img_horiz_exp.png",img_horiz_exp)
skimage.io.imsave("instapy/test/test_img/flip/img_vert_exp.png",img_vert_exp)


#Check if image is flipped correctly

#Horizontal flip
def test_flip1():
    flip("instapy/test/test_img/flip/img_horiz_input.png", "h","instapy/test/test_img/flip/flipped_horiz.png")
    output = skimage.io.imread("instapy/test/test_img/flip/flipped_horiz.png")
    test_output = skimage.io.imread("instapy/test/test_img/flip/img_horiz_exp.png")
    assert np.array_equal(output, test_output), "The flip function does not work properly"


#Vertical flip
def test_flip2():
    flip("instapy/test/test_img/flip/img_vert_input.png", "v","instapy/test/test_img/flip/flipped_vert.png")
    output = skimage.io.imread("instapy/test/test_img/flip/flipped_vert.png")
    test_output = skimage.io.imread("instapy/test/test_img/flip/img_vert_exp.png")
    assert np.array_equal(output, test_output), "The flip function does not work properly"
