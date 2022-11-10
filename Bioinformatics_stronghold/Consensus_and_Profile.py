import numpy as np

# f=open("rosalind_cons.txt")
def read_fasta(file):
	seq = {}
	fp = open(file, 'r')
	for line in fp:
		if line.startswith('>'):
			name = line.replace('>', '')
			name = name.replace('\n', '')
			seq[name] = ''
		else:
			seq[name] += line.replace('\n', '')
	fp.close()
	return seq

q=read_fasta("rosalind_cons.txt")
# print(seq.values())
seqs=list(q.values())
col_len=len(seqs[0])
row_len=len(seqs)
matrix=np.zeros(shape=(4,col_len),dtype=int)
consensus=''
nuc=["A","T","G","C"]
for a in range(col_len):
    pos=[s[a] for s in seqs]
    # print(max(pos,key=pos.count))
    consensus+=max(pos,key=pos.count)
    for b in range(len(nuc)):#b is for rows #a columns
        # print(a,b)
        matrix[b][a]=pos.count(nuc[b])

print(consensus)
# print(matrix)
for i in range(len(nuc)):
    print(nuc[i]+":"," ".join([str(j) for j in matrix[i]]))

