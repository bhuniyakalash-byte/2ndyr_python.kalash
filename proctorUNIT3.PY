import string

counts = {}

# Read and count word frequencies
with open("input.txt", "r", encoding="utf-8") as f:
    for word in f.read().lower().split():
        w = word.strip(string.punctuation)
        if w:
            counts[w] = counts.get(w, 0) + 1

# Write the sorted frequencies to the output file
with open("output.txt", "w", encoding="utf-8") as f:
    for word, count in sorted(counts.items()):
        f.write(f"{word}: {count}\n")
