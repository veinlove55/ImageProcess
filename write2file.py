


def write2file(imageName, value):
    file = open(r'saved.txt', 'a')
    file.write(imageName + ',' + value + '\n')
    file.close()

if __name__ == '__main__':
    write2file('1', '1')
    write2file('2', '2')
    write2file('3', '3')
    write2file('4', '4')
    write2file('5', '5')
    write2file('6', '6')