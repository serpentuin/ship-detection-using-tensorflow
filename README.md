# ship-detection-using-tensorflow
Object detection project implemented using Tensorflow Object Detection API that aimed to detect and recognize the types of ship.

# Environment Setups (Tested)

| Requirement | Version/Description |
| ---------- | ---------- |
| Operating System | Windows 10 |
| IDE (Compiler) | Microsoft Visual Studio 2019 (MSVC 2019) |
| CUDA-enabled GPU | NVIDIA GeForce GTX 1060 |
| NVIDIA® GPU drivers | Version 471.96 (as of September 8th, 2021)
| CUDA® Toolkit | CUDA® 11.2.0 (Dec 2020)
| cuDNN SDK | 8.1.0 (January 26th, 2021) for CUDA 11.0, 11.1 and 11.2
| Python | 3.9.7 (as of September 8th, 2021)
| Tensorflow **(install in step 4)** | 2.6.0 (as of September 8th, 2021)
| Tensorflow-gpu **(install in step 4)** | 2.6.0 (as of September 8th, 2021)

# Steps

## Step 1
Open up the terminal and clone this repository into your machine.

`git clone https://github.com/serpentuin/ship-detection-using-tensorflow.git`

## Step 2
Create Python virtual environment and activate it using terminal.

`cd ship-detection-using-tensorflow`

`python -m venv env`

`.\env\Scripts\activate`
for Windows

`source env/bin/activate`
for Unix/Ubuntu

## Step 3
Update pip version to the latest

`python -m pip install upgrade pip`

## Step 4

Install the required libraries

`pip install -r requirements.txt`

## Step 5 (Work in progress)
Install annotation tool by running the `labelimg_installation.py` script

