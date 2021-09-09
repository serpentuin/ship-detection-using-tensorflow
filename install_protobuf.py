#importing required libraries
import os
import wget
import shutil
from git import Repo
from zipfile import ZipFile
from create_folders import files, paths, scripts

# Install Tensorflow Object Detection 
if os.name=='posix':  
    url="https://github.com/protocolbuffers/protobuf/releases/download/v3.17.3/protoc-3.17.3-linux-x86_64.zip"
    wget.download(url)
    shutil.move('protoc-3.17.3-linux-x86_64.zip', paths['PROTOC_PATH'])
    os.chdir(paths['PROTOC_PATH'])
    with ZipFile('protoc-3.17.3-linux-x86_64.zip', 'r') as zipObj:
        zipObj.extractall()
    os.environ[b'PATH'] += os.pathsep + os.path.abspath(os.path.join('bin'))
if os.name=='nt':
    url="https://github.com/protocolbuffers/protobuf/releases/download/v3.17.3/protoc-3.17.3-win64.zip"
    wget.download(url)
    shutil.move('protoc-3.17.3-win64.zip', paths['PROTOC_PATH'])
    os.chdir(paths['PROTOC_PATH'])
    with ZipFile('protoc-3.17.3-win64.zip', 'r') as zipObj:
        zipObj.extractall()
    os.environ['PATH'] += os.pathsep + os.path.abspath(os.path.join('bin'))