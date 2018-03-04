# Copyright 2018 Xin (Alex) Guo
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and limitations under the License.

# This script tests the greyscale() function

# Essentially, both the input and output of the greyscale function are images.
# But the function will convert the image into a matrix contaning RGB values, and just perform matrix manipulation.
# Therefore, for test purposes, the input and output of the test function will just be matrices to test
# if the matrix manipulation works as expected.

import numpy as np
import pytest
from InstaPy import greyscale

# input color: image 1
input1 = np.array([[[10,20,40],
                    [20,40,10],
                    [40,10,20]],   #R values
                   [[20,40,80],
                    [40,80,20],
                    [80,20,40]],   #G values
                   [[30,60,120],
                    [60,120,30],
                    [120,30,60]]   #B values
                  ])

# expected output: greyscale image 1
exp_output1 = np.array([[[18.1,36.2,72.4],
                         [36.2,72.4,18.1],
                         [72.4,18.1,36.2]],  #R values
                        [[18.1,36.2,72.4],
                         [36.2,72.4,18.1],
                         [72.4,18.1,36.2]],  #G values
                        [[18.1,36.2,72.4],
                         [36.2,72.4,18.1],
                         [72.4,18.1,36.2]]   #B values
                         ])

def test_greyscale1():
    assert greyscale(input1) == exp_output1, "Greyscale has been calculated wrong"

# input: greyscale image 2
input2 = np.array([[[10,20,30],
                    [40,50,60],
                    [70,80,90]],   #R values
                   [[10,20,30],
                    [40,50,60],
                    [70,80,90]],   #G values
                   [[10,20,30],
                    [40,50,60],
                    [70,80,90]]    #B values
                  ])

# expected output: identical greyscale image 2
exp_output2 = np.array([[[10,20,30],
                         [40,50,60],
                         [70,80,90]],   #R values
                        [[10,20,30],
                         [40,50,60],
                         [70,80,90]],   #G values
                        [[10,20,30],
                         [40,50,60],
                         [70,80,90]]    #B values
                       ])

def test_greyscale2():
    assert greyscale(input2) == exp_output2, "A greyscale image should still be greyscale"
