import os
from git import Repo
from create_folders import paths

if not os.path.exists(os.path.join(paths['APIMODEL_PATH'], 'research', 'object_detection')):
    Repo.clone_from('https://github.com/tensorflow/models', paths['APIMODEL_PATH'])