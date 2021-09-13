#importing required libraries
import os

files = {
    'CUSTOM_MODEL_NAME' : 'ship_mobnet', 
    'PRETRAINED_MODEL_NAME' : 'ssd_mobilenet_v2_fpnlite_320x320_coco17_tpu-8',
    'PRETRAINED_MODEL_URL' : 'http://download.tensorflow.org/models/object_detection/tf2/20200711/ssd_mobilenet_v2_fpnlite_320x320_coco17_tpu-8.tar.gz',
    'TF_RECORD_SCRIPT_NAME' : 'generate_tfrecord.py',
    'LABEL_MAP_NAME' : 'label_map.pbtxt',
}

paths = {
    'MAIN_PATH': os.path.join('Tensorflow'),
    'WORKSPACE_PATH': os.path.join('Tensorflow', 'workspace'),
    'SCRIPTS_PATH': os.path.join('Tensorflow','scripts'),
    'APIMODEL_PATH': os.path.join('Tensorflow','models'),
    'ANNOTATION_PATH': os.path.join('Tensorflow', 'workspace','annotations'),
    'IMAGE_PATH': os.path.join('Tensorflow', 'workspace','images'),
    'MODEL_PATH': os.path.join('Tensorflow', 'workspace','models'),
    'PRETRAINED_MODEL_PATH': os.path.join('Tensorflow', 'workspace','pre-trained-models'),
    'CHECKPOINT_PATH': os.path.join('Tensorflow', 'workspace','models',files['CUSTOM_MODEL_NAME']), 
    'OUTPUT_PATH': os.path.join('Tensorflow', 'workspace','models',files['CUSTOM_MODEL_NAME'], 'export'), 
    'TFJS_PATH':os.path.join('Tensorflow', 'workspace','models',files['CUSTOM_MODEL_NAME'], 'tfjsexport'), 
    'TFLITE_PATH':os.path.join('Tensorflow', 'workspace','models',files['CUSTOM_MODEL_NAME'], 'tfliteexport'), 
    'PROTOC_PATH':os.path.join('Tensorflow','protoc')
 }

scripts = {
    'PIPELINE_CONFIG':os.path.join('Tensorflow', 'workspace','models', files['CUSTOM_MODEL_NAME'], 'pipeline.config'),
    'TF_RECORD_SCRIPT': os.path.join(paths['SCRIPTS_PATH'], files['TF_RECORD_SCRIPT_NAME']), 
    'LABELMAP': os.path.join(paths['ANNOTATION_PATH'], files['LABEL_MAP_NAME'])
}

for path in paths.values():
    if not os.path.exists(path):
        if os.name == 'posix':
            os.mkdir(path)
        if os.name == 'nt':
            os.mkdir(path)
