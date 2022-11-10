import requests as r
import re
# a="Q640N1"

'''
def getUniProteinFromFasta(id):
    #Access the Uni Protein Website
    uniProtWebsite = "http://www.uniprot.org/uniprot/%s.fasta" % id
    webResponse = urllib2.urlopen(uniProtWebsite)
    mainPage = webResponse.read()'''
# def find_motif_
f=open(r"rosalind_mprt.txt")
w=open(r"rosalind_mprt_fasta.txt",'w')
f=f.readlines()
for a in f:
    a=a.replace("\n",'') 
    b=re.search(r'([OPQ][0-9][A-Z0-9]{3}[0-9]|[A-NR-Z][0-9]([A-Z][A-Z0-9]{2}[0-9]){1,2})',a)
    seq=r.get("https://rest.uniprot.org/uniprotkb/"+b.group()+".fasta")
    # print(seq.text)
    w.write(seq.text)
w.close()


# with open(r"rosalind_mprt_fasta.txt") as f:
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
seq=read_fasta("rosalind_mprt_fasta.txt")
# print(seq.values())



'''  Will be able to find Overlapping motifs  Will tweak it later'''
motif = re.compile(r"(?=N[^P][ST][^P])")
for k,i in seq.items():
    out=''
    for o in re.finditer(motif,i):
        out=out+' '+str(o.start()+1)
    if out!='':
        j=re.search(r'([OPQ][0-9][A-Z0-9]{3}[0-9]|[A-NR-Z][0-9]([A-Z][A-Z0-9]{2}[0-9]){1,2})',k)
        print(j.group().strip())
        print(out.lstrip('  '))
