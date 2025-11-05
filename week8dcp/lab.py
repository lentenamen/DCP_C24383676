# Open and read the file
with open('data/aceventura.txt', 'r', encoding='latin-1') as f:
    lines = f.readlines()

word_counts = {}

def clean_word(word):
    """Remove punctuation and lowercase the word."""
    for ch in [",", "`", "’", "?", "!", "\n", ".", ":", ";", "'"]:
        word = word.replace(ch, "")
    return word.lower().strip()

def add_to_model(sentence):
    """Add words from a sentence to the word count dictionary."""
    global word_counts
    words = sentence.split()
    for word in words:
        clean = clean_word(word)
        word_counts[clean] = word_counts.get(clean, 0) + 1

# Go through each line and process
for line in lines:
    add_to_model(line)

def print_word_counts():
    """Print all words and their counts."""
    for key, value in word_counts.items():
        print(f"{key}: {value}")

# Print all words and counts
#print_word_counts()

top_10 = sorted(word_counts.items(), key=lambda x: x[1]

print("Top 10 most frequent words:\n")
for word, count in top_10:
    print(f"{word}: {count}")
