'''
from Bio import SeqIO
def read_fasta(fasta_file):
    return SeqIO.parse(fasta_file, "fasta")
fasta_file_path='Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa.gz'
for record in read_fasta(fasta_file_path):
    print(f"Title: {record.id}")
    print(f"Sequence: {record.seq}")
'''
#The code above is used to read the original file

import re
cdna=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
#Open the file as cdna
cdna_dict={}
sequence=[]
inside_key=False
current_key=None
#Initialise the dictionary and variables
for line in cdna:
    line=line.strip()
    #Read the cdna and cut the last newline symbols
    if line.startswith(">"):
        if current_key and sequence:
        #If the function have a sequence now, write to dictionary
            name=line.split()[0]
            #Split the first word
            cdna_dict[name]=''.join(sequence)
            #Use the first word as key
            sequence=[]
            #Initialise the sequence
        current_key=line
        #Update the current_key
        inside_key=True
    elif inside_key:
        sequence.append(line)
        #Sum up the sequence lines
cdna.close()
#Close cdna file
if current_key and sequence:
    cdna_dict[current_key]=''.join(sequence)
#Only when the current_key(current line) and sequence aren't empty, these rows can be executed
output='duplicate_genes.fa'
with open(output, 'w') as output_file:
    for key,sequence in cdna_dict.items():
        output_file.write(f'{key}\n{sequence}\n')
#Write the key and sequence into output file
print(f'The duplicate genes have been written to {output}')