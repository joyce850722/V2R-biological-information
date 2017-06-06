import re
import os

def probable(path, value):
    #path = input("請輸入檔案...\n") #V2R_rootedML_0222.nwk
    #value = float(input("請輸入門檻值...\n"))

    fr = open(path, "r")
    data = fr.read().replace("'", "")

    res = r"(:[0-9||\.||]*)"
    pattern = re.compile(res)
    for match in re.finditer(pattern, data):
        data = data.replace(match.group(1), "")

    res = r"(\([^\()]*\))([0-9||\.||:]*)"
    pattern = re.compile(res)
    while data.count("(") != 1:
        for match in re.finditer(pattern, data):
            nowdata = match.group(0)
            sequence = match.group(1)
            probable = match.group(2)

            if float(probable) < value:
                nowdata = nowdata.replace("(", "").replace(")", "").replace(probable, "")        
                data = data.replace(match.group(0), nowdata)
            else:
                nowdata = nowdata.replace("(", "'").replace(")", "'").replace(probable, "")
                data = data.replace(match.group(0), nowdata)

    data = data.replace(",'", ",(")
    res = r"\((')"
    pattern = re.compile(res)
    for match in re.finditer(pattern, data):
        nowdata = match.group(0).replace(match.group(1), "(")
        data = data.replace(match.group(0), nowdata)

    data = data.replace("',", "),")
    res = r"(')\)"
    pattern = re.compile(res)
    for match in re.finditer(pattern, data):
        nowdata = match.group(0).replace(match.group(1), ")")
        data = data.replace(match.group(0), nowdata)

    fw = open("output\probable_output.nwk", "w")
    fw.write(data)
    fw.close()
