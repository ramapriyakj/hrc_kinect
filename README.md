Human-Robot Collaboration (HRC) - Kinect Camera
============

by Ramapriya Kyathanahally Janardhan (janardhan@campus.tu-berlin.de)

Below are the instructions to succesfully install and run the Human-Robot Collaboration (HRC) - Kinect camera code.

---

Note:
*	The project can be used to generate kinect camera data set for tensor flow testing and training.
*	writeToFile method under HumanActionRecognition.py file needs to be called from processFrame method to generate data sets.
*	Currently the code prints the frames on terminal that will be sent to tensorflow code for detection.
*	Currently the tensor flow model is not completely developed to detect human action and state of mind for kinect camera.
*	The project can hence be used as a base to integrate tensor flow code to detect human action and state of mind.

## Running

*   Run HumanActionRecognition.py

```
roscore
cd hrc_kinect
catkin_make
source devel/setup.bash
rosrun hrckinect HumanActionRecognition.py
```

*   Run bag file
    *	The bag files are currently under kinect_data folder.
    *	Run one of the bag files from this folder or any similar bag file which contains human acction joint information.
    *	The frames containing joint information that can be sent to tensorflow are displayed on terminal
    
```
rosbag play <bag_file_name>
```




