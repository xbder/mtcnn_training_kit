import os
import sys
sys.path.append(os.getcwd())
from wider_loader import WIDER
import cv2
import time

"""
 modify .mat to .txt 
"""

base_path = 'C:/workspace/mtcnn-pytorch/'

#wider face original images path
path_to_image = os.path.join(base_path, './data_set/face_detection/WIDERFACE/WIDER_train/WIDER_train/images')

#matlab file path
file_to_label = os.path.join(base_path, './data_set/face_detection/WIDERFACE/wider_face_split/wider_face_split/wider_face_train.mat')

#target file path
target_file = os.path.join(base_path, './anno_store/anno_train.txt')

wider = WIDER(file_to_label, path_to_image)

line_count = 0
box_count = 0

print('start transforming....')
t = time.time()

with open(target_file, 'w+') as f:
    # press ctrl-C to stop the process
    for data in wider.next():
        line = []
        line.append(str(data.image_name))
        line_count += 1
        for i,box in enumerate(data.bboxes):
            box_count += 1
            barr = []
            for j, bvalue in enumerate(box):
                barr.append(bvalue)
            newbox = (barr[0], barr[1], int(barr[0]) + int(barr[2]), int(barr[1]) + int(barr[3]))
            for j,bvalue in enumerate(newbox):
                line.append(str(bvalue))

        line.append('\n')

        line_str = ' '.join(line)
        f.write(line_str)

st = time.time()-t
print('end transforming')

print('spend time:%d'%st)
print('total line(images):%d'%line_count)
print('total boxes(faces):%d'%box_count)
