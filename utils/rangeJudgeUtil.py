
import os

'''
    范围判断工具
'''

'''
    pt角是否在poly多边形内
    :return 在多边形内，True；否则，False
'''
def isInsidePolygon(pt, poly):
    c = False
    i = -1
    l = len(poly)
    j = l - 1
    while i < l - 1:
        i += 1
        # print(i, poly[i], j, poly[j])
        if ((poly[i]["x"] <= pt["x"] and pt["x"] < poly[j]["x"]) or (
                poly[j]["x"] <= pt["x"] and pt["x"] < poly[i]["x"])):
            if (pt["y"] < (poly[j]["y"] - poly[i]["y"]) * (pt["x"] - poly[i]["x"]) / (
                    poly[j]["x"] - poly[i]["x"]) + poly[i]["y"]):
                c = not c
        j = i
    return c

'''
    判断在不在车厢里（避免把门外和窗外的人识别到）
    判断标准：四角有点在车厢里，就认为在车厢里
    :param pointList 框人的四点坐标
    :param polyList 车厢各点坐标
    :return True，在车厢里；False，不在车厢里
'''
def in_carriage(pointList, polyList):
    for pt in pointList:
        flag = isInsidePolygon(pt, polyList)    # 在范围内，返回True
        if flag is True:    # 只要有一个点在车厢里，就认为在车厢里
            return True
    # print("不在范围内的原因：", pointList)
    return False

if __name__ == '__main__':
    poly = [{'x': 1, 'y': 1}, {'x': 1, 'y': 4}, {'x': 3, 'y': 7}, {'x': 4, 'y': 4}, {'x': 4, 'y': 1}]
    print(isInsidePolygon({'x': 2, 'y': 2}, poly))