#! /usr/bin/env python3

import sys

seq_file=sys.argv[1] #target is your input DNA sequence


with open(seq_file,"r") as fasta:
	for line in fasta:
		line=line.rstrip()
		if line.startswith(">"):
			header=line
		else:
			seq=""
			seq=seq+line

k_i=[1,2,3,4,5,6,7,8,9]
k_j=[1,10]

for i in k_i:
	for j in k_j:
		kmer_size=j*i
		target_size=len(seq)-(kmer_size-1)
		kmer_dict={}
		kmer_start=""
		output_file=open("merkat_"+str(kmer_size)+"_chr21_HSapiens.txt","w")
		for nt in range(0,target_size):
			kmer=seq[nt:nt+kmer_size]
			kmer_start=str(nt+1)
			if kmer not in kmer_dict:
				subdict={}
				kmer_start_list=[]
				kmer_start_list.append(kmer_start)
				subdict['count']=1
				subdict['position']=(kmer_start_list)
				kmer_dict[kmer]=subdict
			else:
				kmer_dict[kmer]['count']+=1
				kmer_dict[kmer]['position'].append(kmer_start)
    
		sorted_kmers = sorted(kmer_dict.keys(), key= lambda x: kmer_dict[x]['count'], reverse=True)
		
		for kmer in sorted_kmers:
			output_file.write(kmer+"\t"+str(kmer_dict[kmer]['count'])+"\t"+",".join(kmer_dict[kmer]['position'])+"\n")

		output_file.close()
		print("Wrote to file:","merkat_"+str(kmer_size)+"_chr21_HomoSapiens.txt")
