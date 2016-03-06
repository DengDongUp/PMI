#coding=utf-8
__author__ = 'root'
from PMI import *
import os
from extract import extract

if __name__ == '__main__':
    path = '/home/quincy1994/文档/微脉圈/训练集/体育'
    files = os.listdir(path)
    documents = []
    # for filename in files:
    #     f = open(path+'/'+filename, 'r')
    #     data = f.readlines()
    #     extractwords = []
    testfile = '/home/quincy1994/桌面/data.txt'
    f = open(testfile, 'r')
    data = f.readlines()
    if data is not None:
        for sentences in data:
            extractwords = []
            words = extract(sentences)
            for word in words:
                extractwords.append(word)
            documents.append(set(extractwords))
    pm = PMI(documents)
    pmi = pm.get_pmi()
    for p in pmi:
        if pmi[p] > 1.5:
            print p, pmi[p], '\n'