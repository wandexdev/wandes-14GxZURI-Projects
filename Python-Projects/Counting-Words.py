
file = open("myfile.txt", "r")
with open("myfile.txt","r") as fil:
        fil.close()
count = 0
for line in file:
        words = line.split()
        count += len(words)
file.close()
print("Number of words in a Text file: ", count)
