# UltimateSecurityCam
---
#### An easy-to-build , un-hack-able security camera which is impossible to fool . "Beginner Friendly"
###### Made with :heart: in python.

##### Working demo video  [here](SampleVid/SecurityCam.mp4)
##### To ask doubts and staying in touch , join our [gitter channel](https://gitter.im/UltimateSecurityCam/Lobby) 

[![Chat at gitter](https://img.shields.io/badge/Chat%20on%20-Gitter-brightgreen.svg)](https://gitter.im/UltimateSecurityCam/Lobby)


## Table of content

- [Introduction](#introduction)
  - [Technologies](#technologies)
  - [Working](#how-it-works)
- [Setup](#setup-instructions)
- [Running](#running)
  - [Linux support](#ultimatesecuritycam-running-on-linux)
  - [Running instructions](#running-instructions)
- [Get in touch](#get-in-touch)



## Introduction
---
[(Back to top)](#list-of-contents)
- This is a security camera software which detects any intruder and alerts the owner .
- This is the basic prototype , we'll make it un-hack-able by using microphone and eliminating every possible hack to fool our software.
- Many issues are up-for-grabs. Check them out from issues tab.


### Technologies:
- `Python 3.6`
- `Opencv (cv2)` [tutorial](https://pythonprogramming.net/loading-images-python-opencv-tutorial/)

### How it works?
We take a snapshot of the room , lets call this `base.jpg`. Now , the code continuously scan the current frame and subtract it from `base.jpg`.
If the difference is more than a threshold , we'll consider a breach happening.



## Setup instructions
---
[(Back to top)](#list-of-contents)
- To run , simply copy the code in the `UltimateSecurityCam.py` and run it.
- More formally , fork the code , and clone it your machine . I recommend that you use the GitH desktop app.
  - If you need a python IDE , I recommend using pycharm. [Tutorial to install : ](https://www.youtube.com/watch?v=QzcaEELafkE).
  - If you get an error , make sure all the **import statements are working** , if not , install using pip-install [tutorial](https://www.youtube.com/watch?v=237dNNQhD3Q)



## Running
---
[(Back to top)](#list-of-contents)

### UltimateSecurityCam running on Linux

Command(with Linux as the working directory):
`python UltimateSecurityCam.py`

![ultimatesecuritycam](https://user-images.githubusercontent.com/30645315/49302849-31d16380-f4ee-11e8-9bfa-4e99866fa3bc.gif)


### Running instructions: 
- Open up `UltimateSecurityCam.py` in your preferred python IDE [UltimateSecurityCam.py](PythonCode/UltimateSecurityCam.py)

- Run using python 3.6 (recommended).
- The program takes 3-second waiting time, after that it starts detecting motion , making an alert sound.

Many improvements and developments are in the pipeline! To know more, contact on github or niteshx22@gmail.com


## Get in touch
---
[(Back to top)](#list-of-contents)

[LinkedIn](https://www.linkedin.com/in/niteshx2/)

[Instagram](https://www.instagram.com/nitz_chaudhry/)

[Facebook](https://www.facebook.com/niteshx2)

[Follow me on Github](https://github.com/NIteshx2)
