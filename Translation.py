def translation():#Translation and proteinchain preperation
    n=Fragments.index("TAC")
    for q in range (n):
        Fragments.pop(n-1)
        n=n-1
               
    for i in range (len(Fragments)):
        a= Fragments[i]
        if a in ["ATT","ATC","ATA"]:
            protein_chain.append("Isoleucine")
        elif a in ["CTT", "CTC", "CTA", "CTG", "TTA", "TTG"]:
            protein_chain.append("Leucine")
        elif a in ["GTT", "GTC","GTA", "GTG"]:
            protein_chain.append("Valine")
        elif a in ["TTT","TTC"]:
            protein_chain.append("Phenylalanine")
        elif a in ["ATG"]:
            protein_chain.append("Methionine")
        elif a in ["TGT","TGC"]:
            protein_chain.append("Cysteine")
        elif a in ["GCT","GCC","GCA","GCG"]:
            protein_chain.append("Alanine")
        elif a in ["GGT","GCC","GGA","GGG"]:
            protein_chain.append("Glycine")
        elif a in ["CCT","CCC","CCA","CCG"]:
            protein_chain.append("Proline")
        elif a in ["ACT","ACC","ACA","ACG"]:
            protein_chain.append("Threonine")
        elif a in ["TCT","TCC","TCA","TCG"]:
            protein_chain.append("Serine")            
        elif a in ["TAT","TAC"]:
            protein_chain.append("Thyrosine")
        elif a in ["TGG"]:
            protein_chain.append("Tryptophan")
        elif a in ["CAA","CAG"]:
            protein_chain.append("Glutamine")
        elif a in ["AAT","AAC"]:
            protein_chain.append("Asparagine")
        elif a in ["CAT","CAC"]:
            protein_chain.append("Histadine")
        elif a in ["GAA","GAG"]:
            protein_chain.append("Glutamic acid")
        elif a in ["GAT","GAC"]:
            protein_chain.append("Aspartic acid")
        elif a in ["AAA","AAG"]:
            protein_chain.append("Lysine")
        elif a in ["CGT","CGC","CGA","CGG","AGA","AGG"]:
            protein_chain.append("Arganine")
        elif a in ["TAA","TAG","TGA"]:
            print("Code terminated, Output protein chain is: \n")
            return protein_chain


#**************************************************************************************************************************************************************************
dnastrand=str(input("Enter the genetic DNA code with initiator codon ACT "))#Enter as along single string of code
genome=dnastrand.upper()
List = list(genome)
Times = 0 
Letters = ""
Fragments = []
for Letter in enumerate(genome):
    Times+=1
    Letters += Letter[1]
    if Times == 3: 
        Fragments.append(Letters) 
        Letters = ""
        Times = 0
    elif Letter[0]+1 == len(genome):
        Fragments.append(Letters)
print(Fragments)
protein_chain=[]




#**************************************************************************************************************************************************************************
x="TAC"
if x in Fragments:
    translation()
else:
    print("No initiator codon found")
print(protein_chain)










