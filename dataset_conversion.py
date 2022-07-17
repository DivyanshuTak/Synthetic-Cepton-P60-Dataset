import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 
import datetime 
import os 
import cv2
import open3d as o3d
from PIL import Image 
from inverse_project import *
from generate_mask import *
import pickle 


# load the masks 
mask_theta = np.load("mask/mask_theta.npy")
mask_phi = np.load("mask/mask_phi.npy")

# recreate the mask 
mask = np.zeros((len(mask_phi), 2))
mask[:,0] = mask_phi
mask[:,1] = mask_theta


### STEPS 
# load a image 
# convert to pointcloud 
# estimate theta, phi
# sample using mask 
# save the new pointcloud 
###





