def dnatorna():
    for n in Dna_sequence:
        if n in ["A"]:
            genome.append("U")
        elif n in ["T"]:
            genome.append("A")
        elif n in ["G"]:
            genome.append("C")
        elif n in ["C"]:
            genome.append("G")
    print(genome)


dnastrand=str(input("Enter the genetic code "))#Enter as along single string of code
dna=dnastrand.upper()
Dna=list(dna)
Dna_sequence=[]
genome=[]
for i in (Dna):
    Dna_sequence.append(i)#For converting from DNA to RNA
dnatorna()





