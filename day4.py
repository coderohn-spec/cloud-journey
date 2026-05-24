f = open("day1.py", "r")
content = f.read()
print(content)
f.close()

f = open("day1.py", "a")
f.write("\nprint('Day 4 added this line')")
f.close()

f = open("day1.py", "r")
content = f.read()
print(content)
f.close()