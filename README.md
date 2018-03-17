## InstaPy


#### A Collaborative Software Development Project

<img src="img/logo.png" align="right" border = "10" width="150" height="150"/>

Date: February 9, 2018

#### Overview

According to a [study](http://comp.social.gatech.edu/papers/icwsm15.why.bakhshi.pdf) by Yahoo Labs, “Filtered photos are 21 percent more likely to be viewed and 45 percent more likely to be commented on. Have you ever wondered how you could tranform your images using filters similar to Instagram in Python?

We present this package that performs digital image processing on .png images.  It encompasses functions ranging from transformations like a simple flip, playing with color hues (rgb2gray) to 2D convolutions using a simple kernel matrix to do some interesting things! We have started with quite basic but diverse functions and hope to advance and add more with time.

#### Functions

###### Blur
This function performs convolution to de-emphasizes differences in adjacent pixel values. It has an averaging effect removing detail and noise resulting in blurring of the image.

###### Flip
This is a transformation function which flips the image either horizontally or vertically.

###### Grayscale
This function converts an RGB image to grayscale. "amount" defines the proportion of conversion, with 100% leading to a complete grayscale and a value of 0% does not change the image at all.

*__Non transparent backround .png images required__*

Note: See Usage section below

#### Python ecosystem
"A picture paints a thousand words", however, a well-constructed image speaks even more than that without having to rely on a written description. We want to explore the elements of filters and their implementation in Python. A similar module called ["ImageFilter"](http://pillow.readthedocs.io/en/5.0.0/reference/ImageFilter.html) exists in Python which has standard filters like blur, sharpen, emboss among others.  We have started with a few basic functions but want to work towards building more advanced filters similar to the ones provided by Instagram.

#### Installation

To install InstaPy, follow these instructions:

1. Input the following into the Terminal: pip install git+https://github.com/UBC-MDS/InstaPy.git
2. You are good to go and can start using InstaPy!

#### Usage

*__Non transparent backround .png images required__*

```import InstaPy```

1.```flip(input_path,direction,output_path)```

Arguments:

* ```input_path```: path to input image
* ```direction```: direction of flip. "h" (horizontal) or "v"(vertical)
* ```output_path```: path to output image
* Example: ```flip("./img.png", "h","./img_flip.png")```

2.```blur(input_path,output_path)```

Arguments:

* ```input_path```: path to input image
* ```output_path```: path to output image
* Example: ```blur("./img.png", "./img_blur.png")```

3.```greyscale(input_path,output_path)```

Arguments:

* ```input_path```: path to input image
* ```output_path```: path to output image
* Example: ```greyscale("./img.png", "./img_gs.png")```




#### Package dependencies

```numpy```

```matplotlib.pyplot```

```skimage.io```



#### Collaborators:

[Bhatnagar, Tarini](https://github.com/tarinib)

[Guo, Xin (Alex)](https://github.com/alexguoxin)

[Nikel, Indiana](https://github.com/indiana-nikel)
