#Copyright 2018 Tarini Bhatnagar
#Licensed under the Apache License, Version 2.0 (the "License")
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0

# March 2018
# This script is for function flip.

#Package dependencies
import numpy as np
import skimage.io


def flip(img, direction,output_path):
    '''
    Flips an image in either horizonatl or vertical direction
    Arguments:
        img: path of input file
        direction: direction of flip, horizontal="h", vertical = "v"
    Output: an image file in .png format
    '''

    assert direction in ["h","v"], "Invalid input for flip direction"
  
    try:
        input_mat = skimage.io.imread(img)
    except AttributeError:
        print("Please provide a string as the path for the input image file.")
        raise
    except TypeError:
        print("Please provide a string as the path for the input image file.")
        raise
    except FileNotFoundError:
        print("The input file/path does not exist.")
        raise
    except OSError:
        print("The input file is not an image.")
        raise
    except Exception as e:
        print("General Error:")
        print(e)
        raise
    
    
    #Loop for direction to be either horizontal or vertical
    
    #Vertical Flip
    if direction == "v":
        asc=range(0, input_mat.shape[0])
        desc=list(reversed(asc))
        output_mat = input_mat.copy()
        output_mat[asc] = input_mat[desc]

    #Horizontal Flip
    elif direction == "h":
        asc=range(0, input_mat.shape[1])
        desc=list(reversed(asc))
        output_mat = input_mat.copy()
        output_mat[:,asc] = input_mat[:,desc]
   
        
    #Converting data type
    output_mat=np.array(output_mat, dtype=np.uint8)
    
    #Save flipped image 
    
    try:
        skimage.io.imsave(output_path, output_mat)
    except AttributeError:
        print("Please provide a string as the path for the input image file.")
        raise
    except TypeError:
        print("Please provide a string as the path for the output image file.")
        raise
    except FileNotFoundError:
        print("The output path does not exist.")
        raise
    except Exception as e:
        print("General Error:")
        print(e)
        raise