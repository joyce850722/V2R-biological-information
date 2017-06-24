#encoding: utf-8
import re
import os

def checkEqual(array,st,ed):
    for i in range(1,len(array)):
        if array[i][st-1:ed] != array[i-1][st:ed+1]:
            return False
    return True
def merge_br(filename, st, ed):
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
            
            if checkEqual(br,st,ed) == True:
                count = count+1
                tmp = ""
                for i in range(0,len(br)):
                    tmp = tmp + br[i][:br[i].rfind(":")] + "|"
                tmp = tmp[:-1] + pe_di[pe_di.find(":"):]
                data = data.replace(match.group(0),tmp[1:-1],1)
                
        print(count)

    fw = open(r"output/merge_output.nwk","w")
    fw.write(data)
    fw.close()
