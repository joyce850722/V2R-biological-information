import re
import os
from Bio import Phylo

#使用者輸入
#path = input("請輸入檔案...\n") 	#example: V2R_rootedML_0222.nwk
#node = input("請輸入比較點...\n")	#輸入序列名或root
#distance = input("請輸入篩選距離...\n")

node = 0

#讀檔
def read_file(file_name):
    fr = open(file_name, "r")
    data = fr.read()
    fr.close()
    return data

#存檔
def save_file(file_name,data):
    fw = open(file_name, "w")
    fw.write(data)
    fw.close()
    
#取代特殊序列名
def replace_special(data):
    res = r"'[a-zA-Z0-9 \\\+\~\!\@\#\$\%\_\.\-\/\*\(\)\:\^\&\{\}\[\]\;\"\'\<]*'"
    special = re.findall(res, data)
    for scequence in special:
        change = str(scequence).replace(":", "").replace("'", "").replace(",", "")
        data = data.replace(scequence,change)
    return data

#移除機率
def remove_probable(data):
    res = r"(\)[0-9||\.||]*:)"
    data = re.sub(res,"):",data)
    return data

#合併到root
def combin_root():
    #合併直到不能合併
    length = 100
    while length != 0 :
        #find which can combin
        res = r"(\([^\()!]*\)):([0-9]+.[0-9]*)"
        data = read_file(r"output\distance_output.nwk")
        combin = re.findall(res, data)
        length = len(combin)
        #split the scequence to get I want
        i = 0
        for scequence in combin:
            combin[i] = re.split('[,:]+', str(combin[i]).replace("(", "").replace(")", "").replace("'", ""))
            #if is not the node we compare conbin the distance
            find = 0
            last = 0
            for item in combin[i]:
                if item == node:
                    find = 1
                last = last + 1
            #combin
            if find == 0:
                j = 0
                newcombin = ""
                #Calculate the distance from the node to root
                for item in combin[i]:
                    if j%2==1:
                        item = float(item)+float(combin[i][last-1])
                    if j <(last-1):
                        newcombin = newcombin+str(item)
                        if j<(last-2):
                            if j%2 == 0:
                                newcombin = newcombin+":"
                            if j%2 == 1:
                                newcombin = newcombin+","
                    j = j+1
                #save the conbin data
                data_change = read_file(r"output\distance_output.nwk")
                res = r"(\([^\()!']*\)[0-9||\.||:]*)"
                combin = re.findall(res, data)
                data_change = data_change.replace(combin[i],newcombin)
                #output the file
                save_file(r"output\distance_output.nwk",data_change)
                length = length +1
            else:
                length = length -1
            i = i+1
    return data_change

def Filterdistance(path, node, distance):
    if (node == "root" and os.path.isfile(r"output\root_point.txt")):
        os.remove("output\root_point.txt")

    if (node != "root" and os.path.isfile(r"output\point_point.txt")):
        os.remove("output\point_point.txt")
        
    data = read_file(path)
    data = replace_special(data)
    data = remove_probable(data)
    save_file(r"output\distance_output.nwk",data)
    data = combin_root()
    tree = Phylo.read(r"output\distance_output.nwk", "newick")
    
    if node == "root":
        res = r"([^\()!:,]*):([0-9]+.[0-9]*)"
        scequence = re.findall(res, data)
        i = 0
        for item in scequence:
            if float(item[1]) <= float(distance):
                tree.clade[i].color = "red"
                
                fw = open(r"output\root_point.txt", "a")
                fw.write(str(item[0]))
                fw.write(':')
                fw.write(str(item[1]))
                fw.write('\n')
                fw.close()
                
            i = i + 1
    else:
        #篩選出小於distance的node
        node_distance = 0        
        find = 0
        end = 0
        while end == 0:
            res = r"(\([^\()!]*\)):([0-9]+.[0-9]*)"
            data = read_file(r"output\distance_output.nwk")
            scequence = re.findall(res, data)
            if len(scequence)==0:
                res = r"([^\()!]*:[0-9]+.[0-9]*)"
                scequence = re.findall(res, data)
                outside_distance_position = 100
                end = 1
                scequence = re.split('[,:]+', str(scequence).replace("(", "").replace(")", "").replace("'", "").replace("[", "").replace("]", ""))
            else:
                scequence = re.split('[,:]+', str(scequence).replace("(", "").replace(")", "").replace("'", "").replace("[", "").replace("]", ""))
                outside_distance_position = len(scequence)-1
            #判斷比較點的位置
            node_position = 0
            for item in scequence:
                if item == node:
                    find = 1
                    node_distance = float(scequence[node_position+1])
                    break
                node_position = node_position +1
            if find ==1:
                #計算點到點的長度
                j = 0
                for item in scequence:
                    other_distance = 0
                    if j%2 ==0 and j != outside_distance_position :
                        #要是不是比較點，距離等於自己加比較點
                        if item != scequence[node_position]:
                            other_distance = float(scequence[node_position+1]) + float(scequence[j+1])
                            #進行篩選，小於等於篩選長度將序列名及距離輸出至output_node
                            if float(other_distance) <= float(distance):
                                mrca = tree.common_ancestor({"name": item})
                                mrca.color = "red"
                                
                                fw = open(r"output\point_point.txt", "a")
                                fw.write(item)
                                fw.write(':')
                                fw.write(str(other_distance))
                                fw.write('\n')
                                fw.close()
                                
                        #是比較點則距離等於自己
                        else:
                            if end == 1:
                                mrca = tree.common_ancestor({"name": item})
                                mrca.color = "red"
                                
                                node_distance = 0
                                fw = open(r"output\point_point.txt", "a")
                                fw.write(item)
                                fw.write(':')
                                fw.write(str(node_distance))
                                fw.write('\n')
                                fw.close()
                                
                            else:
                                node_distance = float(node_distance) + float(scequence[outside_distance_position])                
                    j = j + 1
                #更新node1.nwk
                res = r"(\([^\()!]*\):[0-9]+.[0-9]*)"
                data = read_file(r"output\distance_output.nwk")
                data_change = re.sub(res,(node+":"+str(node_distance)),data)
                save_file(r"output\distance_output.nwk",data_change)
            else:
                print("沒有你輸入的點")      

    Phylo.draw(tree, branch_labels=lambda c: c.branch_length)
