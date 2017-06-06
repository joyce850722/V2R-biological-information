#encoding: utf-8
import re
import os

def checkEqual(array,st,ed):
    for i in range(1,len(array)):
        if array[i][st-1:ed] != array[i-1][st:ed+1]:
            return False
    return True
def merge_br(filename, st, ed):
    #st = int(input("匹配起始位置："))
    #ed = int(input("匹配結束位置："))
    #filename = "V2R_rootedML_0222.nwk"#input("請輸入檔案名稱(含附檔名)：")
    fr = open(filename,"r")
    data = fr.read()
    fr.close()
    res = r"(\([^\()]*\))([0-9||\.||:]*)"
    pattern = re.compile(res)

    count = 1
    dis = [0,0]
    while count != 0:
        count = 0
        for match in re.finditer(pattern, data):
            seq_name = []
            mh_str = match.group(1)
            pe_di = match.group(2)
            br = mh_str.split(",")
            #seq_name.append(br[0][:br[0].find(":")])
            #br[0] = br[0][st:ed+1]
            if checkEqual(br,st,ed) == True:
                count = count+1
                tmp = ""
                for i in range(0,len(br)):
                    tmp = tmp + br[i][:br[i].rfind(":")-1] + "|"
                tmp = tmp[:-1] + pe_di[pe_di.find(":"):]
                data = data.replace(match.group(0),tmp[1:-1],1)
                #print(tmp1,tmp2)
                #print (match.groups(i+1))
        print(count)

    fw = open("output.nwk","w")
    fw.write(data)
    fw.close()
    filename = "output.nwk"
"""
st = int(input("匹配起始位置："))
ed = int(input("匹配結束位置："))
filename = "testData\V2R_rootedML_0222.nwk"#input("請輸入檔案名稱(含附檔名)：")
merge_br(filename, st, ed)

    res = "\)[0-9||.]*:"
    pattern = re.compile(res)
    for i, line in enumerate(open(filename)):
            for match in re.finditer(pattern, line):
                 tmp_str = match.group(i)
                 data = data.replace(str(tmp_str),"):")

    fw = open("output.nwk","w")
    fw.write(data)
    fw.close()
    filename = "output.nwk"
"""
