#! python3
# caption.py

import json
import simplejson
import os
from pprint import pprint

path = os.getcwd() + "/json" 
os.chdir(path)
print(path)
data = json.load(open('daquan.json'))
captions = []
for i in range(len(data)):
    try:
        caption = data[i]['edge_media_to_caption']['edges'][0]['node']['text']
        captions.append(caption)
    except Exception:
        print("Whoops.")


for filename in os.listdir(path): #os.getcwd()):
    print(filename)
    os.chdir(path)
    try:
        data = json.load(open(filename,errors = 'ignore'))
    except Exception:
        print('Moving on.')
    for i in range(len(data)):
        print(filename)
        if filename.endswith('.json'):
            try:
                caption = data[i]['edge_media_to_caption']['edges'][0]['node']['text']
                captions.append(caption)
            except Exception:
                print("Moving on.")

print(captions)

with open('../captions.txt', 'w') as file_handler:
    for item in captions:
        file_handler.write("{}\n".format(item))
