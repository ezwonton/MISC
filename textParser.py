import os


os.chdir("E:\School Work\Misc\Python")
print os.getcwd()
fileLoc = r"E:\School Work\Misc\Python\Syrylo_Nick_Wan_Eric.txt"
print fileLoc

fileInfo = open(fileLoc, "r")
text = []
for line in fileInfo:
    if line == ("\n"):
        pass
    else:
        if line.__contains__("\n"):
            text.append(line[:line.find("\n")])

print text

for line in text:
    print line