DNA = "ATGATCTCGTAA"
RNA = ""


for nucleotideo in DNA:
    if nucleotideo == "A":
        RNA += "U";
    elif nucleotideo == "T":
        RNA += "A";
    elif nucleotideo == "G":
        RNA += "C";
    elif nucleotideo == "C":
        RNA += "G";


print(RNA)