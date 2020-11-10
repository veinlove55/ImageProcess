import os
import csv
import cv2

def readCSV(filePath):
    csv_dict = {}
    nameList = []
    labelList = []
    with open(filePath, "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            csv_dict[row[0]] = row[1]
    return csv_dict

'''
img = cv2.imread('BK63XRG_20140529_101248/BK63XRG_20140529_101248_rgb_f001870.png')  #读取第一张图片
imgInfo = img.shape
size = (imgInfo[1],imgInfo[0])  #获取图片宽高度信息
print(size)
'''
def createMP4(imageFolderPath, labelFilepath):
    folderName = os.path.basename(os.path.normpath(imageFolderPath))
    fps = 30
    size = (1280, 720)
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    videoWrite = cv2.VideoWriter(folderName+'.mp4', fourcc, fps, size)  # 根据图片的大小，创建写入对象 （文件名，支持的编码器，5帧，视频大小（图片大小））
    files = os.listdir(imageFolderPath)
    files.sort()
    print('***************'+imageFolderPath +'*****************')
    index = 0
    csv_dict = readCSV(labelFilepath)
    for file in files:
        if file.split('.')[0] in csv_dict.keys():
            if csv_dict[file.split('.')[0]] == '1':
                name = str(file) + ' ' + r'is HIGHWAY'
            else:
                name = str(file) + ' ' + r'HIGHWAY: ' + csv_dict[file.split('.')[0]]
        else:
            name = 'NOT FOUND IN DATA SET'

        green = (0, 255, 0)
        red = (0, 0, 255)

        fileName = imageFolderPath + '/' + file  # 循环读取所有的图片,假设以数字顺序命名
        img = cv2.imread(fileName)
        font = cv2.FONT_HERSHEY_SIMPLEX  # 使用默认字体
        #img = cv2.putText(img, str(name), (0, 40), font, 1.0, (0, 255, 0), 2)  # #添加文字，1.2表示字体大小，（0,40）是初始的位置，(255,255,255)表示颜色，2表示粗细
        print('##########'+file)
        #print('##########' + csv_dict[file.split('.')[0]])
        if float(csv_dict[file]) >= 0.5:
            img = cv2.putText(img, str(file), (0, 40), font, 1.0, (0, 255, 0), 2)
            img = cv2.putText(img, str('HIGHWAY: '+csv_dict[file]), (0, 80), font, 1.0, red, 2)
            img = cv2.putText(img, str('CITY: ' + str( 1- float(csv_dict[file]) ) ), (0, 120), font, 1.0, green, 2)
        else:
            img = cv2.putText(img, str(file), (0, 40), font, 1.0, (0, 255, 0), 2)
            img = cv2.putText(img, str('HIGHWAY: ' + csv_dict[file]), (0, 80), font, 1.0, green, 2)
            img = cv2.putText(img, str('CITY: ' + str(1 - float(csv_dict[file]))), (0, 120), font, 1.0, red, 2)
        index = index + 1
        videoWrite.write(img)  # 将图片写入所创建的视频对象

if __name__ == "__main__":
    createMP4(r'/home/user_2/new_data/test_data/LB-XL_1656_20140221_104928', r'/home/user_2/workspace/result/inference.csv')

