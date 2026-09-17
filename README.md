# Computer Vision

This repository contains a simple introductory Computer Vision task using Python and OpenCV.

## Repository Structure

```text
Computer Vision/
├── Files/
│   └── images.py
├── Images/
│   ├── image1.jpg
│   └── image2.jpg
└── README.md
```

## What does `images.py` do?

The `images.py` script uses the OpenCV (`cv2`) Python library to load an image from the `Images` folder. It checks whether the image was loaded successfully, prints the image dimensions, and displays the image in a window.

## Images Folder

The `Images` folder contains two sample images used for the computer vision task. They are ordinary visual images included to demonstrate how OpenCV can read and display image files.

## Requirements

Install OpenCV with:

```bash
pip install opencv-python
```

Then run:

```bash
python Files/images.py
```
