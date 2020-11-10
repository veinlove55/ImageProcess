# Check The Data validity
import os
import csv

def checkMeasExist(baseDir, nameList, variant):
    cntChecked = 0
    cntWaste = 0
    cntNotExist = 0
    for iter in range(len(nameList)):
        # check if it is header name
        if nameList[iter] == 'path':
            cntWaste = cntWaste + 1
            continue
        elif (nameList[iter] is '') or (nameList[iter] is ' ') :
            cntWaste = cntWaste + 1
            continue
        else:
            splitName =  nameList[iter].split('_rgb') #segment from folder
            folderName = splitName[0]
            # check if the folder exist
            if os.path.exists(os.path.join(baseDir, variant, folderName, nameList[iter])):
                cntChecked = cntChecked + 1
                # print('cheked percentage: ' +  str(cntChecked / (len(nameList) - cntWaste)))
            else:
                cntNotExist = cntNotExist + 1
                print('fucked up! No file exist')
                print('-----------')
                print(str(cntNotExist))
                print(nameList[iter])
    print('-----------')
    print(variant)
    print('-----------')
    print('total files ' + str(len(nameList) - cntWaste))
    print('-----------')
    print('total checked files ' + str(cntChecked))
    print('-----------')
    print('totala failed checked files' + str(cntNotExist))
    


def readIn(filePath):
    result = {}
    nameList = []
    labelList = []
    with open(filePath, "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        for lines in csv_reader:
            nameList.append(lines[0])
    result["nameList"] = nameList
    return result


def main():
    global base_dir
    base_dir = '/home/deeplearning/data_disk_2/hackathon_data'                  # os.getcwd()
    # train file check
    csvPath = os.path.join(base_dir, 'train.csv')
    readCsvIn = readIn(csvPath)
    checkMeasExist(base_dir, readCsvIn['nameList'], 'train_data')

    # test file check
    csvPath = os.path.join(base_dir, 'test.csv')
    readCsvIn = readIn(csvPath)
    checkMeasExist(base_dir, readCsvIn['nameList'], 'test_data')  
    
    print('check done')

main()