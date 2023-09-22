def parseCSV(file):
    with open(file, "r") as f:
        CSVtable = []
        for i,v in enumerate(f.readlines()):
            currentLine = v.split(",")
            for w,x in enumerate(currentLine):
                currentLine[w] = x.strip("\n")
            CSVtable.append(currentLine)
        return CSVtable

CSV = parseCSV("C:/Users/miles/Desktop/Sean's Coding/Python/CSVFunction/ExampleCSV.csv")

for i in range(len(CSV)):
    print(CSV[i][0],CSV[i][2],CSV[i][2])