def SchreibeWerte(W_W,W_A,W_R,W_G):
    f = open("Kal.wrt","w")
    f.write("")
    f.close()
    f = open("Kal.wrt","a")
    f.write("WHITE")
    for i in range(len(W_W)):
        STR = "\n" + str(W_W[i])
        f.write(STR)
    f.write("\nOUTER")
    for i in range(len(W_A)):
        STR = "\n" + str(W_A[i])
        f.write(STR)
    f.write("\nRED")
    for i in range(len(W_R)):
        STR = "\n" + str(W_R[i])
        f.write(STR)
    f.write("\nGREEN")
    for i in range(len(W_G)):
        STR = "\n" + str(W_G[i])
        f.write(STR)
    f.close()

def LadeWerte(S_W,S_A,S_R,S_G):
    f = open("Kal.wrt","r")
    lines = f.readlines()
    CSensor = S_W
    CSensorNum = 0
    for line in lines:
        if line == "WHITE":
            CSensor = S_W
        elif line == "OUTER":
            CSensor = S_A
        elif line == "GREEN":
            CSensor = S_G
        elif line == "RED":
            CSensor = S_R
        else:
            if CSensorNum == 0:
                CSensor.miniL = int(line)
                CSensorNum += 1
            elif CSensorNum == 1:
                CSensor.maxiL = int(line)
                CSensorNum += 1
            elif CSensorNum == 0:
                CSensor.miniR = int(line)
                CSensorNum += 1
            else:
                CSensor.maxiR = int(line)
                CSensorNum = 0