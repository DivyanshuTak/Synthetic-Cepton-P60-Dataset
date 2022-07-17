import numpy as np 
import cv2
import os 





def generate_mask(leaf_phi, leaf_theta, shape, overlap_horizontal, overlap_vertical, diff_vertical, diff_horizontal):
    
    rows, cols = shape
    mask_theta = []
    mask_phi = []
    
    for col in range(1,cols+1):
        for row in range(1,rows+1):
            updated_phi = leaf_phi  + col*(diff_horizontal*(1-overlap_horizontal))
            mask_phi = list(mask_phi) + list(updated_phi)
            updated_theta = leaf_theta - row*(diff_vertical*(1-overlap_vertical))
            mask_theta =  list(mask_theta) + list(updated_theta)
            
    return mask_phi, mask_theta    