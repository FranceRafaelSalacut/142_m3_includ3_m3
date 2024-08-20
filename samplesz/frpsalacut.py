'''
online resources: 
https://stackoverflow.com/questions/31624041/print-n-or-newline-characters-as-part-of-the-output-on-terminal
https://stackoverflow.com/questions/40647881/skipping-blank-lines-in-read-file-python

'''

from icecream import ic

def readFile(fileName: str):
    with open(fileName, "r") as file:
        for line in file:
            if not line.strip():
                continue
            line = line.replace("\n", "")
            if("#include" in line):
                #print(line)
                readFile(line.split(" ")[1].replace('"', ''))
            else:
                print(line)

def main():
    #fileName = input("")
    #print(fileName)

    inputs = ("inputFile1.in", "inputFile2.in", "inputFile3.in")

    readFile(inputs[0])

main()