#>Rosalind_99
dna="CCCGGCTCACTAAACTAAGATAAAGACGTAGGCCATCCGCGTGTCATCTCGGCATCCCGCCGGAGGAGGGCGTCGATGGGCTACCTGTACTGTTGACGTAGGATTGGTGCTTATGGTGACGGTGAATATGGTCCATCGGGCCACTTACTTTCTGAGTTAAGGTGGAACTCCCCAATGTGAGCCCCTGACGGCATAGGCTCTTGTCTGGACTTGTAGCGATATCTGGGGTTTCGCACTTTTCTTTCCTAGTCCCAGCGTATGAAGCCCTTAATGGTCTATCTAGGTCTGTTGGAGCTACCCACTTTTGAATTCAACTTCCGCGGCAAGTTTCACATTCTGATTGCCAGCCACTAGTTCTGGAACACTGTGGAGATAATAGCTATTCTGGAGTTAATTTGCCTCGTTCCCCTACGCTATGAAGGTTGGGGAGAGGCCATAGAGGAAGTCCGCCCGTGCTAAATGAGAAGTCAAGCGCGCATGCAGCTCGGTTCAGCTTAGCTAAGCTGAACCGAGCTGCATCCTCCCTGCACTTCTGGACCAGGAAACTGCTTGAGGCATGGAGACCGACTATATGCCGGAGGAAACTAGTATCCTTCTCTGCAATCCCCAGTCCAGTACCGATCCTTCCTTGTACCTTGGTCCACCTCAAATACAAGGATGTTTTGGCACGCATAGTTTCGTGCTATTCGTTTAACTATGTGGAGGTACTAAGTAATAGGTTTTTAATCAATGACCAATGATCTAACCATAGCAATTCACTTAAATCTTATTTTCAGAGCTTGTGTCAGATCCGACTAGCCACATTAGACTCCTAAATGGTGATTGCCACTCCTTTTGTACCCCAAATTCTGGTATCATAATTCACAGAAGTGTTCTTCGCACGCCGGCTATGATTCGTTTACCGAGTTTGGACGGTTTCAGAATTGCTATGGGTGAATCGGTACTCAGTGAAGTACTTTCGCGGACATTAGTAGACACGACTCTCGGCCTTCGATG"
# f =open(r'C:\SelfLearn\Rosalind\Bioinformatics_stronghold\rosalind_orf.txt')
'''
Given: A DNA string s of length at most 1 kbp in FASTA format.
Return: Every distinct candidate protein string that can be translated from ORFs of s. Strings can be returned in any order.
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
# print read_fasta("rosalind_orf.txt")

codons={'TTT': 'F','CTT':'L','ATT':'I','GTT':'V','TTC':'F','CTC':'L','ATC':'I',
'GTC':'V','TTA':'L','CTA':'L', 'ATA':'I', 'GTA': 'V',
'TTG':'L',     'CTG':'L'     ,'ATG':'M'  ,   'GTG':'V',
'TCT':'S',     'CCT':'P'     ,'ACT':'T',     'GCT': 'A',
'TCC':'S' ,    'CCC':'P'   ,  'ACC':'T',      'GCC':'A',
'TCA':'S'  ,   'CCA':'P'  ,   'ACA':'T'    , 'GCA':'A',
'TCG':'S'   ,  'CCG':'P' ,    'ACG':'T'   ,  'GCG': 'A',
'TAT':'Y'   ,  'CAT':'H',     'AAT':'N'  ,   'GAT':'D',
'TAC':'Y'   ,  'CAC':'H'    , 'AAC':'N' ,    'GAC':'D',
'TAA':' '  , 'CAA':'Q'    , 'AAA':'K',     'GAA': 'E',
'TAG':' '  , 'CAG':'Q'   ,  'AAG':'K',      'GAG' :'E',
'TGT':'C'   ,  'CGT':'R'  ,   'AGT':'S'     ,'GGT': 'G',
'TGC':'C'  ,   'CGC':'R' ,    'AGC':'S'    , 'GGC': 'G',
'TGA':' ' ,  'CGA':'R',     'AGA':'R'   ,  'GGA':'G',
'TGG':'W'    , 'CGG':'R'    ,  'AGG':'R'  ,   'GGG':'G' }

def reverse_complement(dna):
  dna=dna.replace('A','t')
  dna=dna.replace('G','c')
  dna=dna.replace('T','a')
  dna=dna.replace('C','g')
  dna=dna[::-1].upper()
  return dna
# rc_dna=reverse_complement(dna)

def orfs(dna):
  orfs=[]
  orfs+=dna,dna[1:],dna[2:]
  rc_dna=reverse_complement(dna)
  orfs+=rc_dna,rc_dna[1:],rc_dna[2:]
  return(orfs)

# print(len(orfs(dna)))

def translate(dna):
  seqs=orfs(dna)
  # print(seqs)
  pro_seqs=[]
  for seq in seqs:
    # print(seq)
    # pro_seq=''
    for i in range(0,len(seq)-2,3):
      if  seq[i:i+3]=='ATG':
        pro_seq='M'
        for i in range(i+3,len(seq)-2,3):
          if codons[seq[i:i+3]]==' ':
            # pro_seq=pro_seq+'!'
            break
          elif seq[i:i+3] in codons:
            pro_seq=pro_seq+codons[seq[i:i+3]]
            # print(pro_seq)
        pro_seqs.append(pro_seq)
    # pro_seq=''
  return(list(set(pro_seqs)))

dna = dna.replace("\n",'')
# print(translate(dna))

# for i in translate(dna):
#   print(i)
# # print(read_fasta("rosalind_orf.txt"))
for dna in read_fasta("rosalind_orf.txt").values():
  for i in translate(dna):
    print(i)

      