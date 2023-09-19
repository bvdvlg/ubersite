from time import sleep
import os
import sys

task_name = os.environ['TASK_NAME']
task_dir = os.environ['TASK_DIR']

sys.path.append('{}/{}'.format(task_dir, task_name))

if __name__ == '__main__':
    task_name = os.environ['TASK_NAME']
    task_dir = os.environ['TASK_DIR']
    full_path = "{}/{}/main.py".format(task_dir, task_name)
    res = os.system('python3 {}'.format(full_path))