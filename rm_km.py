#!/usr/bin/env python3

import sys

dis_file=sys.argv[1]

with open(dis_file,"r") as disfile:

	for line in disfile:
		line=line.rstrip()
		kmer,count,dist=line.split("\t")
		dist_list1=[]
		dist_list2=[]
		dist_list1=dist.split(",")
		for i in dist_list1:
			if int(i) > len(kmer):
				dist_list2.append(i)
		print(kmer, "\t",len(dist_list2)+1,"\t",dist_list2)
			 
				
