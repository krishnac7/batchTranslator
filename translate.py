import os
from mtranslate import translate
items = os.listdir(".")
newlist = []
directory="translated"
if not os.path.exists(directory):
    os.makedirs(directory)
for names in items:
    if names.endswith(".txt"):
        newlist.append(names)
master = open(os.path.join(directory,"master.txt"),"a+")
for files in newlist:
    with open(files) as f:
        content = f.readlines()
        content = [x.strip() for x in content]
        completeName = os.path.join(directory, "Hindi_"+files)
        with open(completeName, "a+") as myfile:
            for line in content:
                if line is not '':
                    translated = translate(line, 'hi').encode('utf-8')
                    myfile.write("\n"+translated)
                    master.write(line+":"+translated+"\n")
            print("translated "+files)
master.close()
