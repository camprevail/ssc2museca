import hashlib
import os
import time
import sys
import json
import re

def hash_file(filename):
    """"This function returns the SHA-1 hash
   of the file passed into it"""

    # make a hash object
    h = hashlib.sha1()

    # open file for reading in binary mode
    with open(filename, 'rb') as file:
        # loop till the end of the file
        chunk = 0
        while chunk != b'':
            # read only 1024 bytes at a time
            chunk = file.read(1024)
            h.update(chunk)

    # return the hex representation of digest
    return h.hexdigest()

def generate_hash(path):
    a = round(time.perf_counter(), 3)
    filelist = []
    cache = {}
    for root, dirs, files in os.walk(path):
        for name in files:
            filelist.append('/'.join(re.split('/|\\\\', root) + [name]))

    for file in filelist:
        cache[file] = (hash_file(file))
    b = round(time.perf_counter(), 3)
    # print('cache generated in {} seconds'.format(str(round(b-a, 3))))
    with open(f'{path}-cache.json', 'w') as f:
        json.dump(cache, f, indent=2)
    return

if __name__ == "__main__":
    generate_hash(sys.argv[1])

