import pandas as pd
import random 
with open("data/shakespere.txt",'r',encoding="latin-1") as f:
    lines = f.readlines()

sonnets = []
current_sonnet = []
current_RN = "" #Current roman numeral


#Part 1
for line in lines:
    line = line.strip()

    romanNum = True
    for i in line:
        if i not in "IVXLCDM":
            romanNum = False
            break
    if romanNum == True:
        if current_RN and current_sonnet:
            sonnets.append({current_RN:current_sonnet})
            current_sonnet = []
        current_RN = line
    elif line: 
        if len(current_sonnet) < 14:
            current_sonnet.append(line)
if current_RN and current_sonnet:
    sonnets.append({current_RN:current_sonnet})

for sonnet in sonnets:
    for rn,lines in sonnet.items():
        print(f"{rn} : {lines[0]}\n")


# Part 2

allLines = {}
lineNum = 0

for i in sonnets:
    for j in i:
        lines = i[j]
        for k in lines:
            allLines[f"{j}{lineNum}"] = k
            lineNum+=1
print("\nNext sonnet\n")
for i in range(14):
    random_key = random.choice(list(allLines.keys()))
    print(allLines[random_key])
    