from DNAToolkit import *
import random


rndDNAStr = ''.join([random.choice(nucleotides)
                   for nuc in range(50)])
print(validateSeq(rndDNAStr))


DNAStr = validateSeq(rndDNAStr)
print(countNucFrequency(DNAStr))


