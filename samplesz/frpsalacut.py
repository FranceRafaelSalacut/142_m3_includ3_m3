'''
online resources: 
https://stackoverflow.com/questions/31624041/print-n-or-newline-characters-as-part-of-the-output-on-terminal
https://stackoverflow.com/questions/40647881/skipping-blank-lines-in-read-file-python

'''

from icecream import ic

def readFile(fileName: str, fileNames: "list" = []) :
    with open(fileName, "r") as file:
        for line in file:
            if not line.strip():
                continue
            line = line.replace("\n", "")
            if("#include" in line):
                #print(line)
                newFileName = line.split(" ")[1].replace('"', '')
                if newFileName in fileNames:
                    continue
                fileNames.append(newFileName)
                readFile(newFileName, fileNames)
            else:
                print(line)

def main():
    #fileName = input("")
    #print(fileName)

    inputs = ("inputFile1.in", "inputFile2.in", "inputFile3.in")

    readFile(inputs[2])

main()