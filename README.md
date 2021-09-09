# A.  Environment Setup (Testing in progress)

| Requirement | Version/Description |
| ---------- | ---------- |
| Operating System | Windows 10 |
| IDE (Compiler) | Microsoft Visual Studio 2019 (MSVC 2019) |
| CUDA-enabled GPU | NVIDIA GeForce GTX 1060 |
| NVIDIA® GPU drivers | Version 471.96 (as of September 8th, 2021) |
| CUDA® Toolkit | CUDA® 11.2.0 (Dec 2020) |
| cuDNN SDK | 8.1.0 (January 26th, 2021) for CUDA 11.0, 11.1 and 11.2 |
| Python | 3.9.7 (as of September 8th, 2021) |
| Tensorflow **(install in step 4)** | 2.6.0 (as of September 8th, 2021) |
| Tensorflow-gpu **(install in step 4)** | 2.6.0 (as of September 8th, 2021) |
| Protocol Buffers | [3.17.3](https://github.com/protocolbuffers/protobuf/releases/tag/v3.17.3) (Jun 2021) |

# B.  Steps

## Step 1 : Clone this repository into your machine using terminal.

`git clone https://github.com/serpentuin/ship-detection-using-tensorflow.git`

## Step 2 : Create Python virtual environment and activate it using terminal.

`cd ship-detection-using-tensorflow`

`python -m venv env`

`source env/bin/activate`
for **Unix/Ubuntu**

`.\env\Scripts\activate`
for **Windows**

## Step 3 : Update pip version to the latest.

`python -m pip install upgrade pip`

## Step 4 : Install the required libraries.

`pip install -r requirements.txt`

## Step 5 : Install annotation tool (labelImg).

### Unix/Ubuntu

`git clone https://github.com/tzutalin/labelImg.git`

`make qt5py3`

`cd labelImg`

`python labelImg.py`


### Windows

`git clone https://github.com/tzutalin/labelImg.git`

`cd labelImg`

`pyrcc5 -o libs/resources.py resources.qrc`

`python labelImg.py`

## Step 6 : Create folders using `create_folder.py` script.

```
CUSTOM_MODEL_NAME = 'ship_centernet' 
PRETRAINED_MODEL_NAME = 'centernet_hg104_512x512_coco17_tpu-8'
PRETRAINED_MODEL_URL = 'http://download.tensorflow.org/models/object_detection/tf2/20200713/centernet_hg104_512x512_coco17_tpu-8.tar.gz'
TF_RECORD_SCRIPT_NAME = 'generate_tfrecord.py'
LABEL_MAP_NAME = 'label_map.pbtxt'
```

Above codes are the snippets from a part of codes in `create_folder.py`script. Please select a pre-trained model from [Tensorflow 2 Models Zoo](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md) and be sure to change the following variables accordingly:

```
CUSTOM_MODEL_NAME = 
PRETRAINED_MODEL_NAME = 
PRETRAINED_MODEL_URL = 
```

Open the terminal, and run following command to create the necessary folders:

`python create_folder.py`

## Step 7 : Install Tensorflow Object Detection API.

Work in progress. Will be updated soon :) .

# C.  Pretrained Detection Model Used

The selected model is a detection model that is pre-trained on the [COCO 2017](https://cocodataset.org/#home) dataset.

| Item | Details |
| ---- | -------------------------------|
| Name | [CenterNet HourGlass104 512x512](http://download.tensorflow.org/models/object_detection/tf2/20200713/centernet_hg104_512x512_coco17_tpu-8.tar.gz) |
| Speed | 70 ms |
| COCO mAP | 41.9 |
| Outputs | Boxes |
