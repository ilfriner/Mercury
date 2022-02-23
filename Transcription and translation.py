def translation():#Translation and proteinchain preperation
    n=Fragments.index("UAC")
    for q in range (n):
        Fragments.pop(n-1)  #Pops off the TAC sequence
        n=n-1
               
    for i in range (len(Fragments)):
        a= Fragments[i]
        if a in ["AUU","AUC","AUA"]:
            protein_chain.append("Isoleucine")
        elif a in ["CUU", "CUC", "CUA", "CUG", "UUA", "UUG"]:
            protein_chain.append("Leucine")
        elif a in ["GUU", "GUC","GUA", "GUG"]:
            protein_chain.append("Valine")
        elif a in ["UUU","UUC"]:
            protein_chain.append("Phenylalanine")
        elif a in ["AUG"]:
            protein_chain.append("Methionine")
        elif a in ["UGU","UGC"]:
            protein_chain.append("Cysteine")
        elif a in ["GCU","GCC","GCA","GCG"]:
            protein_chain.append("Alanine")
        elif a in ["GGU","GCC","GGA","GGG"]:
            protein_chain.append("Glycine")
        elif a in ["CCU","CCC","CCA","CCG"]:
            protein_chain.append("Proline")
        elif a in ["ACU","ACC","ACA","ACG"]:
            protein_chain.append("Threonine")
        elif a in ["UCU","UCC","UCA","UCG"]:
            protein_chain.append("Serine")            
        elif a in ["UAU","UAC"]:
            protein_chain.append("Thyrosine")
        elif a in ["UGG"]:
            protein_chain.append("Tryptophan")
        elif a in ["CAA","CAG"]:
            protein_chain.append("Glutamine")
        elif a in ["AAU","AAC"]:
            protein_chain.append("Asparagine")
        elif a in ["CAU","CAC"]:
            protein_chain.append("Histadine")
        elif a in ["GAA","GAG"]:
            protein_chain.append("Glutamic acid")
        elif a in ["GAU","GAC"]:
            protein_chain.append("Aspartic acid")
        elif a in ["AAA","AAG"]:
            protein_chain.append("Lysine")
        elif a in ["CGU","CGC","CGA","CGG","AGA","AGG"]:
            protein_chain.append("Arganine")
        elif a in ["UAA","UAG","UGA"]:
            print("Code terminated, Output protein chain is: \n")
            return protein_chain


#**************************************************************************************************************************************************************************
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

    RNAstrand=""
    for line in genome:
        RNAstrand += line
    print(RNAstrand)
    return RNAstrand

    

        


dnastrand=str(input("Enter the genetic code "))#Enter as along single string of code
dna=dnastrand.upper()
Dna=list(dna)   #converts to list
Dna_sequence=[]
genome=[]
for i in (Dna):
    Dna_sequence.append(i) #For converting from DNA to RNA



#produces codon triplets

List = list(dnatorna())
Times = 0    #Starts at 0 count
Letters = ""    #Starts with no letters
Fragments = []  #Fragment list in empty
for Letter in enumerate(List):
    Times+=1
    Letters += Letter[1]
    if Times == 3: 
        Fragments.append(Letters) 
        Letters = ""
        Times = 0
    elif Letter[0]+1 == len(genome):
        Fragments.append(Letters)
print(Fragments)
print(len(Fragments))
protein_chain=[]




#**************************************************************************************************************************************************************************
x="UAC"
if x in Fragments:
    translation()
else:
    print("No initiator codon found")
print(protein_chain)









