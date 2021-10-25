import os
import shutil
from create_folders import files, paths, scripts

src = os.path.join(paths['PRETRAINED_MODEL_PATH'], files['PRETRAINED_MODEL_NAME'], scripts['PIPELINE_CONFIG'])
dst = os.path.join(paths['CHECKPOINT_PATH'])
shutil.copyfile(src=src, dst=dst)
