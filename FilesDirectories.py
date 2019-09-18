from pathlib import Path
p = Path("C:\\Learning6\\io_example\\sample1.txt")
p1 = Path("C:\\Learning6\\io_example\\test")
p2 = Path("C:\\Learning6\\io_example")
print(p.is_dir())
print(p.is_file())
print(p.name)
print(p.exists())
print(p.is_absolute())
# print(p1.mkdir(0))
# print(p2.glob('*.*'))
for file in p2.glob('*.*'):
    print(file)                         # will show only files not directory
for file in p2.glob('*'):
    print(file)                         # will show all files and directories
