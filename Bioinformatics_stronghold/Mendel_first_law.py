'''Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.

Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.'''
homoDominant=19
heterozygous=24
homoRecessive=21
total=homoDominant+heterozygous+homoRecessive

dominantTotal = homoDominant/total
heterozygousDominantTotal = (heterozygous/total) * ((homoDominant/(total-1)) + (heterozygous-1)/(total-1) * 0.75 + ((homoRecessive/(total-1)) * 0.5))
domHeterRecesTotal = (homoRecessive/total) * (homoDominant/(total-1) + heterozygous/(total-1) * 0.5)
completeProbablity = dominantTotal + heterozygousDominantTotal + domHeterRecesTotal

print(completeProbablity)
