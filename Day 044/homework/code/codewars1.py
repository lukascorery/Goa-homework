"""https://www.codewars.com/kata/5556282156230d0e5e000089/train/python"""

def dna_to_rna(dna):
    rna = ""
    for acid in dna:
        if acid == "T":
            rna += "U"
        else:
            rna += acid
    return rna