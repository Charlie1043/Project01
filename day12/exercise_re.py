import re

file = open("exc.txt", "r")
pattern1 = r"\n\n"
# pattern1 = r"(\n\n.+\n*\s+\w+\s+)+"
pattern2 = r"(\w{4}\.){2}\w{4}"
lines = re.split(pattern1, file.read())
regex1 = re.compile(pattern1)
regex2 = re.compile(pattern2)
# obj1 = regex1.findall(file.read())
lines.remove(lines[0])
port_needed = input("请输入端口名称：")
pattern3 = "%s$" % port_needed
print(pattern3)
regex3 = re.compile(pattern3)
print(regex3)
for line in lines:
    obj1 = regex3.search(line.split(" ")[0])
    obj2 = regex2.search(line)
    # print(obj1, obj2)
    if obj1:
        print(obj2.group())



# print(lines)
# count = 0
# for line in lines:
#     # print(line)
#     count += 1
# print(count)




