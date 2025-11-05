with open('data/aceventura.txt','r',encoding='latin-1') as f:
        lines = f.readlines()

word_counts={}

def clean_word(word):
    for ch in [",", "`", "’", "?", "!", "\n", ".", ":", ";", "'"]:
        word = word.replace(ch,"")
    return word.lower().strip()

def add_to_model(sentence):
    global word_counts
    words = sentence.split(" ")
    for i in words:
        clean = clean_word(i)
        if clean: #skips empty string
            word_counts[clean] = word_counts.get(clean,0)+1
    
for line in lines:
    add_to_model(line)

def print_word():
    for key,value in word_counts.items():
        print(f"{key}:{value}")   

#print_word()

top_10 = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:10]

print("Top 10 most frequent words:\n")
for word, count in top_10:
    print(f"{word}: {count}")



def extract_characters(lines):
    characters = []
    skip = {"EXT", "INT", "CONT'D", "DAY", "NIGHT", "FADE IN", "FADE OUT", "DISSOLVE TO","CUT TO", "CLOSE UP", "WIDE SHOT", "ANGLE ON", "BACK TO", "FLASHBACK", "MONTAGE","SUPER", "BLACK", "TITLE", "END", "THE END", "SMASH CUT", "MATCH CUT", "SERIES OF SHOTS"}
    for line in lines:
        stripped = line.strip()
        if stripped.isupper() and not any(word in stripped for word in skip):
            if stripped not in characters:
                characters.append(stripped)
    
    return characters

#doesn't work
#for name in extract_characters(lines):
#    print(name)

def count_lines_foreach(lines):
    characters = extract_characters(lines)
    line_counts = {char:0 for char in characters}
    current_speaker = None

    for line in lines:
        stripped =  line.strip()
        if stripped in characters:
            current_speaker = stripped
        elif current_speaker:
            line_counts[current_speaker] +=1 

    return line_counts

line_counts = count_lines_foreach(lines)

topchar = sorted(line_counts.items(),key=lambda x:x[1],reverse=True)[0]

print("\nMost lines spoken")
print(f"{topchar[0]}:{topchar[1]} lines")