file1 = open("C:\\Learning6\\io_example\\sample1.txt", "a")
file1.write(" Sample Text")
file1.close()

file1 = open("C:\\Learning6\\io_example\\sample1.txt")
print(file1.read())
print(file1.readline())
print(file1.name)
print(file1.mode)
print(file1.closed)
file1.close()
print(file1.closed)

with open("C:\\Learning6\\io_example\\sample1.txt") as f:
    for line in f:
        print(line)
