import os
import wget
import shutil
from zipfile import ZipFile
from create_folders import files, paths, scripts

wget.download(files['PRETRAINED_MODEL_URL'])
shutil.move((files['PRETRAINED_MODEL_NAME']+'.tar.gz'), (paths['PRETRAINED_MODEL_PATH']))
os.chdir(paths['PRETRAINED_MODEL_PATH']) 
with ZipFile(files['PRETRAINED_MODEL_NAME']+'.tar.gz', 'r') as zipObj:
    zipObj.extractall()