def SchreibeWerte(sensoren):
    f = open("Kal.wrt","w")
    f.write("")
    f.close()
    f = open("Kal.wrt","a")
    STR = ""
    for s in sensoren:
        STR += str(s.miniL) + "\n"
        STR += str(s.maxiL) + "\n"
        STR += str(s.miniR) + "\n"
        STR += str(s.maxiR) + "\n"
    print(STR)
    f.write(STR)
    
    f.close()

def LadeWerte(sensoren):
    f = open("Kal.wrt","r")
    print("Deine Mudda")
    lines = f.readlines()
    for i in range (len(sensoren)):
        sensoren[i].miniL = int(lines[i * 4])
        sensoren[i].maxiL = int(lines[i * 4 +1])
        sensoren[i].miniR = int(lines[i * 4 +2])
        sensoren[i].maxiR = int(lines[i * 4 +3])
    
        