import random

def load_txt_file(filename):
    with open(filename,'r',encoding='latin-1') as f:
        lines = f.readlines()

    return lines

lines = load_txt_file('data/shakespere.txt')

def parse_sonnets(lines):
    sonnets = []    #hold parsed sonnets
    current_sonnet = {} #temp dictionary for current sonnet
    current_RN = None   #roman numeral id for sonnet
    current_lines = []  #list of lines for current sonnet
    

    for line in lines:
        line = line.strip()     #remove whitespace

        if not line:
            continue    #skip empty line

        is_romannum = True 
        #check if line is a roman numeral 
        for char in line:
            if char not in "IVXLCDM":
                is_romannum = False
                break
        
        if is_romannum:
            #saves sonnet before parsing new one
            if current_RN and current_lines:
                current_sonnet[current_RN] = current_lines
                sonnets.append(current_sonnet)
                current_sonnet={}
                current_lines=[]
            current_RN = line #starts new sonnet with roman numeral
        else:
            current_lines.append(line)  #add line to current sonnet

    #save last after loop ends
    if current_RN and current_lines:
        current_sonnet[current_RN] = current_lines
        sonnets.append(current_sonnet)

    return sonnets

def print_sonnets(sonnets):
    for sonnet in sonnets:
        for num in sonnet:
            lines = sonnet[num]
            print(f"{num}:{lines[0]}") #print roman numeral and it's first line

lines = load_txt_file("data/shakespere.txt")
sonnets = parse_sonnets(lines)
print_sonnets(sonnets)

def make_sonnet(sonnets):
    all_lines_dict = {} #new dictionary

    line_id = 0
    for sonnet in sonnets:
        for key in sonnet:
            lines = sonnet[key]
            for line in lines:
                #creates key using sonnet number and  line id
                all_lines_dict[f"{key}{line_id}"] = line
                line_id = line_id + 1
    
    print("\nNew Sonnet\n")
    for i in range(14):
        #randomly select 14 lines for new sonnet
        random_key = random.choice(list(all_lines_dict.keys()))
        print(all_lines_dict[random_key])

make_sonnet(sonnets)