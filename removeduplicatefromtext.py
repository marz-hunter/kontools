#open the two files
with open("list.txt") as f1, open("delete.txt") as f2:
    #create empty list to store words from file
    list_words = []
    delete_words = []
    #loop through each file, read and store in respective lists
    for line1 in f1:
        for word1 in line1.split():
            list_words.append(word1)
    for line2 in f2:
        for word2 in line2.split():
            delete_words.append(word2)
    #loop through the list_words to delete words in delete_words list
    for word in delete_words:
        while word in list_words:
            list_words.remove(word)

#open a new file to write the words after deletion
with open("after_deletion.txt", "w") as f3:
    #write the remaining words to the new file
    for word in list_words:
        f3.write(word + "\n")
