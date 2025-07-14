"""https://www.codewars.com/kata/554e4a2f232cdd87d9000038/train/python"""
def DNA_strand(dna):
    # code here
    DNA = ""
    for string in dna:
        if string == "A":
            DNA +="T"
        elif string == "T":
            DNA +="A"
        elif string == "G":
            DNA +="C"
        elif string == "C":
            DNA +="G"
    return DNA