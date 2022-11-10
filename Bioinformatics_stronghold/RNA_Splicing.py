
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

def translateDna(dna,introns):
  prot=''
  for intron in introns:
    # print(intron)
    dna=dna.replace(intron,"")
    # print(len(dna))
  for i in range(0,len(dna)-2,3):
    if codons[dna[i:i+3]]==' ':
      break
    else:
      prot=prot+codons[dna[i:i+3]]
  print(prot)

seq=read_fasta('rosalind_splc.txt')
# dna,introns=str(seq.values()[0]),list(seq.values()[1:])
seqs=list(seq.values())
dna,introns=seqs[0],seqs[1:]

translateDna(dna,introns)
# print(introns)