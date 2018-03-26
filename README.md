# InstaPy

[![Build Status](https://travis-ci.org/UBC-MDS/InstaPy.svg?branch=master)](https://travis-ci.org/UBC-MDS/InstaPy)

DSCI 524 Collaborative Software Development Project

<img src="img/logo.png" align="right" border = "10" width="150" height="150"/>

February 9, 2018

### Overview

According to a [study](http://comp.social.gatech.edu/papers/icwsm15.why.bakhshi.pdf) by Yahoo Labs, “Filtered photos are 21 percent more likely to be viewed and 45 percent more likely to be commented on.” Have you ever wondered how you could tranform your images using filters similar to Instagram in Python?

We present this package that performs digital image processing on .jpg images.  It encompasses functions ranging from transformations like a simple flip, playing with color hues (rgb2gray) to 2D convolutions using a simple kernel matrix to do some interesting things! We have started with quite basic but diverse functions and hope to advance and add more with time.

### Functions

- Blur

This function performs convolution to de-emphasizes differences in adjacent pixel values. It has an averaging effect removing detail and noise resulting in blurring of the image.

- Flip

This is a transformation function which flips the image either horizontally or vertically.

- Greyscale

This function converts an RGB image to grayscale. 

Note: See Usage section below

### Python Ecosystem

"A picture paints a thousand words", however, a well-constructed image speaks even more than that without having to rely on a written description. We want to explore the elements of filters and their implementation in Python. A similar module called ["ImageFilter"](http://pillow.readthedocs.io/en/5.0.0/reference/ImageFilter.html) exists in Python which has standard filters like blur, sharpen, emboss among others.  We have started with a few basic functions but want to work towards building more advanced filters similar to the ones provided by Instagram.

### Installation

To install InstaPy, follow these steps in Terminal:

1. Clone InstaPy repository to your local machine 
``` 
git clone https://github.com/UBC-MDS/InstaPy.git
```

2. Navigate to the cloned repository.

3. Type ```python setup.py install```

4. You are good to go and can start using `InstaPy`! See usage below to see how to import functions.

### Usage

```from Instapy.blur import blur```

```from Instapy.flip import flip```

```from Instapy.greyscale import greyscale```

1.```flip(input_path, direction, output_path)```

Arguments:

* ```input_path```: path to input image
* ```direction```: direction of flip. "h" (horizontal) or "v"(vertical)
* ```output_path```: path to output image
* Example: ```flip("./img.jpg", "h","./img_flip.jpg")```

2.```blur(input_path, output_path)```

Arguments:

* ```input_path```: path to input image
* ```output_path```: path to output image
* Example: ```blur("./img.jpg", "./img_blur.jpg")```

3.```greyscale(input_path, output_path)```

Arguments:

* ```input_path```: path to input image
* ```output_path```: path to output image
* Example: ```greyscale("./img.jpg", "./img_gs.jpg")```

### Package Dependencies

```numpy```

```matplotlib.pyplot```

```skimage.io```

### Collaborators:

[Bhatnagar, Tarini](https://github.com/tarinib)

[Guo, Xin (Alex)](https://github.com/alexguoxin)

[Nikel, Indiana](https://github.com/indiana-nikel)
