# Bangla Sign Language Detection using CNN

This repository is the implementation of [Real-time Vision-based Bangla Sign Language Detection using Convolutional Neural Network](https://ieeexplore.ieee.org/document/9708141) at ICACC 2021.   

## Abstract
Sign Language is an essential means of communication for people with speech and hearing impairment. In spite of this, there are no effective tools to assist the social interaction between Bangla sign language speakers and non-sign language speakers. Our main objective is to implement an automated translation system that is capable of translating Bangla sign language to Bangla text using common computing environments such as a computer and a generic webcam. The dataset has been created for this project with 1500 images for 10 signs. A seven-layered custom sequential CNN model has been trained and validated with the processed dataset. For real-time detection, we have extracted the region of interest and then detected the specified sign. The system runs in real-time and can provide output from a video feed with a time delay of 120.6 ms. Our system has been tested for an accuracy of 97.0%.

## Installation
- clone this github repo:
```
git clone 
```
### create and activate virtual environment

python3 -m venv env
source env/bin/activate

### install dependencies
pip install -r requirements.txt

### run the detector

python main.py
