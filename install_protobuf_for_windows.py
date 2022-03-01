#importing required libraries
import os
import wget
import shutil
from zipfile import ZipFile
from create_folders import files, paths, scripts

# Install Tensorflow Object Detection 
if os.name=='nt':
    url="https://github.com/protocolbuffers/protobuf/releases/download/v3.19.4/protoc-3.19.4-win64.zip"
    wget.download(url)
    shutil.move('protoc-3.19.4-win64.zip', paths['PROTOC_PATH'])
    os.chdir(paths['PROTOC_PATH'])
    with ZipFile('protoc-3.19.4-win64.zip', 'r') as zipObj:
        zipObj.extractall()
