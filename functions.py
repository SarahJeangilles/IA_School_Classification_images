# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 14:11:04 2021

@author: Lenovo
"""
import numpy as np
import skimage
from skimage.feature import hog
# from skimage.io import imread
# from skimage.transform import rescale
from sklearn.base import BaseEstimator, TransformerMixin
import dash_bootstrap_components as dbc
import dash_html_components as html
import pickle 
import joblib
from layouts import lib

class RGB2GrayTransformer(BaseEstimator, TransformerMixin):
    """
    Convert an array of RGB images to grayscale
    """
 
    def __init__(self):
        pass
 
    def fit(self, X, y=None):
        """returns itself"""
        return self
 
    def transform(self, X, y=None):
        """perform the transformation and return an array"""
        return np.array([skimage.color.rgb2gray(img) for img in X])
     
 
class HogTransformer(BaseEstimator, TransformerMixin):
    """
    Expects an array of 2d arrays (1 channel images)
    Calculates hog features for each img
    """
    def __init__(self, y=None, orientations=9,
                 pixels_per_cell=(8, 8),
                 cells_per_block=(3, 3), block_norm='L2-Hys'):
        self.y = y
        self.orientations = orientations
        self.pixels_per_cell = pixels_per_cell
        self.cells_per_block = cells_per_block
        self.block_norm = block_norm
 
    def fit(self, X, y=None):
        return self
 
    def transform(self, X, y=None):
 
        def local_hog(X):
            return hog(X,
                       orientations=self.orientations,
                       pixels_per_cell=self.pixels_per_cell,
                       cells_per_block=self.cells_per_block,
                       block_norm=self.block_norm)
 
        try: # parallel
            return np.array([local_hog(img) for img in X])
        except:
            return np.array([local_hog(img) for img in X])

def morecontrast(img):
    im = np.multiply(img, 1.5)
    im = np.clip(im, 0, 255)
    return im

class MoreContrast(BaseEstimator, TransformerMixin):
    """
    Augmenter le contraste
    """
 
    def __init__(self):
        pass
 
    def fit(self, X, y=None):
        """returns itself"""
        return self
 
    def transform(self, X, y=None):
        """perform the transformation and return an array"""
        return np.array([morecontrast(img) for img in X])
    
# def mypred(X):
#     model = pickle.load(open('best_model.pkl', 'rb'))
#     return model.predict([X])
    


# if __name__ == '__main__':
#     RGB2GrayTransformer.__module__ = "functions"
#     HogTransformer.__module__ = "functions"
#     app.run_server(debug=True)