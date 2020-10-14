Dict_Employee = {}
Dict_Customer = {}

def readFile():
    rfile = open("data.txt")
    for lines in rfile:
        lines = lines.rstrip()
        if lines.startswith("e"):
            employee(lines)
            continue
        elif lines.startswith("c"):
            customer(lines)
            continue
        elif lines.startswith("t"):
            transcation(lines)
            continue

def employee(empData):
    empData = empData.split()
    empID = empData[1]
    Dict_Employee[empID] = empData[2]

def customer(custData):
    custData = custData.split()
    custID = custData[1]
    Dict_Customer[custID] = {'custName': custData[2], 'custAmt': float(custData[3])}

def transcation(transData):
    transData = transData.split()
    cuidToken = transData[1]
    empidToken = transData[2]
    transMode = transData[3]
    transAmt = float(transData[4])
    fileOutput(cuidToken, empidToken, transMode, transAmt)

def fileOutput(cToken, eToken, tMode, tAmt):
    cName = Dict_Customer[cToken]["custName"]
    eName = Dict_Employee[eToken]
    totalAmt = 0
    if tMode == 'w':
        tMode = '-'
        totalAmt = Dict_Customer[cToken]["custAmt"] - tAmt
    elif tMode == 'd':
        tMode ='+'
        totalAmt = Dict_Customer[cToken]["custAmt"] + tAmt

    print('{} {} {}${:.2f} ${:.2f}'.format(cName, eName, tMode, tAmt, totalAmt))

def numLoop():
    count = 0
    while count < 6:
        i = 1
        while i <= 10:
            print(i % 10, end="")
            i += 1
        count += 1
        
        
numLoop()
print('')
readFile()