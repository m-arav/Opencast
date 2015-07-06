# OPENCAST
A screen casting and recording software for Linux


The Opencast program is an attempt at making a screen casting program for linux destops . Using this program you can multicast your workscreen to devices on the same network

# DEPENDENCIES

X11
Gstreamer 0.10 && Gstreamer C Libraries ( INCLUDING RTSP LIBRARIES)
v4l2loopback driver (by default it tries device video1)
Qt 4 (pyqt4)

# BUILD

Only the c programs need to be compiled

cd src/

gcc gst_C.c -o Stream `pkg-config --cflags --libs gstreamer-0.10`
gcc str_rec.c -o record `pkg-config --cflags --libs gstreamer-0.10`
gcc rtsp.c -o rtsp `pkg-config --cflags --libs gstreamer-0.10 gst-rtsp-server-0.10`

# RUN

Note: v4l2loopback module has to be inserted into the kernel beforehand

python Open_Cast.py 
