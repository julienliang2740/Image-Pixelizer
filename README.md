# Image-Pixelizer
(Inspired by my need for a tool to create map art and make Chinese characters in Minecraft)

A small script that takes an image and gives a pixelated as well as thresholded image.

Image specification and parameters are adjusted in input.json:
```
{
    "imagetype" : "png",
    "desired_n" : 25,
    "enlargement_factor" : 10,
    "threshold_value" : 150
}
```

Usage:
Drag images into the "source" folder
```
python process.py
```
