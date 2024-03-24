import os
import shutil
from random import randint

def generate_random_hash():
    return str(randint(1000000000, 9999999999))
    
class UserFolderManager:
    def __init__(self, code_folder):
        self.code_folder = code_folder
        self.user_code_hash = self.generate_retryable_hash()

    def __enter__(self):
        if self.user_code_hash is None:
            raise Exception

        os.mkdir("{}/{}".format(self.code_folder, self.user_code_hash))
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        shutil.rmtree("{}/{}".format(self.code_folder, self.user_code_hash))

    def create_file(self, filename):
        return open("{}/{}/{}".format(self.code_folder, self.user_code_hash, filename), 'w')

    def generate_retryable_hash(self, max_retries=10):
        user_code_hash = generate_random_hash()
        attempt = 0
        while user_code_hash in os.listdir(self.code_folder) and attempt < max_retries:
            attempt += 1
            user_code_hash = generate_random_hash()
        if not attempt < max_retries:
            return None
        else:
            return user_code_hash
    
