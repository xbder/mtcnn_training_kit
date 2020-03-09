import cv2
from mtcnn.core.detect import create_mtcnn_net, MtcnnDetector
from mtcnn.core.vision import vis_face

'''
    评估模型的准确率
    使用数据集：WIDER_val
'''

if __name__ == '__main__':
    pnet, rnet, onet = create_mtcnn_net(p_model_path="./original_model/pnet_epoch.pt",
                                        r_model_path="./original_model/rnet_epoch.pt",
                                        o_model_path="./original_model/onet_epoch.pt",
                                        use_cuda=True)
    mtcnn_detector = MtcnnDetector(pnet=pnet, rnet=rnet, onet=onet, min_face_size=24)

    anno_val = "./anno_store/anno_val.txt"
    img_path = "./data_set/face_detection/WIDER_val/WIDER_val/"
    evaluate_result = "./results/evaluate_result.txt"
    f_eval = open(evaluate_result, 'w+', encoding="utf-8")

    img_nums = 0    # 图片数量
    correct = 0    # 正确数量（图片层面：全部人脸均检测出才算该图片识别正确）

    with open(anno_val, 'r') as fo:
        for line in fo.readlines():
            line = line.strip()
            arr = line.split(" ")
            img_nums += 1
            filename = arr[0]
            person_nums = (len(arr) - 1)/4.0

            img = cv2.imread(filename)
            bboxs, landmarks = mtcnn_detector.detect_face(img)  # 人脸框bboxs，五官点landmarks
            reco_nums = len(bboxs)    # 识别到的人数

            if int(person_nums) == reco_nums:
                correct += 1
                f_eval.write(filename + " " + str(int(person_nums)) + str(correct) + "\n")

    f_eval.close()
    print("eval finished! Accuracy:", reco_nums/person_nums)
    # img = cv2.imread("./l_z.png")
    # img_bg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # # b, g, r = cv2.split(img)
    # # img2 = cv2.merge([r, g, b])
    #
    # bboxs, landmarks = mtcnn_detector.detect_face(img)    # 人脸框bboxs，五官点landmarks
    # # print(len(bboxs))
    # # # print box_align
    # # save_name = 'r_4.jpg'
    # # vis_face(img_bg, bboxs, landmarks, save_name)