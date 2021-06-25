# Artificial-Intelligence
# LICENSE CAR PLATE RECOGNITION SYSTEM

## A. PROJECT SUMMARY



**Project Title:** License Car Plate Recognition System

**Team Members:** 
- Nurin Syafiqah binti Mohd Saofi (B031910122)
- Nur Fatin binti Yazid (B031910017)
- Nor Afieqa binti Mahdi (B031910141)
- NurSyafiqah Adilla binti Mohd Syafiq @ Jackson (B031910324)


**Objectives:**
- To develop an artificial intelligence system that are able to detect Malaysia car number plate
- To develop a system that are able to recognize the character of the car number plate
- To develop an application programming interface (API) for the future ease of use as the integration module
- To use image processing to identify vehicles violating traffic by their plate numbers.


##  B. ABSTRACT 



![System Cover](https://user-images.githubusercontent.com/80866677/122080137-9b0cee00-ce30-11eb-9f67-970be4573f44.png)
Figure 1 shows the AI output of detecting license car plate number.


## C.  DATASET


Given the trained License Car Plate Recognition System, we’ll proceed to implement two more additional Python scripts used to:

- Detect license car plate number in images
- Detect car plate number  in real-time video streams

We’ll wrap up the post by looking at the results of applying our face mask detector.


Video 1

[![Figure 3](![Snapshot_8](https://user-images.githubusercontent.com/80866677/122157113-dd6c1480-ce9c-11eb-8587-6aadbf68e56f.png)](https://user-images.githubusercontent.com/80866677/122157213-0d1b1c80-ce9d-11eb-9c41-c12a945105fe.mp4)

This video was taken from dashcam by a youtuber (Basri Bakar).

This dataset consists of 1 video and xxx images.

Our goal is to train a custom deep learning model to detect car plate number in real life or pictures.

Why we want to create license car plate recognition system?

Violation of traffic legislation has been acknowledged as a major cause of road accidents in most areas of the world. Even if the rules and regulation against them are present, the number of violators is continuously growing. A system must therefore be established to help police agencies enforce these standards in order to improve road safety and reduce road accidents.


## D.   PROJECT STRUCTURE

The following directory is our structure of our project:
- $ tree --dirsfirst --filelimit 10
- .
- ├── dataset
- │   ├── with_mask [690 entries]
- │   └── without_mask [686 entries]
- ├── examples
- │   ├── example_01.png
- │   ├── example_02.png
- │   └── example_03.png
- ├── face_detector
- │   ├── deploy.prototxt
- │   └── res10_300x300_ssd_iter_140000.caffemodel
- ├── detect_mask_image.py
- ├── detect_mask_video.py
- ├── mask_detector.model
- ├── plot.png
- └── train_mask_detector.py
- 5 directories, 10 files


The dataset/ directory contains the data described in the “Our License Car Plate detection dataset” section.

Three image examples/ are provided so that you can test the static image license car plate detector.

We’ll be reviewing three Python scripts in this tutorial:

- train_mask_detector.py: Accepts our input dataset and fine-tunes MobileNetV2 upon it to create our mask_detector.model. A training history plot.png containing accuracy/loss curves is also produced
- detect_mask_image.py: Performs face mask detection in static images
- detect_mask_video.py: Using your webcam, this script applies face mask detection to every frame in the stream

In the next two sections, we will train our license car plate detector.



## E   TRAINING THE COVID-19 FACE MASK DETECTION

We are now ready to train our face mask detector using Keras, TensorFlow, and Deep Learning.

From there, open up a terminal, and execute the following command:

- $ python train_mask_detector.py --dataset dataset
- [INFO] loading images...
- [INFO] compiling model...
- [INFO] training head...
- Train for 34 steps, validate on 276 samples
- Epoch 1/20
- 34/34 [==============================] - 30s 885ms/step - loss: 0.6431 - accuracy: 0.6676 - val_loss: 0.3696 - val_accuracy: 0.8242
- Epoch 2/20
- 34/34 [==============================] - 29s 853ms/step - loss: 0.3507 - accuracy: 0.8567 - val_loss: 0.1964 - val_accuracy: 0.9375
- Epoch 3/20
- 34/34 [==============================] - 27s 800ms/step - loss: 0.2792 - accuracy: 0.8820 - val_loss: 0.1383 - val_accuracy: 0.9531
- Epoch 4/20
- 34/34 [==============================] - 28s 814ms/step - loss: 0.2196 - accuracy: 0.9148 - val_loss: 0.1306 - val_accuracy: 0.9492
- Epoch 5/20
- 34/34 [==============================] - 27s 792ms/step - loss: 0.2006 - accuracy: 0.9213 - val_loss: 0.0863 - val_accuracy: 0.9688
- ...
- Epoch 16/20
- 34/34 [==============================] - 27s 801ms/step - loss: 0.0767 - accuracy: 0.9766 - val_loss: 0.0291 - val_accuracy: 0.9922
- Epoch 17/20
- 34/34 [==============================] - 27s 795ms/step - loss: 0.1042 - accuracy: 0.9616 - val_loss: 0.0243 - val_accuracy: 1.0000
- Epoch 18/20
- 34/34 [==============================] - 27s 796ms/step - loss: 0.0804 - accuracy: 0.9672 - val_loss: 0.0244 - val_accuracy: 0.9961
- Epoch 19/20
- 34/34 [==============================] - 27s 793ms/step - loss: 0.0836 - accuracy: 0.9710 - val_loss: 0.0440 - val_accuracy: 0.9883
- Epoch 20/20
- 34/34 [==============================] - 28s 838ms/step - loss: 0.0717 - accuracy: 0.9710 - val_loss: 0.0270 - val_accuracy: 0.9922
- [INFO] evaluating network...

|      |    precision    | recall| f1-score | support |
|------|-----------------|-------|----------|---------|
|with_mask|0.99|1.00|0.99|138|
|without_mask|1.00|0.99|0.99|138|
|accuracy| | |0.99|276|
|macro avg|0.99|0.99|0.99|276|
|weighted avg|0.99|0.99|0.99|276|


![Figure 4](https://www.pyimagesearch.com/wp-content/uploads/2020/04/face_mask_detector_plot.png)

Figure 4: Figure 10: COVID-19 face mask detector training accuracy/loss curves demonstrate high accuracy and little signs of overfitting on the data

As you can see, we are obtaining ~99% accuracy on our test set.

Looking at Figure 4, we can see there are little signs of overfitting, with the validation loss lower than the training loss. 

Given these results, we are hopeful that our model will generalize well to images outside our training and testing set.


## F.  RESULT AND CONCLUSION

Recognising the license car plate in real-time.


[![Figure5](https://i.ytimg.com/vi/p4SY5vXnL_4/maxresdefault.jpg)](https://www.youtube.com/watch?v=p4SY5vXnL_4)

Figure 5: License Car Plate Recognition in Malaysia

In Figure 5, you can see that license car plate recognition is capable of detecting while the car moves in real time.



## G.   PROJECT PRESENTATION 

In this project, you learned how to create a license car plate recogniser using OpenCV, Keras/TensorFlow, and Deep Learning.

To create our license car plate detector, we trained an image of car plate number and real time video.



[![demo](https://img.youtube.com/vi/-p7HGwOWxtg/0.jpg)](https://www.youtube.com/watch?v=-p7HGwOWxtg "demo")





