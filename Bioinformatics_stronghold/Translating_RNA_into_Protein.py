f=open(r"C:\SelfLearn\Rosalind\Bioinformatics_stronghold\rosalind_prot.txt")
rna=f.read()
codons={'AUU':'I','AUC':'I', 'AUA':'I',
            'CUU':'L','CUC':'L','CUA':'L','CUG':'L','UUA':'L','UUG':'L','GUU':'V','GUC':'V','GUA':'V','GUG':'V',
            'GCU':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A','CGU':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R','AGA':'R', 'AGG':'R',
            'AAA':'K', 'AAG':'K','AAU':'N', 'AAC':'N',
            'AUG':'M','GAU':'D', 'GAC':'D',
            'UUU':'F','UUC':'F',
            'UGU':'C', 'UGC':'C',
            'CCU':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
            'CAA':'Q', 'CAG':'Q',
            'UCU':'S', 'UCC':'S', 'UCA':'S', 'UCG':'S', 'AGU':'S','AGC':'S',
            'GAA':'E', 'GAG':'E',
            'ACU':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
            'GGU':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G',
            'UGG':'W',
            'CAU':'H', 'CAC':'H',
              'UAU':'Y', 'UAC':'Y',
              'AUU':'I', 'AUC':'I', 'AUA':'I',
              'GUU':'V', 'GUC':'V', 'GUA':'V', 'GUG':'V',
              'UAG':' ', 'UGA':' ', 'UAA':' '}
pro_seq=""
for i in range(0,len(rna)-2,3):
        a=rna[i:i+3].upper()
        if a not in codons.keys():
          print("Invalid rna coding sequence at codon",a,"position=",i)
          break
        elif codons[a]==' ':
          print("stop codon",a,"at pos",i)
          break
        else:
          pro_seq=pro_seq+codons[a]
print(pro_seq)