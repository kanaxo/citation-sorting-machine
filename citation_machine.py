
while True:
    filename = input("Please enter path to file: ")
    filename = str(filename)
    try:
        oldCitations = open(filename,'r')
        break
    except:
        print("please try again. Note: Do take out the string literals!")

#read lines and put into list
values = []
for line in oldCitations:
    val = line.strip('\n')
    values.append(val)
values.sort()
oldCitations.close()
print("oldCitations done")

#create new file
x = filename.split('/')
try:
    newCitations = open("/".join(x[:-1]) + "/" + "newcitations.txt","w+") #overwrite or create new file
except:
    newCitations = open("newcitations.txt","w+") #if oldCitation file is read in same directory as program
for citation in values:
    newCitations.write(citation + "\n")

newCitations.close()
print("new citations created")
