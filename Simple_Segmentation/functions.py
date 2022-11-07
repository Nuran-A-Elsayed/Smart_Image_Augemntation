from PIL import image as im
import numpy as np
from numpy import asarray
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier

def load_image(filename):
    im=im.open(filename)
    data = np.array(im)
    return im,data


def create_knn_model(x_train,y_train):
    knn = KNeighborsClassifier(n_neighbors = 2)
    knn.fit(x_train,y_train)
    return knn

def segment(image_as_array,classifier):

    prediction=classifier.predict(image)
    pixel_number=prediction.shape[0]
    image=image.reshape(pixel_number,1,4)
    # data3.setflags(write=1)
    for pixel in range(pixel_number):
        if prediction[pixel]==0:
            
            image[pixel]= [0,0,0,255]
    

