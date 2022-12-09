#Open list.txt in read mode
f = open("list.txt", "r")

#Open no.txt and web.txt in write mode
f1 = open("no.txt", "w")
f2 = open("web.txt", "w")

#Read each line in list.txt
for line in f:
    line=line.strip()
    #Check for empty lines in list.txt
    if line != '':
        #Split line with separator " " (space) 
        words = line.split(" ")
        #Save first word to no.txt
        f1.write(words[0] + "\n")
        #Save second word to web.txt
        f2.write(words[1] + "\n")

#Close all the files
f.close()
f1.close()
f2.close()
