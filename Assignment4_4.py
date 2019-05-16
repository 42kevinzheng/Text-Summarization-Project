import nltk
import os
from collections import defaultdict
from nltk import FreqDist
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk import word_tokenize
from nltk import tokenize

final = []
final2 = []
pathToStudent = ("./Datastudent/Data2014/2014_4_101_400")
StudentOpen = os.listdir(pathToStudent)  # Path of the student essays
fileList = []   # empty array to hold all the final text files
for file in StudentOpen:
    if file[18:23] == "final":    # read all the final files in the DataStudent folder.
        fileList.append(file)  # add to the array
for file in fileList:
        with open(os.path.join(pathToStudent, file), 'r') as myfile:  # read the files
            freqStudent = defaultdict(int)
            for line in myfile:
                sentence = line.split('.')  # split the sentence by their period
                for word in sentence:
                    tokens = word_tokenize(word)  # tokenization
                    tk = nltk.pos_tag(tokens)  # NLTK tagging
                    fileList2 = []  # empty array to hold all tokens
                    fileList3 = []  # empty array to hold all tagsets
                    for k, v in tk:
                        fileList2.append(k)  # add tokens to the array
                        fileList3.append(v)  # add tagsets to the array
                    a = 0
                    for a in range(len(fileList3)):
                        x = a+1
                        z = a-1
                        q = a-2
                        if(x < len(fileList3)):
                            if (fileList3[a]=='NNP' and (fileList3[x]!='NNP' and fileList3[z]!="NNP") and fileList3[x]!='NNPS'):
                                f = fileList2[a]
                                ff = str(f)
                                fff = ff.lower()
                                freqStudent[fff] += 1
                            elif ((fileList3[a] == "NNP" and fileList3[x] == 'NNP')):  # +1
                                ff = fileList2[a], fileList2[x]
                                fff = str(ff)
                                ffff = fff.lower()
                                freqStudent[ffff] += 1
                            if (fileList3[a] == 'NNPS' and (fileList3[x] != 'NNP' and fileList3[z] != "NNP")):
                                f = fileList2[a]
                                ff = str(f)
                                fff = ff.lower()
                                freqStudent[fff] += 1
                            elif ((fileList3[a] == "NNPS" and fileList3[x] == 'NNPS')):  # +1
                                ff = fileList2[a], fileList2[x]
                                fff = str(ff)
                                ffff = fff.lower()
                                freqStudent[ffff] += 1
                            if (fileList3[a] == "NNP" and fileList3[x] == "VB"):
                                f = fileList2[a]
                                ff = str(f)
                                fff = ff.lower()
                                freqStudent[fff] += 1
                            if (fileList3[a] == "NNP" and fileList3[x] == "VB"):
                                f = fileList2[a]
                                ff = str(f)
                                fff = ff.lower()
                                freqStudent[fff] += 1
                            if (fileList3[a] == "NNP" and fileList3[x] == "VBN"):
                                f = fileList2[a]
                                ff = str(f)
                                fff = ff.lower()
                                freqStudent[fff] += 1
                            if (fileList3[a] == "NNP" and fileList3[x] == "VBD"):
                                f = fileList2[a]
                                ff = str(f)
                                fff = ff.lower()
                                freqStudent[fff] += 1
                            if (fileList3[a] == "NNPS" and fileList3[x] == "VB"):
                                f = fileList2[a]
                                ff = str(f)
                                fff = ff.lower()
                                freqStudent[fff] += 1
                            if (fileList3[a] == "NNPS" and fileList3[x] == "VBN"):
                                f = fileList2[a]
                                ff = str(f)
                                fff = ff.lower()
                                freqStudent[fff] += 1
                            if (fileList3[a] == "NNPS" and fileList3[x] == "VBD"):
                                f = fileList2[a]
                                ff = str(f)
                                fff = ff.lower()
                                freqStudent[fff] += 1
                            if (fileList3[a] == "NNS" and fileList3[x] == "VBZ"):
                                f = fileList2[a]
                                ff = str(f)
                                fff = ff.lower()
                                freqStudent[fff] += 1
                            if (fileList3[a] == "NNS" and fileList3[x] == "VB"):
                                f = fileList2[a]
                                ff = str(f)
                                fff = ff.lower()
                                freqStudent[fff] += 1
                            if (fileList3[a] == "NNS" and fileList3[x] == "VBN"):
                                f = fileList2[a]
                                ff = str(f)
                                fff = ff.lower()
                                freqStudent[fff] += 1
                            if (fileList3[a] == "NNS" and fileList3[x] == "VBD"):
                                f = fileList2[a]
                                ff = str(f)
                                fff = ff.lower()
                                freqStudent[fff] += 1
                            if (fileList3[a] == "NN" and fileList3[x] == "VBN"):
                                f = fileList2[a]
                                ff = str(f)
                                fff = ff.lower()
                                freqStudent[fff] += 1
                            if (fileList3[a] == "NN" and fileList3[x] == "VBD"):
                                f = fileList2[a]
                                ff = str(f)
                                fff = ff.lower()
                                freqStudent[fff] += 1
                            if ((fileList3[a] == "NN" and fileList3[x] == 'VBZ')):
                                f = fileList2[a]
                                ff = str(f)
                                fff = ff.lower()
                                freqStudent[fff] += 1
                            if ((fileList3[a] == "NN" and fileList3[x] == 'VB')):
                                f = fileList2[a]
                                ff = str(f)
                                fff = ff.lower()
                                freqStudent[fff] += 1
                            if ((fileList3[a] == "NNP" and fileList3[x] == 'NN')):     # +1
                                ff = fileList2[a], fileList2[x]
                                fff = str(ff)
                                ffff = fff.lower()
                                freqStudent[ffff] += 1
                            if ((fileList3[a] == "NNP" and fileList3[x] == 'NNS')):  # +1
                                ff = fileList2[a], fileList2[x]
                                fff = str(ff)
                                ffff = fff.lower()
                                freqStudent[ffff] += 1
                            if ((fileList3[a] == "NNP" and fileList3[x] == 'NNPS')):  # +1
                                ff = fileList2[a], fileList2[x]
                                fff = str(ff)
                                ffff = fff.lower()
                                freqStudent[ffff] += 1
                            if ((fileList3[a] == "NN" and fileList3[x] == 'NNP')):     # +1
                                ff = fileList2[a], fileList2[x]
                                fff = str(ff)
                                ffff = fff.lower()
                                freqStudent[ffff] += 1
                            if ((fileList3[a] == "NN" and fileList3[x] == 'NN')):     # +1
                                ff = fileList2[a], fileList2[x]
                                fff = str(ff)
                                ffff = fff.lower()
                                freqStudent[ffff] += 1
                            if ((fileList3[a] == "NN" and fileList3[x] == 'NNS')):  # +1
                                ff = fileList2[a], fileList2[x]
                                fff = str(ff)
                                ffff = fff.lower()
                                freqStudent[ffff] += 1
                            if ((fileList3[a] == "NN" and fileList3[x] == 'NNPS')):  # +1
                                ff = fileList2[a], fileList2[x]
                                fff = str(ff)
                                ffff = fff.lower()
                                freqStudent[ffff] += 1
                            if ((fileList3[a] == "NNPS" and fileList3[x] == 'NNP')):     # +1
                                ff = fileList2[a], fileList2[x]
                                fff = str(ff)
                                ffff = fff.lower()
                                freqStudent[ffff] += 1
                            if ((fileList3[a] == "NNPS" and fileList3[x] == 'NN')):     # +1
                                ff = fileList2[a], fileList2[x]
                                fff = str(ff)
                                ffff = fff.lower()
                                freqStudent[ffff] += 1
                            if ((fileList3[a] == "NNPS" and fileList3[x] == 'NNS')):  # +1
                                ff = fileList2[a], fileList2[x]
                                fff = str(ff)
                                ffff = fff.lower()
                                freqStudent[ffff] += 1
                            if ((fileList3[a] == "NNS" and fileList3[x] == 'NNP')):     # +1
                                ff = fileList2[a], fileList2[x]
                                fff = str(ff)
                                ffff = fff.lower()
                                freqStudent[ffff] += 1
                            if ((fileList3[a] == "NNS" and fileList3[x] == 'NN')):     # +1
                                ff = fileList2[a], fileList2[x]
                                fff = str(ff)
                                ffff = fff.lower()
                                freqStudent[ffff] += 1
                            if ((fileList3[a] == "NNS" and fileList3[x] == 'NNS')):  # +1
                                ff = fileList2[a], fileList2[x]
                                fff = str(ff)
                                ffff = fff.lower()
                                freqStudent[ffff] += 1
                            if ((fileList3[a] == "NNS" and fileList3[x] == 'NNPS')):  # +1
                                ff = fileList2[a], fileList2[x]
                                fff = str(ff)
                                ffff = fff.lower()
                                freqStudent[ffff] += 1
                            if ((fileList3[q] == "NNS" and fileList3[x] == 'NNPS' and fileList3[a]=='NNP')):  # +1
                                ff = fileList2[q], fileList2[x],fileList2[a]
                                fff = str(ff)
                                ffff = fff.lower()
                                freqStudent[ffff] += 1
                            if ((fileList3[q] == "NNP" and fileList3[x] == 'NNP' and fileList3[a] == 'NNP')):  # +1
                                ff = fileList2[q], fileList2[x], fileList2[a]
                                fff = str(ff)
                                ffff = fff.lower()
                                freqStudent[ffff] += 1
                            if ((fileList3[q] == "NN" and fileList3[x] == 'NN' and fileList3[a] == 'NN')):  # +1
                                ff = fileList2[q], fileList2[x], fileList2[a]
                                fff = str(ff)
                                ffff = fff.lower()
                                freqStudent[ffff] += 1
            free = FreqDist(freqStudent)
            fun = free.most_common(5)  # Find the 10 most common tags in NLTK
            thi = free.most_common(1)
            for d, s in thi:
                aa = d
        final.append(file)
        final2.append(aa)
zz = list(zip(final, final2))
my_list = list(set(final2))
for l in my_list:
    print("These files has the same topics:")
    for qq in zz:
        if (l == qq[1]):
            print(qq)
            tokenizer = RegexpTokenizer(r'\w+')  # Remove punctuations
            stopWords = set(stopwords.words('english'))
            read = open(os.path.join(pathToStudent, qq[0]), 'r')
            essaySum = 0
            essaySen = 0
            for para in read:
                freqStudent = defaultdict(int)
                senList = []
                paragraph = para.split('\n\n')
                for s in paragraph:
                    toto = tokenize.sent_tokenize(s)
                    for stuff in toto:
                        senList.append(stuff)
                        tokens = tokenizer.tokenize(stuff)
                        for word in tokens:
                            if word not in stopWords:
                                freqStudent[word] += 1
                free = FreqDist(freqStudent)
                fun = free.most_common()
                high = free.most_common(1)
                for k, v in high:
                    highest = v
                keyDict = {}
                valueDict = {}
                index = 0
                for one, two in fun:
                    keyDict[index] = one
                    valueDict[index] = two
                    index += 1
                highDict = {}
                for sene in senList:  # Array of sentences
                    sum = 0
                    sum_token = word_tokenize(sene)  # Token each sentence.
                    for xxx in sum_token:  # Loop each word in the sentence.
                        if xxx in keyDict.values():  # If word is in the keyList, then go ahead.
                            vv = [key for (key, value) in keyDict.items() if value == xxx]
                            ass = int(vv[0])
                            vvv = [value for (key, value) in valueDict.items() if key == ass]
                            ass2 = int(vvv[0])
                            hh = ass2 / highest
                            sum += hh
                        highDict[sene] = sum
                sorted_x = sorted(highDict.items(), key=lambda kv: kv[1])
                sorted_x.reverse()
                print('\n')
                totalSum = 0
                totalSen = 0
                for e, v in sorted_x:
                    print(e, '  :::  ', "(Sentence value:", v, ")")
                    totalSum += v
                    totalSen += 1
                if(totalSen != 0 and totalSum !=0):
                    print("\n")
                    print(fun)
                    print("The total sum of the paragraph:", totalSum)
                    print("The total number of sentences:", totalSen)
                    print("The average value of the paragraph:", totalSum/totalSen)
                    essaySum +=totalSum
                    essaySen +=totalSen
            print('\n\n')
            print('The essay analysis is done\n\n')
            print("The total number of sentences in this essay:",essaySen)
            print("The total sum value of this essay:",essaySum)
            print("The average value of this essay:",essaySum/essaySen)
            print('\n\n\n')
            print('##########################################################################################################')
            print("\n\n\n\n\n")
            print("Onto the next essay")
            print('\n\n\n\n\n')
            print('##########################################################################################################')


