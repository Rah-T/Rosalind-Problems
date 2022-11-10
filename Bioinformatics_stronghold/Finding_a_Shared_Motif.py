'''
sequences={"Rosalind_1":"GATTACA","Rosalind_2":"TAGACCA","Rosalind_3":"ATACA"}
'''
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
sequences=read_fasta("rosalind_lcsm.txt")
seq=list(sequences.values())
def Shortestseq(seq):
    m=len(seq[0])
    for i in seq:
        if len(i)<m:
            short=i
        else:
            short=seq[0]
    return short
# print(Shortestseq(seq))
short=Shortestseq(seq)
def k_mers(short,k_mer_min_len=2):
    k_mer=[]
    k=k_mer_min_len
    for i in range(0,len(short)):
        for j in range(i+k,len(short)+1):
            if short[i:j] !=None:
                # print(short[i:j])
                k_mer.append(short[i:j])
    return k_mer
# print(k_mers(short))
k=k_mers(short)


def shared_motif(seq,k):
    motif=[]
    for i in k:
        for s in seq:
            if i not in s:
                break
        else:
            motif.append(i)
    return motif
print(max(shared_motif(seq,k),key=len))
# print((shared_motif(seq,k)))