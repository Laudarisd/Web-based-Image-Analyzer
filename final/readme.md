This is the final darknet directory
Follow these steps to train fruits_360 Kaggle dataset on the YOLOv3 object detector model:
1. download yolov3.weights and save it in this directory
2. run image_resize.py to convert all images into shape (416,416)
  Remember to change filepath in image_resize.py. But the training images should be in data/obj/... folder.
3. run the get_annotations.py to create .txt files for each image with annotated labels.
4. run the create_train_and_text.py to generate the train.txt and test.txt files. Paste these files in data folder.
5. run the get_anchors.py to generate anchors.
6. make changes to cfg/yolov3.cfg file:
  1. change classes
  2. change anchors
  3. change gpu usage to 1 if using GPU
7. run train.py with proper command line arguments
 
