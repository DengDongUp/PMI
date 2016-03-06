#coding=utf-8
import jieba
import jieba.analyse
import jieba.posseg as pseg
import re

class Extractkeys:
    def GetStopWords(self):
        stopWordFile = open('/home/quincy1994/文档/微脉圈/tags/停用词表','r')
        stopWords=[]
        lines = stopWordFile.readlines()
        for word in lines:
            stopWords.append(word.decode('utf-8'))
        return stopWords

    def CutSimpleWord(self,wordlist):
        newwordlist = []
        for word in wordlist:
            if word.__len__() >= 2:
                newwordlist.append(word)
        return newwordlist

    def removeEmoji(self, sentence):
        return re.sub('\[.*?\]', '', sentence)

    def CutWithPartOfSpeech(self, sentence):
        sentence = self.removeEmoji(sentence)
        words =jieba.cut(sentence)
        wordlist=[]
        for word in words:
            wordlist.append(word)
        return wordlist

    def ExtractWord(self,wordlist):
        sentence = ','.join(wordlist)
        words = jieba.analyse.extract_tags(sentence,5)
        wordlist = []
        for w in words:
            wordlist.append(w)
        return wordlist

    def RemoveStopWord(self,wordlist):
        stopWords = self.GetStopWords()
        keywords = []
        for word in wordlist:
            if word not in stopWords:
                keywords.append(word)
        return keywords

def extract(text):
    ek = Extractkeys()
    wordlist = ek.CutWithPartOfSpeech(text)
    # keywords = ek.RemoveStopWord(wordlist)
    # newwordlist = ek.CutSimpleWord(keywords)
    extractwords = ek.ExtractWord(wordlist)
    # extractwords = newwordlist
    return extractwords

# def extract(text,document):
#     ek = Extractkeys()
#     wordlist = ek.CutWithPartOfSpeech(text)
#     keywords = ek.RemoveStopWord(wordlist)
#     newwordlist = ek.CutSimpleWord(keywords)
#     extractwords = ek.ExtractWord(newwordlist)
#     # print ','.join(extractwords)
#     document.append(extractwords)
#     return extractwords
if __name__ == '__main__':
    tags = ''
    try:
        filename = raw_input("请输入语料文本(带路径):")
        # filename = '/home/quincy1994/文档/微脉圈/训练集/美食/1268518877.txt'
        f = open(filename, 'r')
        print("\n--------------类别--------------")
        print("1.健康养生, 2.军事历史, 3.时政, 4.公益, 5.读书")
        print("6. 电视剧, 7.IT科技, 8'教育, 9.艺术, 10.电影")
        print("11.漫画, 12.游戏, 13.旅游, 14.美食, 15.摄影")
        print("16.萌宠, 17.服装美容, 18.体育, 19.设计, 20.综艺")
        print("21.星座, 22.音乐, 23.健身, 24.财经")
        category = raw_input("你选择的类别是(按序号):")
        data = f.readlines()
        document = []
        tags = []
        for text in data:
            print text
            extractwords = extract(text, document)
            print "第",(data.index(text)+1), "句提取的关键词有:", ','.join(extractwords)
            numbers = raw_input("你选择留下的是(按序号,从1开始,以空格分割,Enter代表结束提取,-1结束程序\n")
            if numbers == "-1":
                break
            if numbers == '':
                continue
            numberlist = numbers.split(' ')
            for num in numberlist:
                if num == '':
                    continue
                tags.append(extractwords[int(num)-1])
        print("提取的tag有:")
        tags = set(tags)
        for tag in tags:
            print tag
    finally:
        print ("你选择的类别是(按序号):"+category)
        print 'tags:', '/'.join(tags)
        print("提取完毕,谢谢!")
        print filename


    # filename = '/home/quincy1994/文档/微脉圈/训练集/萌宠/5464919306.txt'
    # pm = PMI(document,filename)
    # pmi = pm.GetNMI()
    # for p in pmi:
    #     print p,pmi[p]
    #/home/quincy1994/视频/体育/2792539300.txt