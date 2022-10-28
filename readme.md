# Bangla Sign Language Detection using CNN

This repository is the implementation of [Real-time Vision-based Bangla Sign Language Detection using Convolutional Neural Network](https://ieeexplore.ieee.org/document/9708141) at ICACC 2021.   

## Abstract
Sign Language is an essential means of communication for people with speech and hearing impairment. In spite of this, there are no effective tools to assist the social interaction between Bangla sign language speakers and non-sign language speakers. Our main objective is to implement an automated translation system that is capable of translating Bangla sign language to Bangla text using common computing environments such as a computer and a generic webcam. The dataset has been created for this project with 1500 images for 10 signs. A seven-layered custom sequential CNN model has been trained and validated with the processed dataset. For real-time detection, we have extracted the region of interest and then detected the specified sign. The system runs in real-time and can provide output from a video feed with a time delay of 120.6 ms. Our system has been tested for an accuracy of 97.0%.

## Dataset
The dataset includes 1500 grayscale images from 10 subjects. The ```dataset``` folder contains the images and the csv files associated with labels.  

## Citation
If this code or part of it, dataset helps you in your research, please cite our paper: 
```
@inproceedings{rafiq2021real,
  title={Real-time Vision-based Bangla Sign Language Detection using Convolutional Neural Network},
  author={Rafiq, Riyad Bin and Hakim, SM Azizul and Tabashum, Thasina},
  booktitle={2021 International Conference on Advances in Computing and Communications (ICACC)},
  pages={1--5},
  year={2021},
  organization={IEEE}
}
```

## Installation
- Clone this github repo:
```
git clone https://github.com/riyadRafiq/bangla-sign-language-detection.git
```
- Create and activate virtual environment
```
python3 -m venv env
source env/bin/activate
```
- Install dependencies
```
pip install -r requirements.txt
```
- Run the detector
```
python main.py
```
