no = []
web = []

# Read the words from the files
with open('no.txt', 'r') as file1:
    for line in file1:
        no.append(line.strip())

with open('web.txt', 'r') as file2:
    for line in file2:
        web.append(line.strip())

# Loop through the words in each list
for word1, word2 in zip(no, web):
    url = "https://web.archive.org/web/{}if_/{}".format(word1, word2)
    print(url)
