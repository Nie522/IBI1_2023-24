'''
1.Input files: 
Read SLC6A4 sequence of different species
2.Compare each amino acid: 
Find score of each amino acid
If the corresponding element is the same, it usually gets a positive score; 
If different, a negative score is obtained based on the BLOSUM62 matrix
3.Print output: 
Print Seq1 name/sequence
Print Seq2 name/sequence
Print Seq3 name/sequence
Print Scores
'''
import pandas as pd

df = pd.read_csv('BLOSUM62.csv', index_col=0, header=0)
# Using pandas to read the csv file; By default, it is separated by commas
# The first column is used as the row index, the first row is used as the column index

blosum62 = df.to_dict('index')
# Transform the DataFrame into a dictionary, value corresponding to each index is another dictionary

def calculate_score(seq1, seq2, blosum62_matrix):
    score = 0
    min_len = min(len(seq1), len(seq2))
    # Ensure the two sequences are in the same length
    for i in range(min_len):
        aa1, aa2 = seq1[i], seq2[i]
        score += blosum62_matrix.get(aa1, {}).get(aa2, 0)
    # Define the calculate measures
    return score

with open('SLC6A4_HUMAN.fa') as f:
    human_seq = ''.join([line.strip() for line in f if line[0] != '>'])

with open('SLC6A4_MOUSE.fa') as f:
    mouse_seq = ''.join([line.strip() for line in f if line[0] != '>'])

with open('SLC6A4_RAT.fa') as f:
    rat_seq = ''.join([line.strip() for line in f if line[0] != '>'])
# Read sequence files and remove possible non-sequence lines (such as headings)

score1 = calculate_score(human_seq, mouse_seq, blosum62)
score2 = calculate_score(human_seq, rat_seq, blosum62)
score3 = calculate_score(mouse_seq, rat_seq, blosum62)
# Calculatee BLOSUM62 scores

print(f"The BLOSUM62 score for human-mouse sequence alignment is: {score1}")
print(f"The BLOSUM62 score for human-rat sequence alignment is: {score2}")
print(f"The BLOSUM62 score for mouse-rat sequence alignment is: {score3}")