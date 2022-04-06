# 结合hunjun的code分析轨迹
ls1=[]

with open ("./fragtable") as f1:
    lines=f1.readlines()

for i in lines[-1].rsplit()[2:]:
    if int(i)> 0:
        ls1.append((lines[0].rsplit()[lines[-1].rsplit().index(i)]))

for i in ls1:
    if 'C6' in i:
        while i in ls1:
            ls1.remove(i)

with open("./rxn.log") as f2:
    lines=f2.readlines()

for line in lines:
    if ':' not in line:
        continue
    for j in ls1:
        if 'C6' in ls1:
            continue
        if j in line.split('::')[1]:
           print(line)
