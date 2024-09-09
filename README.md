# HEVC-Encoding on Jetson Tx2

# option 1: run through python code:

## Installation guide:

1. Make sure you already install CUDA through JetPack. You need to remove the default OpenCV 3.3 on Jetson TX2, as it is a lower version and is not linked to CUDA and gstreamer.

    run the cmd below to remove OpenCV

    **sudo apt-get purge libopencv***

2. Run **./install_opencv_3.4.sh** to build OpenCV 3.4 from source, which links CUDA and gstreamer. The entire process takes very long time. You need to assign a temp folder for OpenCV source code. After install, run the following code to verify:

        $ ls /usr/local/lib/python3.5/dist-packages/cv2.*
        /usr/local/lib/python3.5/dist-packages/cv2.cpython-35m-aarch64-linux-gnu.so
        
        $ ls /usr/local/lib/python2.7/dist-packages/cv2.*
        /use/local/lib/python2.7/dist-packages/cv2.so
        
        $ python3 -c 'import cv2; print(cv2.__version__)'
        3.4.0
        $ python2 -c 'import cv2; print(cv2.__version__)'
        3.4.0
    Make sure OpenCV is target to **/usr/local/lib** path, if you install ROS, it may change the path to **/opt/ros/kinectic/**,which is a wrong path. Then you need to comment it out in **~/.bash.rc** file 

# option 2: run through gstreamer cmd directly

1. install all gstreamer dependencies as the pdf guideline.

2. run the cmd below:

        gst-launch-1.0 filesrc location=0548207774487603-1564435253804-20190729-down-212524.mkv ! matroskademux ! h264parse ! omxh264dec ! videoconvert ! omxh265enc ! mpegtsmux ! filesink location=output.h265