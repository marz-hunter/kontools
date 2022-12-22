# reading the contents of file1
with open('file1.txt') as f1:
    data1 = f1.read()

# reading the contents of file2
with open('file2.txt') as f2:
    data2 = f2.read()

# separating the words of file1
words1 = data1.split()

# separating the words of file2
words2 = data2.split()

# combining the words of both the files
combined_words = []
for word1 in words1:
    for word2 in words2:
        combined_words.append(word1+word2)

# writing the combined words to a new file
with open('combined.txt', 'w') as f3:
    for word in combined_words:
        f3.write(word + "\n")
