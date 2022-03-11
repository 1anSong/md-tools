"""
It needs rdf.xvg and rdf_cn.xvg
plot rdf and rdf_cn using rdf.xvg and rdf_cn.xvg which produce by gromacs 
"""

import matplotlib.pyplot as plt

frame=[]
rdf_number=[]
cnrdf_number=[]

with open('rdf.xvg') as rdf:
    for line in rdf:
        if line[0] == '#':
            continue
        if line[0] == '@':
            continue
        frame.append(float(line.strip().split()[0]))
        rdf_number.append(float(line.strip().split()[1]))

with open ('rdf_cn.xvg') as cn_rdf:
    for line in cn_rdf:
        if line[0] =="#":
            continue
        if line[0] =="@":
            continue
        cnrdf_number.append(float(line.strip().split()[1]))

if len(frame) > len(cnrdf_number):
    cnrdf_number.insert(0,float(0))

fig=plt.figure()
ax1=fig.add_subplot()
ax1.plot(frame,rdf_number,color="black",label="g(r)")
ax1.set_xlabel("nm")
ax1.set_ylabel("g(r)")

ax2=ax1.twinx()
ax2.plot(frame,cnrdf_number,color="red",label="G(r)")
ax2.set_ylabel("G(r)")

ax1.legend(bbox_to_anchor=(0.5,1))
ax2.legend(bbox_to_anchor=(0.5,0.9))
fig.savefig("rdf.png")
