#function to create data
from functions import load_image
import numpy as np

def create_background_data(file_list):
    #Creating X_train
    x_train=[]
    y_train=[]
    for file in file_list:
        filename=r'file'
        Image,data=load_image(filename)
        x_train1=data.flatten()
        num_of_rows= x_train1.size//4
        x_train1=x_train1.reshape(num_of_rows,4)
        x_train.append(x_train1)
        y_train1=np.empty(num_of_rows)
        y_train1.fill(0)
        y_train.append(y_train1)
    return x_train,y_train



def create_foreground_data(file_list):
    #Creating X_train
    y_train=[]
    for file in file_list:
        filename=r'file'
        Image,data=load_image(filename)
        x_train=data.flatten()
        num_of_rows= x_train.size//4
        x_train=x_train.reshape(num_of_rows,4)
        x_train.append(x_train)
        y_train1=np.empty(num_of_rows)
        y_train1.fill(1)
        y_train.append(y_train1)
    return x_train,y_train

  
def creating_test_data(file_list):
    test=[]
    for file in file_list:
        filename=r'file'
        Image,data=load_image(filename)
        test1=data.flatten()
        num_of_rows= test1.size//4
        test1=test1.reshape(num_of_rows,4)
        test.append(test1)
    return test
    
        