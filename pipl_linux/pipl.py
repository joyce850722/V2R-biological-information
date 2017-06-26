# -*- coding: utf-8 -*-
import math
import os
import shutil
from collections import defaultdict
def spfile(name,fl):
    str = ""
    mark = ""
    if os.path.exists("b/"+name) == False:
        os.makedirs("b/"+name)
    f = open(fl,'r')
    while 1:
        st = f.readline()
        if (st == ""):
            if (os.path.isfile("b/"+name+"/"+mark+".txt") == False):
                f1 = open("b/"+name+"/"+mark+".txt",'w')
                f1.write(str)
                f1.close()
            break
        elif(st[0]==">"):
            if mark != "":
                if (os.path.isfile("b/"+name+"/"+mark+".txt") == False):
                    f1 = open("b/"+name+"/"+mark+".txt",'w')
                    f1.write(str)
                    f1.close()
                str = ""
            mark = st[1:-1]
            mark = markch(mark)
            str = ">"+mark+"\n"
        else:
            if (os.path.isfile("b/"+name+"/"+mark+".txt") == False):
                str += st[:-1]
    f.close
def splitfile(q,ss = []) :
    path = q+"e-10.txt"
    f = open(path,'r')
    while 1:
        st = f.readline()
        ss.extend(st.split(","))
        if (st == ""):
            break
    f.close
    return 0
def sort(s = [],e = []):
    esort = []
    op = []
    for i in range(len(s)):
        s[i] = int(s[i])
        e[i] = int(e[i])
    ssort = sorted(s)
    for i in range(len(ssort)):
        for j in range(len(s)):
            if (ssort[i] == s[j]):
                esort.insert(i,e[j])
                continue
        if (i==0):
            if (ssort[0]>=4000):
                op.insert(0,ssort[0]-4000)
            else:
                op.insert(0,0)
            op.insert(1,esort[0])
        elif ((ssort[i]<=op[len(op)-1]) & (esort[i]>op[len(op)-1])):
            op[len(op)-1] = esort[i]
        elif (ssort[i]>op[len(op)-1]):
            if (ssort[i]<op[len(op)-1]+1000):
                op[len(op)-1] = esort[i]+1000
            elif (ssort[i]-4000<op[len(op)-1]):
                op[len(op)-1] = esort[i]
            else:
                if (ssort[i]>=4000):
                    op.insert(len(op),ssort[i]-4000)
                else:
                    op.insert(len(op),0)
                op.insert(len(op),esort[i])
    return op
def fileout(name,q , d , l = [],n=[]):
    d = markch(d)
    strs=">"+ d +" "+q+"\n"
    f = open("b/"+name+"/"+d+".txt")
    f.readline()
    st=f.readline()
    t = int(len(l)/2)-1
    for i in range(t):
        ss = st[l[i*2]:l[i*2+1]]
        fw = open("br/"+q+"_"+d+"l"+str(i)+".fa","w")
        fw.write(strs+ss)
        fw.close()
    t = int(len(n)/2)-1
    for i in range(t):
        ss = st[n[i*2]:n[i*2+1]]
        ss = ss[::-1]
        fw = open("br/"+q+"_"+d+"n"+str(i)+".fa","w")
        fw.write(strs+ss)
        fw.close()
    return 0
def markch(s):
    s = s.split(" ")
    ss = ""
    for i in range(len(s[0])):
        if s[0][i] !="|":
            ss += s[0][i]
    return(ss)
def blast(d,q):
    ss = []
    qc = []
    dc = []
    t = 0
    j=0
    a = splitfile(q,ss)
    fl = "b/"+q+".fa"
    spfile(q,fl)

    for j in range(int(len(ss)/12)):
        ls = []
        le = []
        ns = []
        ne = []
        boo = 1
        for i in range(len(qc)):
            if ((ss[j*12]==qc[i])&(ss[j*12+1]==dc[i])):
                boo = 0
                break
    
        if (boo== 1):
            qc.insert(t,ss[j*12])
            dc.insert(t,ss[j*12+1])
            for i in range(len(ss)-1):
                if ((ss[i]==qc[t])&(ss[i+1] ==dc[t])):
                    if (ss[i+8]<ss[i+9]):
                        ls.insert(len(ls),ss[i+8])
                        le.insert(len(le),ss[i+9])
                    else:
                        ns.insert(len(ns),ss[i+8])
                        ne.insert(len(ne),ss[i+9])
                i+=11
            sl = sort(ls,le)
            sn = sort(ns,ne)
            fileout(q,qc[t],dc[t],sl,sn)
            t+=1
def orf():
	fw = open("brs.fasta", "w")
	path = "br/"
	file_data = os.listdir(path)

	for file in range(1, len(file_data), 1):
	    fr = open(path+file_data[file], "r")
	    dna = fr.read()

	    longest = 0
	    location = (dna.find("\n") + 1)
	    information = dna[: location]
	    orisequence = dna[location :].upper()

	    for retro in range(0, 2, 1):
		for start in range(0, 3, 1):
		    sequence = orisequence[start :].replace("N", "").replace("\n", "")
		    sequence = ",".join([sequence[i : i+3] for i in range(0, len(sequence), 3)])
		    
		    #delete the extra sequence
		    sequence = sequence.split(",")       
		    if len(sequence[len(sequence) - 1]) != 3:
		        del sequence[len(sequence) - 1]
		    sequence = ",".join(sequence)
		    
		    a = sequence.replace("GCT", "A").replace("GCC", "A").replace("GCA", "A").replace("GCG", "A")
		    c = a.replace("TGT", "C").replace("TGC", "C")
		    d = c.replace("GAT", "D").replace("GAC", "D")
		    e = d.replace("GAA", "E").replace("GAG", "E")
		    f = e.replace("TTT", "F").replace("TTC", "F")
		    g = f.replace("GGT", "G").replace("GGC", "G").replace("GGA", "G").replace("GGG", "G")
		    h = g.replace("CAT", "H").replace("CAC", "H")
		    i = h.replace("ATT", "I").replace("ATC", "I").replace("ATA", "I")
		    k = i.replace("AAA", "K").replace("AAG", "K")
		    l = k.replace("CTT", "L").replace("CTC", "L").replace("CTA", "L").replace("CTG", "L").replace("TTA", "L").replace("TTG", "L")    
		    m = l.replace("ATG", "M")
		    n = m.replace("AAT", "N").replace("AAC", "N")
		    p = n.replace("CCT", "P").replace("CCC", "P").replace("CCA", "P").replace("CCG", "P")
		    q = p.replace("CAA", "Q").replace("CAG", "Q")
		    r = q.replace("CGT", "R").replace("CGC", "R").replace("CGA", "R").replace("CGG", "R").replace("AGA", "R").replace("AGG", "R")
		    s = r.replace("TCT", "S").replace("TCC", "S").replace("TCA", "S").replace("TCG", "S").replace("AGT", "S").replace("AGC", "S")
		    t = s.replace("ACT", "T").replace("ACC", "T").replace("ACA", "T").replace("ACG", "T")
		    v = t.replace("GTT", "V").replace("GTC", "V").replace("GTA", "V").replace("GTG", "V")
		    w = v.replace("TGG", "W")
		    y = w.replace("TAT", "Y").replace("TAC", "Y")
		    x = y.replace("TAA", "X").replace("TAG", "X").replace("TGA", "X")
		    protein = x.replace(",", "")
		    
		    #find the longest sequence
		    position = 0
		    while True:
		        position = protein.find("M", (position + 1))
		        if position == -1:
		            break
		        length = protein.find("X", position) - position + 1
		        if longest < length:
		            longest = length
		            result = protein[position : (position + length)]
		
		#reverse the sequence
		orisequence = orisequence[: : (-1)]

	    #filter the longest and output data
	    if longest >= 100:
		information += result + "\n"
		fw.write(information)
	    
	fw.close()
def dts(d):
	path = "b/"
	result = ""
	fr = open(path+d+".fa", "r")
	dna = fr.read()
	dna = dna.split("\n")
	for i in range(len(dna)/2):
		information = dna[i*2]
		
		sequence = dna[i*2+1]
		sequence = ",".join([sequence[i : i+3] for i in range(0, len(sequence), 3)])
		 
		a = sequence.replace("GCT", "A").replace("GCC", "A").replace("GCA", "A").replace("GCG", "A")
		c = a.replace("TGT", "C").replace("TGC", "C")
		d = c.replace("GAT", "D").replace("GAC", "D")
		e = d.replace("GAA", "E").replace("GAG", "E")
		f = e.replace("TTT", "F").replace("TTC", "F")
		g = f.replace("GGT", "G").replace("GGC", "G").replace("GGA", "G").replace("GGG", "G")
		h = g.replace("CAT", "H").replace("CAC", "H")
		i = h.replace("ATT", "I").replace("ATC", "I").replace("ATA", "I")
		k = i.replace("AAA", "K").replace("AAG", "K")
		l = k.replace("CTT", "L").replace("CTC", "L").replace("CTA", "L").replace("CTG", "L").replace("TTA", "L").replace("TTG", "L")
		m = l.replace("ATG", "M")
		n = m.replace("AAT", "N").replace("AAC", "N")
		p = n.replace("CCT", "P").replace("CCC", "P").replace("CCA", "P").replace("CCG", "P")
		q = p.replace("CAA", "Q").replace("CAG", "Q")
		r = q.replace("CGT", "R").replace("CGC", "R").replace("CGA", "R").replace("CGG", "R").replace("AGA", "R").replace("AGG", "R")
		s = r.replace("TCT", "S").replace("TCC", "S").replace("TCA", "S").replace("TCG", "S").replace("AGT", "S").replace("AGC", "S")
		t = s.replace("ACT", "T").replace("ACC", "T").replace("ACA", "T").replace("ACG", "T")
		v = t.replace("GTT", "V").replace("GTC", "V").replace("GTA", "V").replace("GTG", "V")
		w = v.replace("TGG", "W")
		y = w.replace("TAT", "Y").replace("TAC", "Y")
		z = y.replace("TAA", "X").replace("TAG", "X").replace("TGA", "X")
		 
		protein = z.replace(",", "")
		information +=  "\n"
		information += protein + "\n"
		result += information
	fw = open("hmmmmake.fasta", "w")
	fw.write(result)
	fw.close()
def dtp():
	path = "WDNA_result/"
	file_data = os.listdir(path)
	 
	for file in range(0, len(file_data), 1):
	    fr = open(path+file_data[file], "r")
	    dna = fr.read()
	 
	    location = (dna.find("\n") + 1)
	    information = dna[: location]    
	    sequence = dna[location :].replace("\n", "")
	     
	    sequence = ",".join([sequence[i : i+3] for i in range(0, len(sequence), 3)])
	     
	    a = sequence.replace("GCT", "A").replace("GCC", "A").replace("GCA", "A").replace("GCG", "A")
	    c = a.replace("TGT", "C").replace("TGC", "C")
	    d = c.replace("GAT", "D").replace("GAC", "D")
	    e = d.replace("GAA", "E").replace("GAG", "E")
	    f = e.replace("TTT", "F").replace("TTC", "F")
	    g = f.replace("GGT", "G").replace("GGC", "G").replace("GGA", "G").replace("GGG", "G")
	    h = g.replace("CAT", "H").replace("CAC", "H")
	    i = h.replace("ATT", "I").replace("ATC", "I").replace("ATA", "I")
	    k = i.replace("AAA", "K").replace("AAG", "K")
	    l = k.replace("CTT", "L").replace("CTC", "L").replace("CTA", "L").replace("CTG", "L").replace("TTA", "L").replace("TTG", "L")    
	    m = l.replace("ATG", "M")
	    n = m.replace("AAT", "N").replace("AAC", "N")
	    p = n.replace("CCT", "P").replace("CCC", "P").replace("CCA", "P").replace("CCG", "P")
	    q = p.replace("CAA", "Q").replace("CAG", "Q")
	    r = q.replace("CGT", "R").replace("CGC", "R").replace("CGA", "R").replace("CGG", "R").replace("AGA", "R").replace("AGG", "R")
	    s = r.replace("TCT", "S").replace("TCC", "S").replace("TCA", "S").replace("TCG", "S").replace("AGT", "S").replace("AGC", "S")
	    t = s.replace("ACT", "T").replace("ACC", "T").replace("ACA", "T").replace("ACG", "T")
	    v = t.replace("GTT", "V").replace("GTC", "V").replace("GTA", "V").replace("GTG", "V")
	    w = v.replace("TGG", "W")
	    y = w.replace("TAT", "Y").replace("TAC", "Y")
	    z = y.replace("TAA", "X").replace("TAG", "X").replace("TGA", "X")
	     
	    protein = z.replace(",", "")
	    information += protein + "\n"
	 
	    filename = "protein/"+file_data[file] + ".fasta"
	    fw = open(filename, "w")
	    fw.write(information)
	    fw.close()
def ghmark():
	fr = open("hmmout.txt","r")
	result = ""
	for line in fr.readlines():
		if line.find("#") == -1:
			a = line.find(" ") 		
		        result = result + line[144:]
	fw = open("hmmout1.txt","w")
	fw.write(result)
	fw.close()
def hmmresult():
	fr = open("hmmout1.txt","r")
	fe = open("brs.fasta","r")
	a = fe.read()

	result = ""

	for line in fr.readlines():
		line = line.strip("\n")
		key1 = a.find(line)
	       	b = a[key1-1:]
		key2 = b.find("\n")	
		key3 = b.find("\n",key2+1) 
		c = b[0:key3]
		result = result + c + "\n"
	
	fw = open("hr.fasta","w")
	fw.write(result)
	fw.close()
def wise2(d):
	if not os.path.isdir("WDNA_result"):
		os.mkdir("WDNA_result")
	if not os.path.isdir("Wise_output"):
		os.mkdir("Wise_output")
	#read V2R file
	fr = open('b/'+d+'.fa','r')
	data = fr.read()
	data_wr = data
	time = data.count(">")

	out_path = "WDNA_result"#output path for exon seq.
	DATA_DIR = "br/"#input blast result path
	wise_out_path = "Wise_output"
	file_data = []

	#rest
	file_num=0
	max_score=0
	min_score=10000

	for filename in os.listdir(DATA_DIR):
		tmp_name = filename.replace(".fa","")
		#tmp_name = tmp_name.strip(".fa")
	
		if (os.path.isfile("%s/%s.fasta" %(wise_out_path,tmp_name))):
		   continue
	
		print "loading %s" % tmp_name
		file_data.append(tmp_name)
	
		#cut v2r one seq
		tmp = filename.find(".") +1
		v2r_name = filename[0:tmp].strip(" ")
		v2r_st = data.find(v2r_name,0)
	
		#To cut the last v2r seq
		if(v2r_st == 39733):
			v2r_ed = len(data)
			data_wr = data[v2r_st-1:]
		else:
			v2r_ed = data[v2r_st:].find(">") + v2r_st
			data_wr = data[v2r_st-1:v2r_ed]
		
		#print("V2R_st:%d V2R_ed:%d" %(v2r_st,v2r_ed))
	
		#If it can not find v2r seq, output a error file
		if(v2r_st>=v2r_ed or v2r_st<0 or v2r_ed<0):
			print "error!!can not find V2R sequence,It must have wrong on DNA's file name!"
			error_fw = open("error_list.txt","a")
			error_data = tmp_name+":can not find V2R sequence,It must have wrong on DNA file name.\n"
			error_fw.write(error_data)
			error_fw.close()
			continue
	
		#open the v2r file cut before
		fw = open("v2r.fasta", "w")
		fw.write(data_wr)
		fw.close()
	
		#Wise2 cmd line
		wise_info = os.system("genewise v2r.fasta %s/%s.fa >%s/%s.txt -genesf -cdna" %(DATA_DIR,tmp_name,wise_out_path,tmp_name))
	
		#If return error code output error file
		if(wise_info != 0):
			print "error!!Wise2 can not analyze the sequences!"
			error_fw = open("error_list.txt","a")
			error_data = tmp_name+":Wise2 can not analyze the sequences.\n"
			error_fw.write(error_data)
			error_fw.close()
			continue
	
		#read wise2 output file
		wise_out_fr = open('%s/%s.txt' %(wise_out_path,tmp_name),'r')
		wise_out = wise_out_fr.read()
		wise_out_fr.close()
	
		#find output score
		score_pos = wise_out.find("Score") + 6
		score = wise_out[score_pos:]
		score_pos = score.find(" ")
		score_str = score[0:score_pos].strip(" ")
		score = float(score_str)
	
		#find the best&worst score
		if(score > max_score):
			max_score = score
		elif(score < min_score):
			min_score = score
	
		file_num = file_num + 1
	
	
		#write score in file
		score_fw = open("score_list.txt","a")
		score_w = tmp_name + " " + score_str + "\n"
		score_fw.write(score_w)
		score_fw.close()
	
		#cut exon and output the result file
		wise_out = wise_out[wise_out.find("//")+3:]
		"""
		last_num_pos = wise_out.find("Exon") -3
		last_num = int(wise_out[last_num_pos-5:last_num_pos].strip(" "))
		"""
		out_seq = wise_out[wise_out.find("["):-3]
		#out_seq = out_seq[out_seq.find("\n")+1:]
	
		#read DNA file, and find DNA tag
		dna_fr = open('%s/%s.fa' %(DATA_DIR,tmp_name),'r')
		dna_tag = dna_fr.readline()
		dna_tag = dna_tag[:-2]
		dna_fr.close()
	
		#find termination code
		"""
		dna = dna_fr.read().strip(dna_tag)
		dna_col = dna.find("\n")
		dna_ = dna[last_num/dna_col+last_num:]
		"""
		#write seq file
		out_seq = dna_tag + out_seq
		fw_out_seq = open("%s/%s.fasta" %(out_path,tmp_name), "w")
		fw_out_seq.write(out_seq)
		fw_out_seq.close()	
	

	fr.close()
	print "The best score:%f" %(max_score)
	print "The worst score:%f" %(min_score)
def wextend():
	out_path = "WDNA_result"#output path for exon seq.
	DATA_DIR = "Wise_output"
	blast_path = "br"
	file_data = []
	#rest
	file_num=0
	max_score=0
	min_score=10000

	for filename in os.listdir(DATA_DIR):
		print "loading %s" % filename
		filename = filename.strip(".txt")
	
		#open the v2r file cut before
		fr = open("%s/%s.txt" %(DATA_DIR,filename), "r")
		wise_out = fr.read()
		fr.close()
		wise_out = wise_out[wise_out.find("//")+3:]
		#find output position
		gene_num = wise_out.count("Gene")
		cdna = []
		if gene_num == 2:
			cdna.append(wise_out[wise_out.find("//")+3:-3])
		else:	
			cdna = wise_out[wise_out.find("//")+3:].split(">")
	
		cut_list = []
		all_dna = []
		for i in range(0,gene_num/2):
			st_pos = wise_out.find("Gene") + 12
			cut_num = wise_out[st_pos:]
			cut_num = cut_num[:cut_num.find("\n")]
		
			cut_list = cut_num.strip().split(" ")
		
			dna_st = int(cut_list[0])-1
			dna_ed = int(cut_list[1])-1
		
			o_st = dna_st
			o_ed = dna_ed
		
			fr_dna = open("%s/%s.fa" %(blast_path,filename),"r")
			dna = fr_dna.read().upper()
			fr_dna.close()
			tag_ed = dna.find("\n")+1
			dna = dna[tag_ed:].replace("\n","")
		
			if dna[dna_st : (dna_st + 3)] != "ATG" and dna[(dna_ed - 3) : dna_ed] != "TAG" and dna[(dna_ed - 3) : dna_ed] != "TAA" and dna[(dna_ed - 3) : dna_ed] != "TGA":
				for dna_st in range(dna_st,0,-3):
					sequence = dna[(dna_st - 3) : dna_st]
					if sequence == "ATG" or sequence == "TAG" or sequence == "TAA" or sequence == "TGA":
						dna_st = dna_st - 3
						break
			head_dna = dna[dna_st:o_st]
		
			if dna[(dna_ed - 3) : dna_ed] != "TAG" and dna[(dna_ed - 3) : dna_ed] != "TAA" and dna[(dna_ed - 3) : dna_ed] != "TGA":
				for dna_ed in range(dna_ed,len(dna),3):
					sequence = dna[dna_ed : (dna_ed + 3)]
					if sequence == "TAG" or sequence == "TAA" or sequence == "TGA":
						dna_ed = dna_ed + 3
						break
			tail_dna = dna[o_ed: dna_ed]
		
			dna_tag = ">"+filename[:-1]+" [%d:%d].sp\n" %(dna_st,dna_ed)
		
			all_dna.append(head_dna + cdna[i][cdna[i].find("\n")+1:].replace("\n","") + tail_dna)

	
	
		dna_len = []
		su_count = 0
	
		if gene_num > 2:
			dna = all_dna[all_dna.index(max(all_dna))]
			if len(dna)>749:
				list_data = list(dna)
				fr_dna = open("%s/%s.fasta" %(out_path,filename),"w")
				for col in range(60,len(dna)+int(len(dna)/61),61):
					list_data.insert(col,"\n")
				dna = "".join(list_data)
				data = dna_tag + dna
				fr_dna.write(data)
		elif gene_num == 2:
			dna = all_dna[0]
			if len(dna)>749:
				list_data = list(dna)
				fr_dna = open("%s/%s.fasta" %(out_path,filename),"w")
				for col in range(60,len(dna)+int(len(dna)/61),61):
					list_data.insert(col,"\n")
				dna = "".join(list_data)
				data = dna_tag + dna
				fr_dna.write(data)
def wdel_file():
	#count the score
	sdan = 451.89
	table = defaultdict(int)
	out_path = "WDNA_result"
	wise_path = "Wise_output"
	count = 0
	score_list = []

	fw = open("new_score_list.txt","a")

	with open("score_list.txt","r") as fr:
		fw.write("".join(list(set([i for i in fr]))))
	fw.close()
	os.remove("score_list.txt")

	with open("new_score_list.txt","r") as fr:
		for line in fr:
			if line == "\n":
				continue
			else:
				pos = line.find(" ")+1
				line = line.strip("\n")
				table[line[0:pos].strip(" ")] = float(line[pos:].strip(" "))
				count = count+1

	print("file num",count)
	count = int(math.floor(count*0.95))
	score_lst = list(table.values())
	score_lst = sorted(score_lst)
	print(len(score_lst))
	print(count)
	sdan = score_lst[count] 

	print "Standard deviation:%f" %(sdan)
	#score_lst = list(table.values())
	for key in table:
		if table[key] < sdan:
			#print "delete:%s" %(name_list[int(i)])
			if (os.path.isfile("%s/%s.fasta" %(out_path,key))):
				os.remove("%s/%s.fasta" %(out_path,key))
			if (os.path.isfile("%s/%s.txt" %(wise_path,key))):
				os.remove("%s/%s.txt" %(wise_path,key))
				#print "delete:%s" %(name_list[i])

	if os.path.isfile("error_list.txt"):
		with open("error_list.txt","r") as fr:
			for line in fr:
				pos = line.find(":")+1
				name = line[:pos].strip()
				if os.path.isfile("%s/%s.fasta" %(out_path,name)):
					os.remove("%s/%s.fasta" %(out_path,name))
				if os.path.isfile("%s/%s.txt" %(wise_path,name)):
					os.remove("%s/%s.txt" %(wise_path,name))

	"""
	DATA_DIR = "zhen/frog_result"#input blast result path
	out_path = "frog_result"

	for filename in os.listdir(DATA_DIR):
		if os.path.isfile("%s/%s" %(out_path,filename)):
			os.remove("%s/%s" %(out_path,filename))
	"""
	print("sucessful!!")
def TMHMMoutput():
		#repeat it after read all file
		#read one protein in TMHMM
	class TMHMM:
	    def __init__(self,path,dirs):
		self.path = path
		self.dirs = dirs
	    def readprotein(self,path,dirs):
		proteinnumber = 0
		while proteinnumber<len(dirs):
		    f = open("protein/%s" %(dirs[proteinnumber]),'r+')
		    protein = f.read()
		    #cmd call TMHMM
		    TMHMM_info = os.system("cat protein/%s |./tmhmm-2.0c/bin/decodeanhmm -f ./tmhmm-2.0c/lib/TMHMM2.0.options -modelfile ./tmhmm-2.0c/lib/TMHMM2.0.model >TMHMM/%s" %(dirs[proteinnumber],dirs[proteinnumber]))
		    proteinnumber += 1
		    f.close()
	path = "protein/"
	dirs = os.listdir(path)   #Determines how many txt files this folder contains
	sequence = TMHMM(path,dirs)
	sequence.readprotein(path,dirs)
def checkv2r():
	#!/usr/bin/python
	import os, sys

	    
	class TMHMM:
	    def __init__(self,path,dirs):
		self.path = path
		self.dirs = dirs
	    def findall(self,path,dirs):
		# output all file                                       
		filenumber = 0
		#ok deviation-----------------------------------
		deviation = 0.00
		while filenumber<len(dirs):
		    f = open("TMHMM/%s" %(dirs[filenumber]),'r+')
		    zebrafish = f.read()                                      
		    #find all sequence-----------------------------------
		    start = zebrafish.find("%pred NB(0): ") +13
		    end = zebrafish.find("   ")
		    sequence = zebrafish[start:end]    
		    #sequence divide-----------------------------------
		    sequence = sequence.replace(", "," ")
		    sequence = sequence.split(" ")
		    #compare with fishV2R------------------------------
		    #if i,o,m order by m i m o m i m o m i m o m i t than start, check the range is right or not

		    #change number and string to int, 
		    #if is string need to provide base for number int([number | string[, base]]
		    i = 0
		    while i < len(sequence)-14 and i+41<len(sequence):
		        i = i+3
		        if sequence[i]=="M" and (int(sequence[i+2], 10)-int(sequence[i+1], 10)+1)<=23*(1+deviation) and (int(sequence[i+2], 10)-int(sequence[i+1], 10)+1)>=23*(1-deviation):
		            if sequence[i+3]=="i" and (int(sequence[i+5], 10)-int(sequence[i+4], 10)+1)<=13*(1+deviation) and (int(sequence[i+5], 10)-int(sequence[i+4], 10)+1)>=11*(1-deviation):
		                if sequence[i+6]=="M" and (int(sequence[i+8], 10)-int(sequence[i+7], 10)+1)<=23*(1+deviation) and (int(sequence[i+8], 10)-int(sequence[i+7], 10)+1)>=19*(1-deviation):
		                    if sequence[i+9]=="o" and (int(sequence[i+11], 10)-int(sequence[i+10], 10)+1)<=15*(1+deviation) and (int(sequence[i+11], 10)-int(sequence[i+10], 10)+1)>=13*(1-deviation):
		                        if sequence[i+12]=="M" and (int(sequence[i+14], 10)-int(sequence[i+13], 10)+1)<=23*(1+deviation) and (int(sequence[i+14], 10)-int(sequence[i+13], 10)+1)>=23*(1-deviation):
		                            if sequence[i+15]=="i" and (int(sequence[i+17], 10)-int(sequence[i+16], 10)+1)<=25*(1+deviation) and (int(sequence[i+17], 10)-int(sequence[i+16], 10)+1)>=15*(1-deviation):
		                                if sequence[i+18]=="M" and (int(sequence[i+20], 10)-int(sequence[i+19], 10)+1)<=22*(1+deviation) and (int(sequence[i+20], 10)-int(sequence[i+19], 10)+1)>=19*(1-deviation):
		                                    if sequence[i+21]=="o" and (int(sequence[i+23], 10)-int(sequence[i+22], 10)+1)<=26*(1+deviation) and (int(sequence[i+23], 10)-int(sequence[i+22], 10)+1)>=23*(1-deviation):
		                                        if sequence[i+24]=="M" and (int(sequence[i+26], 10)-int(sequence[i+25], 10)+1)<=24*(1+deviation) and (int(sequence[i+26], 10)-int(sequence[i+25], 10)+1)>=22*(1-deviation):
		                                            if sequence[i+27]=="i" and (int(sequence[i+29], 10)-int(sequence[i+28], 10)+1)<=12*(1+deviation) and (int(sequence[i+29], 10)-int(sequence[i+28], 10)+1)>=12*(1-deviation):
		                                                if sequence[i+30]=="M" and (int(sequence[i+32], 10)-int(sequence[i+31], 10)+1)<=24*(1+deviation) and (int(sequence[i+32], 10)-int(sequence[i+31], 10)+1)>=21*(1-deviation):
		                                                    if sequence[i+33]=="o" and (int(sequence[i+35], 10)-int(sequence[i+34], 10)+1)<=13*(1+deviation) and (int(sequence[i+35], 10)-int(sequence[i+34], 10)+1)>=8*(1-deviation):
		                                                        if sequence[i+36]=="M" and (int(sequence[i+38], 10)-int(sequence[i+37], 10)+1)<=23*(1+deviation) and (int(sequence[i+38], 10)-int(sequence[i+37], 10)+1)>=23*(1-deviation):
		                                                            if sequence[i+39]=="i" and (int(sequence[i+41], 10)-int(sequence[i+40], 10)+1)<=24*(1+deviation) and (int(sequence[i+41], 10)-int(sequence[i+40], 10)+1)>=13*(1-deviation):
		                                                                #The sequence of this protein was recorded as the fish V2R gene-----------------
		                                                                f_v2r = open("v2r.txt","a")
		                                                                f_v2r.write(dirs[filenumber]+"\n")
		                                                                f_v2r.close()
		                                                                #if TMHMM say it is V2R move it to TMHMMv2r
		                                                                copyTMHMM_is_v2r = os.system("cp protein/%s TMHMMv2r/%s" %(dirs[filenumber],dirs[filenumber]))
		                                                                first = sequence[i+1]
		                                                                last = sequence[i+41]
										name = zebrafish[1:(zebrafish.find("%len") -1)]									
										print(name+first+"to"+last+"is fishV2R")									
		    f.close()
		    filenumber += 1       
	path = "TMHMM/"
	dirs = os.listdir(path)   #Determines how many txt files this folder contains
	sequence = TMHMM(path,dirs)
	sequence.findall(path,dirs)
def merge():
	path = "TMHMMv2r/"
	file_data = os.listdir(path)
	fw = open("MTMHMMv2r.fasta", "w")
	result = ""
	for file in range(1, len(file_data), 1):
	    with open(path+file_data[file], "r") as fr:
		  sequence = fr.read()
		  result += sequence + "\n"
	fw.write(result)
	fw.close()
def del_file():
	if os.path.isfile("123h"):
		os.remove("123h")
	if os.path.isfile("brs.fasta"):
		os.remove("brs.fasta")
	if os.path.isfile("CMTMHMMv2r.fasta"):
		os.remove("CMTMHMMv2r.fasta")
	if os.path.isfile("hmake.fasta"):
		os.remove("hmake.fasta")
	if os.path.isfile("hmmmmake.fasta"):
		os.remove("hmmmmake.fasta")
	if os.path.isfile("hmmout.txt"):
		os.remove("hmmout.txt")
	if os.path.isfile("hmmout1.txt"):
		os.remove("hmmout1.txt")
	if os.path.isfile("hr.fasta"):
		os.remove("hr.fasta")
	if os.path.isfile("MTMHMMv2r.fasta"):
		os.remove("MTMHMMv2r.fasta")
	if os.path.isfile("v2r.fasta"):
		os.remove("v2r.fasta")
	if os.path.isfile("v2r.txt"):
		os.remove("v2r.txt")
	if os.path.isfile("new_score_list.txt"):
		os.remove("new_score_list.txt")
def clear_dir():
	if os.path.isdir("br"):
		shutil.rmtree("br")
	os.mkdir("br")
	if os.path.isdir("protein"):
		shutil.rmtree("protein")
	os.mkdir("protein")
	if os.path.isdir("TMHMM"):
		shutil.rmtree("TMHMM")
	os.mkdir("TMHMM")
	if os.path.isdir("TMHMMv2r"):
		shutil.rmtree("TMHMMv2r")
	os.mkdir("TMHMMv2r")
#--------------------------------------------------------------------------------

del_file()
clear_dir()
if not os.path.isdir("br"):
	os.mkdir("br")
q = raw_input("請輸入欲比對之物種檔案名稱\n")
d = raw_input("請輸入欲比對之基因檔案名稱\n")
if not os.path.isfile("b/"+q+".fa.nsq"):	
	os.system("makeblastdb -in b/"+q+".fa -dbtype nucl")
if not os.path.isfile("b/"+d+".fa.nsq"):
	os.system("makeblastdb -in b/"+d+".fa -dbtype nucl")
if not os.path.isfile(q+"e-10.txt"):
	os.system("tblastn -query b/"+ d +".fa -db b/"+q+".fa -out "+q+"e-10.txt -outfmt 10 -evalue 0.0000000001")
blast(d,q)
orf()
dts(d)
os.system("clustalo --infile hmmmmake.fasta --outfile hmake.fasta")
os.system("hmmbuild --amino 123h hmake.fasta")
os.system("hmmsearch -E 0.0000000001 --tblout hmmout.txt 123h brs.fasta")
ghmark()
hmmresult()
wise2(d)
wextend()
wdel_file()
dtp()
TMHMMoutput()
checkv2r()
merge()
os.system("clustalo --infile MTMHMMv2r.fasta --outfile CMTMHMMv2r.fasta")
os.system("megacc -a NJ_TJJ_right.mao -d CMTMHMMv2r.fasta -o Aresult.txt")
