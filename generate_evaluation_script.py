from create_folders import files, paths, scripts
from generate_training_script import TRAINING_SCRIPT

command = "python {} --model_dir={} --pipeline_config_path={} --checkpoint_dir={}".format(
    TRAINING_SCRIPT, paths['CHECKPOINT_PATH'],scripts['PIPELINE_CONFIG'], paths['CHECKPOINT_PATH'])

print(command)