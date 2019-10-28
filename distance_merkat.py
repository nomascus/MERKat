#!/usr/bin/env python3

import sys

merkat_file=sys.argv[1]

with open(merkat_file,"r") as merkat:
	for line in merkat:
		line=line.rstrip()
		kmer, count, positions = line.split("\t")
		positions_list=positions.split(",")
		positions_list_rev=positions_list[::-1]
		differences=[]
		for i in range(0,len(positions_list_rev)-1):
			diff=int(positions_list_rev[i])-int(positions_list_rev[i+1])
			differences.append(diff)
		print(kmer,differences)
