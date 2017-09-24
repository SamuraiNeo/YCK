import data
def ptable():
    adt = ""
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
    line5 = ""
    line6 = ""
    line7 = ""
    for i in range(len(data.period1)):
        if(len(data.period1[i]) == 2):
            ad = 2
        elif(len(data.period1[i]) == 1):
            ad = 3
        elif(len(data.period1[i]) == 0):
            ad = 4
        for j in range(ad):
            adt = adt + " "
        line1 = line1 + (data.period1[i] +ad)

    for i in range(len(data.period2)):
        if(len(data.period2[i]) == 2):
            ad = 2
        elif(len(data.period2[i]) == 1):
            ad = 3
        elif(len(data.period2[i]) == 0):
            ad = 4
        for j in range(ad):
            adt = adt + " "
        line2 = line2 + (data.period2[i] +ad)

    for i in range(len(data.period3)):
        if(len(data.period3[i]) == 2):
            ad = 2
        elif(len(data.period3[i]) == 1):
            ad = 3
        elif(len(data.period3[i]) == 0):
            ad = 4
        for j in range(ad):
            adt = adt + " "
        line3 = line3 + (data.period3[i] +ad)

    for i in range(len(data.period4)):
        if(len(data.period4[i]) == 2):
            ad = 2
        elif(len(data.period4[i]) == 1):
            ad = 3
        elif(len(data.period4[i]) == 0):
            ad = 4
        for j in range(ad):
            adt = adt + " "
        line4 = line4 + (data.period4[i] +ad)

    for i in range(len(data.period5)):
        if(len(data.period5[i]) == 2):
            ad = 2
        elif(len(data.period5[i]) == 1):
            ad = 3
        elif(len(data.period5[i]) == 0):
            ad = 4
        for j in range(ad):
            adt = adt + " "
        line5 = line5 + (data.period5[i] +ad)

    for i in range(len(data.period6)):
        if(len(data.period6[i]) == 2):
            ad = 2
        elif(len(data.period6[i]) == 1):
            ad = 3
        elif(len(data.period6[i]) == 0):
            ad = 4
        for j in range(ad):
            adt = adt + " "
        line6 = line6 + (data.period6[i] +ad)

    for i in range(len(data.period7)):
        if(len(data.period7[i]) == 2):
            ad = 2
        elif(len(data.period7[i]) == 1):
            ad = 3
        elif(len(data.period7[i]) == 0):
            ad = 4
        for j in range(ad):
            adt = adt + " "
        line7 = line7 + (data.period7[i] + ad)
    print(line1)
    print(line2)
    print(line3)
    print(line4)
    print(line5)
    print(line6)
    print(line7)
