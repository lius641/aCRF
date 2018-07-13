"""import csv
with open("C:\\Users\\lius39\\Desktop\\test.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter = ',')
    for row in readCSV:
        print(row[0])
        
        
import re        
def modifyip(tfile,sstr,rstr):
    try:
        lines=open(tfile,'r').readlines()
        flen=len(lines)
        for i in range(flen):
            if sstr in lines[i]:
                lines[i]=lines[i].replace(sstr,rstr)
        open(tfile,'w').writelines(lines)
    except Exception as e:
        print(e)

modifyip("C:\\Users\\lius39\\Documents\\Code\\test.txt","and","A111")"""

"""
import re
text = '<div class=\"t m0 xc h2 y14 ff1 fs0 fc0 sc0 ls0 ws0\">SITE<span class=\"_ _43\"> </span>Site<span class=\"_ _26"> </span>BRAIN =</div>'
m = re.search('(<div class=\"t)\s(\w+)\s(\w+)\s(\w+)\s(\w+)\s(\w+)\s(\w+)\s(\w+)\s(\w+)\s(\w+)\s(\w+)\">(\w+)<(.*)(</div>)', text)
if m:
    fp = m.group(1)
    fend = m.group(14)
    rstr = m.group(1) + ' ' + m.group(2) + ' ' + m.group(3) + ' ' + m.group(4) + ' ' + m.group(5) + ' ' + m.group(6) + ' ' + m.group(7) 
    print(rstr)
"""


"""
import re
text = '<div class=\"t m0 xc h2 y14 ff1 fs0 fc0 sc0 ls0 ws0\">SITE<span class=\"_ _43\"> </span>Site<span class=\"_ _26"> </span>BRAIN =</div>'
m = re.search('(<div class=["|\w|\s|\d]+>)([\s|\w\d]+)((</*span[\s|\w|=|_|"]*>[\s|\w|=]*)+)(</div>)', text)
if m:
    p1=m.group(1)
    p2=m.group(2)
    p3=m.group(3)
    p4=m.group(4)
    p5=m.group(5)
    print(p1)
    print(p2)
    print(p3)
    print(p4)
    print(p5)
    print(p1+p2+p3+p5)"""
    
import re
lines=open("C:\\Users\\lius39\\Documents\\Code\\test.txt",'r').readlines()
flen=len(lines)
for i in range(flen):
    for m in re.finditer('(<div class=["|\w|\s|\d]+>)([\s|\w\d]+)((</*span[\s|\w|=|_|"]*>[\s|\w|=]*)+)(</div>)', lines[i], re.S):
        p1=m.group(1)
        p2=m.group(2)
        p3=m.group(3)
        p4=m.group(4)
        p5=m.group(5)
        print(p1+p2+p3+p5)
        
        
        
        