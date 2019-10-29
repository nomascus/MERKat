import random
import math
big_randos=0
counts=[]
random_counts=[]
kmers=[]
with open("/Users/info/PFB2019_ALB/kmers/outfiles/kmer10.out","r") as f:
	for line in f:
		line=line.strip()
		splitLine=line.split("\t")
		kmer=splitLine[0]
		count=splitLine[1]
		count=int(count)
	#	count=count.replace("'","")
		counts.append(count)
		kmers.append(kmer)
sample_size=math.floor(.1*len(counts))
sample_size_str=str(sample_size)
num_digits=len(sample_size_str)-1
format_str = "{:." + str(num_digits) + 'f' + "}"
for i in range(1,sample_size):
	random_counts.append(random.choice(counts))	
for j in range(0,len(counts)):
	for k in random_counts:
		if k > counts[j]:
			big_randos +=1
	p_val=big_randos/sample_size
	print(kmers[j], format_str.format(p_val))
	big_randos=0
#print(counts)
