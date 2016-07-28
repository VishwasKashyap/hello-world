import sys
import re

with open("out.txt","wt") as fout:
    with open("random.txt","rt") as fin:
        for line in fin:
            fout.write(line.replace("\n",""))

with open("out.txt","wt") as fout:
    with open("out.txt","wt") as fin:
        for line in fin:
            fout.write(line.replace(">",">\n")
