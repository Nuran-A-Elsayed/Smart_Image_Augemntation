# Smart_Image_Augemntation
A interesting way to increase the object instances in a dataset through an augmentation algorithm 

# Segmentation Task To do list
1-save two rectangles of 'background data' and two rectangles of 'tree data' in folders 'foreground' and 'background' respectively

2-write a function to load in the images in a folder and return an ndarray of pixel data (columns are r,g,b, rows are the pixels in each of the images)

3-create a single x_train ndarray from the two arrays created previously, with an associated y_train with a single column containing 1 for foreground pixels and 0 for background pixels.

4-create an KNeighborsClassifier instance and call fit, passing in the above arrays

5-write a function segment that accepts an Pillow image and the classifier, and returns a monochrome 8-bit image containing values of 255 for 'foreground' and 0 for 'background' (call 'predict' on the classifier, passing in the pixel values extracted from the image

6-write a function batch_segment that inputs a input_folder, a CVAT ground truth file containing BB of trees, and an output folder. It will extract original image data for each tree, pass this into segment, save the original data for that tree in one file (per tree), and the 0/255 segmentation mask in another file.

7-If there are errors in the segmentation, add these patches to the 'foreground' or 'background' folder (as appropriate) and re-run the segmentation.

8-We could optionally hand-correct the segmentation mask and pass this data into a supervised segmentation algorithm later.


