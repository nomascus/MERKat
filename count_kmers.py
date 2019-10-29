#!/usr/bin/env python3
#script to search for kmers of various lengths within genome of interest 

with open("ecoli_refseq_genome.fna","r") as file_obj:
	for line in file_obj:
		line=line.rstrip()
		for j in (0,1,2,3,4):	
			for i in (1,2,3,4,5,6,7,8,9):
				kmer_length=i*(10**j)
				outfile='kmer'+str(kmer_length)+'.out'
				kmer_out = open(outfile,"w")
				kmer_dict={}
				for start_pos in range(0,len(line) - kmer_length + 1):
					end_pos = start_pos + kmer_length
					kmer=line[start_pos:end_pos]
					if kmer not in kmer_dict:	
						sub_dict={}
						#when making new key value, need to put name into quotes if hasn't already been defined
						sub_dict['count']=1
						position_list = []
						position=str(start_pos)
						#position_tuple =(start_pos, end_pos)
						position_list.append(position)
						sub_dict['positions']=position_list
						#make sub-dictionaries and populate first, then put into main dictionary
						kmer_dict[kmer]=sub_dict
					else:	
						kmer_dict[kmer]['count']+=1
						position=str(start_pos)
						#position_tuple =(start_pos, end_pos)
						kmer_dict[kmer]['positions'].append(position)
						#need to put count in quotes again because it only exists within the dictionary. Not a defined variable outside of dict)
				#for below: all of the information is getting stored in kmer_dict each time, and want to write each set of kmer_dict info to new outfile
				#creating list of all kmers and sorting by how many each has
				sorted_kmers = sorted(kmer_dict.keys(), key= lambda x: kmer_dict[x]['count'], reverse=True)
				for key in sorted_kmers:
					kmer_out.write(key+"\t"+ str(kmer_dict[key]['count'])+"\t"+("\t".join(kmer_dict[key]['positions']))+"\n")
				kmer_out.close()
