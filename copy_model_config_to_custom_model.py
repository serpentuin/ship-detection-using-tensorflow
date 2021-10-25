import os
import shutil
from create_folders import files, paths, scripts

src = os.path.join(paths['PRETRAINED_MODEL_PATH'], files['PRETRAINED_MODEL_NAME'], 'pipeline.config')
dst = os.path.join(paths['CHECKPOINT_PATH'])
shutil.copyfile(src=src, dst=dst)
