# UltimateSecurityCam
#### An easy-to-build , un-hack-able security camera which is impossible to fool . "Beginner Friendly"
###### Made with :heart: in python.

##### Working demo video  [here](SampleVid/SecurityCam.mp4)
##### To ask doubts and staying in touch , join our [gitter channel](https://gitter.im/UltimateSecurityCam/Lobby) 

[![Chat at gitter](https://img.shields.io/badge/Chat%20on%20-Gitter-brightgreen.svg)](https://gitter.im/UltimateSecurityCam/Lobby)
- This is a security camera software which detects any intruder and alerts the owner .
- This is the basic prototype , we'll make it un-hack-able by using microphone and eliminiting every possible hack to fool our software.
- Many issues are up-for-grabs. Check them out from issues tab.


### Technologies used :
- Python 3.6
- Opencv (CV2) [tutorial](https://pythonprogramming.net/loading-images-python-opencv-tutorial/)

### How it works ?
We take a snapshot of the room , lets call this base.jpg. Now , continuously scan the current frame and subtract it from base.jpg
if the differnce is more than a treshold , we'll consider a breach happening.

## Setup instructions : 
- To run , simply copy the code in the StarterCode.py and run it.
- More formally , fork the code , and clone it your machine . I recommend that you use the github desktop app.
  - If you need a python IDE , I recommend using pycharm. [Tutorial to install : ](https://www.youtube.com/watch?v=QzcaEELafkE).
  - If you get an error , make sure all the **import statements are working** , if not , install using pip-install [tutorial](https://www.youtube.com/watch?v=237dNNQhD3Q)


## Running instructions : 
- Open up StarterCode.py in your preferred python IDE [UltimateSecurityCam.py](PythonCode/UltimateSecurityCam.py)

- Run using python , 3.6 is recommended.
- The program takes 3-second waiting time, after that it starts detecting motion , making an alert sound.

Many improvements and developments are in the pipeline ! to know more, contact on github or niteshx22@gmail.com
