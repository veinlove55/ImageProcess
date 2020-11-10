import os
import csv

def readCSV(filePath):
    fileList = []
    with open(filePath, "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            fileList.append(row[0])
    return fileList

if __name__ == "__main__":
    list = readCSV(r'/home/user_2/workspace/my_test_ord.csv')
    for file in list:
        fpath = '/home/user_2/new_data/test_data/'+file
        if  not os.path.isfile(fpath):
            print(file + ' not exist')
