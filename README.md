# mtcnn_training_kit

​	mtcnn模型训练，参考自https://github.com/Sierkinhane/mtcnn-pytorch.git，已改完bug。



## bug Details：

### 1、mtcnn/data_preprocess/*.py中import错误

``` python
import cv2
import numpy as np
sys.path.append(os.getcwd())    # 原文，但os.getcwd()得到的是当前目录，而不是项目根目录

# 修改为：
base_path = "C:/workspace/path/to/project"
sys.path.append(base_path)

from mtcnn.core.detect import MtcnnDetector,create_mtcnn_net
from mtcnn.core.imagedb import ImageDB
from mtcnn.core.image_reader import TestImageLoader
```

## 2、anno_store/tool/format/transform.py文件

原有：写入anno_store/anno_train.txt文件时为：x_left y_top w h

改为：写入内容为：x_left y_top x_right y_bottom

``` python
with open(target_file, 'w+') as f:
    # press ctrl-C to stop the process
    for data in wider.next():
        line = []
        line.append(str(data.image_name))
        line_count += 1
        for i,box in enumerate(data.bboxes):
            # # 写入文件：x_left y_top w h
            # box_count += 1
            # for j,bvalue in enumerate(box):
            #     print(bvalue)
            #     line.append(str(bvalue))

            # 写入文件：x_left y_top x_right y_bottom
            box_count += 1
            barr = []
            for j, bvalue in enumerate(box):
                barr.append(bvalue)
            newbox = (barr[0], barr[1], int(barr[0]) + int(barr[2]), int(barr[1]) + int(barr[3]))
            for j, bvalue in enumerate(newbox):
                line.append(str(bvalue))

        line.append('\n')

        line_str = ' '.join(line)
        f.write(line_str)
```

## 3、某些图片文件标注错误

​	存在图片文件标注错误（坐标为负数）

目前已发现有问题图片：54--Rescue\54_Rescue_rescuepeople_54_29.jpg

解决办法：anno_store/anno_train.txt文件中删除该图片的标注，并从图片库中删除该图片。





======================================================
原README.md请见ORIGIN-README.md
======================================================