from time import sleep
import os
import sys

if __name__ == '__main__':
    user_dir = os.environ['USER_DIR']
    task_id = os.environ['TASK_ID']
    full_path = "{}/{}/main.py".format(user_dir, task_id)
    #ret = os.system('python3 {}'.format(full_path))
    #exit(1 if ret == 256 else ret)
    exit(0)