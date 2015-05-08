import math, json

def retreive(dic, *args):
    for j in args:
        f = open(j + '.csv', 'r')
        header = f.readline().split(',')
        header_length = len(header)
        header_range = range(header_length)
        dic[j] = [[] for k in header_range]

        line = f.readline()[:-1]
        while line:
            line = line.split(',')
            for i in header_range:
                dic[j][i].append(line[i])
            line = f.readline()[:-1]

        f.close()
    del header, header_length, header_range, j, f, line

def retreive_list(dic, field):
    f = open(field + '.csv', 'r')
    header = f.readline().split(',')
    header_length = len(header)
    header_range = range(header_length)
    dic[field] = [[] for k in header_range]

    line = f.readline()[:-1]
    while line:
        line = line.split(',')
        for i in header_range:
            dic[field][i].append(line[i])
        line = f.readline()[:-1]

    f.close()
    del header, header_length, header_range, f, line, i

def retreive_dic(dic, field):
    f = open(field + '.csv', 'r')
    header = f.readline().split(',')
    header_length = len(header)
    header_range = range(header_length)
    # dic[field] = {}

    line = f.readline()[:-1]
    while line:
        line = line.split(',')
        dic[field][int(line[0]) - 1] = float(line[1])
        line = f.readline()

    f.close()
    del header, header_length, header_range, f, line


if __name__ == '__main__':
    dic = {'train': '', 'sample_predictions': {}, 'test': ''}
    #retreive(dic, *dic)
    retreive_list(dic, 'train')
    retreive_list(dic, 'test')
    retreive_dic(dic, 'sample_predictions')

    
