import re
gene = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
repeat = input("Please input your repeat sequence ('GTGTGT' or 'GTCTGT'): ")
if repeat not in ['GTGTGT', 'GTCTGT']:
    repeat = input("Please input 'GTGTGT' or 'GTCTGT': ")
output_filename = f"{repeat}_duplicate_genes.fa"
#Create the output file
repeat_count = 0
#Let the count be zero at first
with open(output_filename, "w") as outfile:
    gene_name = None  #Initialise gene name
    sequence = ""  #Initialise sequence
    for line in gene:
        if line.startswith(">"):
            if gene_name:
            #Only be executed when the gene_name is not "None"
                repeat_count = sequence.count(repeat)
                #Count the repeat times
                outfile.write(f"{gene_name} repeats {repeat_count}\n")
                #Write the results in the output file
            gene_name = line.strip().split()[0]
            sequence = ""
            #Reset the gene name and sequence
            repeat_count = 0
            #Reset the counting results
        else:
            sequence += line.strip()
    if gene_name and sequence:
        if re.search(repeat, sequence):
            repeat_count += 1
            outfile.write(f"{gene_name} repeats {repeat_count} times\n")
    #Identify last gene sequence (because only encountering next">" the gene can be identified)
print(f"The results have been written in {output_filename}")
#Remind the user that all the code has been executed