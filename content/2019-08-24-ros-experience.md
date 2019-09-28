Title: ROS experience
Author: SergeM
Date: 2019-08-24 20:32:00
Slug: ros-experience
Tags: ros, linux, robotics, raspberry, pi


Here will be some notes on ROS.


## ROS on raspberry pi
There is a compiled image by ubiquity that contain ROS kinetic.

[https://downloads.ubiquityrobotics.com/pi.html](https://downloads.ubiquityrobotics.com/pi.html).

It seems for me too old. It's 2019, there are ubuntu 18, ros melodic and ros2, next year the support of python2.7 will be discontinued. Meh... 


## Installing tensorflow for ROS on raspberry pi
Alternatively one can try to install it from wheels:
https://www.tensorflow.org/install/pip?lang=python3#package-location

The dependencies are better to install using pip and piwheels.org:
```
sudo pip3 install --extra-index-url=https://www.piwheels.org/simple -U tensorflow keras
```

### Issues
#### h5py
I encountered an error about h5py: 
```
ImportError: libhdf5_serial.so.100: cannot open shared object file: No such file or directory
```
installing 
```
sudo apt-get install libhdf5-dev
sudo apt-get install libhdf5-serial-dev
```
didnt help.

Some version mismatch

I could resolve it by compiling h5py with my version:
```
HDF5_VERSION=1.8.16 sudo pip3 install --no-binary=h5py h5py
```

#### load_img

`keras_preprocessing.image.utils.load_img` results in the error:
```
  File "/home/ubuntu/sergem_robocar/py3/lib/python3.5/site-packages/keras_preprocessing/image/utils.py", line 108, in load_img
    raise ImportError('Could not import PIL.Image. '
ImportError: Could not import PIL.Image. The use of `load_img` requires PIL.
```

pillow is installed. 

The error may be caused by missing jpeg libraries. Try to load PIL in a separate python and check if it works.
I got the following error.
```python
>>> from PIL import Image as pil_image
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/ubuntu/sergem_robocar/py3/lib/python3.5/site-packages/PIL/Image.py", line 95, in <module>
    from . import _imaging as core
ImportError: libjpeg.so.62: cannot open shared object file: No such file or directory
```

Easily solvable by 
```
sudo apt install libjpeg62
```


# Name clash in dynamic_reconfigure
Probably it is written somewhere but I haven't read the docs...

I am developign a node for robot steering translation. I got an error:
```
$ rosrun steering_translator steering_translator.py 
Traceback (most recent call last):
  File "/home/user/omicron_robocar/catkin_ws/src/steering_translator/src/steering_translator.py", line 5, in <module>
    import steering_translator.cfg
  File "/home/user/omicron_robocar/catkin_ws/src/steering_translator/src/steering_translator.py", line 5, in <module>
    import steering_translator.cfg
ImportError: No module named cfg
```

I did everything according to the tutorials [How to Write Your First .cfg File](http://wiki.ros.org/dynamic_reconfigure/Tutorials/HowToWriteYourFirstCfgFile)
and [Setting up Dynamic Reconfigure for a Node (python)](http://wiki.ros.org/dynamic_reconfigure/Tutorials/SettingUpDynamicReconfigureForANode%28python%29), just changed couple of names.
The problem was in the naming of the package (steering_translator) and the executable file (steering_translator.py). They are getting mixed up on the execution. The solution was to rename python file to steering_translator_node.py.


