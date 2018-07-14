import re
tfile="C:\\Users\\lius39\\Documents\\Code\\pdf2htmlEX-win32-0.14.6-upx-with-poppler-data\\go29527_acrf_testing.html"
lines=open(tfile,'r').readlines()
flen=len(lines)
p11=re.compile(r'(<div class=")(\w) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+)(">)')
import csv
with open("C:\\Users\\lius39\\Documents\\project\\GO29527\\entimICE\\doc\\acrf.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter = ',')
    for row in readCSV:
        a=row[1]
        b=row[2]
        searchl='(<div class=["|\w|\s|\d]+>)('+a+')((</*span[\s|\w|=|_|"]*>[\s|\w|=]*)+)(</div>)'
        for i in range(flen):
            for m in re.finditer(searchl, lines[i]):
                sstr=m.group(1)+m.group(2)+m.group(3)+m.group(5)
                m1=re.search(p11,m.group(1))
                p1=m1.group(1)+m1.group(2)+' '+m1.group(3)+' '+'x8'+' '+m1.group(5)+' '+m1.group(6)+' '+m1.group(7)+' '+m1.group(8)+' '+m1.group(9)+' '+m1.group(10)+' '+m1.group(11)+' '+m1.group(12)+m1.group(13)+b+'</div>'
                rstr=sstr+p1
                lines[i]=lines[i].replace(sstr,rstr)
open(tfile,'w').writelines(lines)