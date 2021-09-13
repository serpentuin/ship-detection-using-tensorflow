import os
from create_folders import files, paths, scripts

TRAINING_SCRIPT = os.path.join(paths['APIMODEL_PATH'], 'research', 'object_detection', 'model_main_tf2.py')

command = "python {} --model_dir={} --pipeline_config_path={} --num_train_steps=3000".format(
    TRAINING_SCRIPT, paths['CHECKPOINT_PATH'],scripts['PIPELINE_CONFIG'])

print(command)