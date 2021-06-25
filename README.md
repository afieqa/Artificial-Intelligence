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


This dataset consists of 7 images.

Our goal is to train a custom deep learning model to detect car plate number in pictures and from that detection, we can know where the car from.

Why we want to create license car plate recognition system?

Violation of traffic legislation has been acknowledged as a major cause of road accidents in most areas of the world. Even if the rules and regulation against them are present, the number of violators is continuously growing. A system must therefore be established to help police agencies enforce these standards in order to improve road safety and reduce road accidents.


## D.   PROJECT STRUCTURE

The following directory is our structure of our project:
- ├── example
- │   ├── T2.jpg
- │   ├── T9.jpg
- │   ├── T10.jpg
- │   ├── T12.jpg
- │   ├── T14.jpg
- │   ├── T19.jpg
- │   └── T21.jpg
- |
- ├── DP Pict.jpg
- ├── Scanned
- ├── PlateRecognation.py
- ├── PlateRecognationGui.py
- 2 directories, 10 files


The dataset/ directory contains the picture of we will use for this project

Three image examples/ are provided so that you can test the static image license car plate detector.

We’ll be reviewing Two Python scripts in this tutorial:

- PlateRecognation.py: Performs plate car recognation in static image. It will display 5 pictures of step detection plate number
- PlateRecognationGui.py: Using GUI, this will detect license plate number by picture choosen.

In the next two sections, we will show how we use our license car plate detector.



## E   IMPLEMENTION LICENSE CAR PLATE NUMBER

The technique that we use to run the system is:

# **1. Pytesseract**
- Pytesseract or known as Python-tesseract is a tool to read and recognize the text in pictures and licence plates. It change text in picture into string.

![image](https://user-images.githubusercontent.com/80866677/123432571-1e7eca00-d5fd-11eb-9b29-a491016e97c6.png)

# **2. Bilateral Filter**
- known as Gaussian Blur, a non-linear, edge-preserving, and noise-reducing smoothing filter for images. It replaces the intensity of each pixel with a weighted average of intensity values from nearby pixels. This weight can be based on a Gaussian distribution

Original Picture:

![T2](https://user-images.githubusercontent.com/80866677/123433234-cd230a80-d5fd-11eb-84ab-e3d3bd4c4cfe.jpg)

After Bilateral filter process

![image](https://user-images.githubusercontent.com/80866677/123433291-df9d4400-d5fd-11eb-9052-8566c8e5db38.png)


# **3. Canny Edged Detection**
- a multi-stage edge detector operator that employs a vast spectrum of images to detect edges.

![image](https://user-images.githubusercontent.com/80866677/123434905-92ba6d00-d5ff-11eb-84c3-251e9cac3fa7.png)


# **4. imageTK**
- a module contains support to create and modify Tkinter BitmapImage and PhotoImage objects from PIL images.

![image](https://user-images.githubusercontent.com/80866677/123435607-50ddf680-d600-11eb-8d63-1a0b527f7853.png)


## F.  RESULT AND CONCLUSION

Recognising the license car plate in real-time.




## G.   PROJECT PRESENTATION 

In this project, you learned how to create a license car plate recogniser using OpenCV, Keras/TensorFlow, and Deep Learning.





[![demo](https://img.youtube.com/vi/-p7HGwOWxtg/0.jpg)](https://www.youtube.com/watch?v=-p7HGwOWxtg "demo")





