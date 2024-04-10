import re
seq='ATGCAATCGGTGTGTCTGTTCTGAGAGGGCCTAA'
count=0
if re.search('GTGTGT',seq):
    count=count+1
if re.search('GTCTGT',seq):
    count=count+1
print("The total number of repeat elements is ",count)