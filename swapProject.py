def swapData():
    file1 = input("Enter the file path of file1: ")
    file2 = input("Enter the file path of file2: ")
    with open(file1, 'r') as a:
        fileData1 = a.read()
    with open(file2, 'r') as a:
        fileData2 = a.read()
    with open(file1, 'w') as a:
        a.write(fileData2)
    with open(file2, 'w') as a:
        a.write(fileData1)

swapData()
