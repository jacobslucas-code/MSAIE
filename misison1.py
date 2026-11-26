import sys


def manifest_dictionary(file):
    crates=[]
    with open(file) as f:
        for line in f:
            if no line: continue
            else:
                type,weight=line.split(',')
                crates.append((type,weight))
    return crates

def totals(crates,limit):
    total={}
    totalweight=0
    for type,weight in crates:
        total[type]=total.get(type,0)+weight
        totalweight+=weight
    return total

print(manifest_dictionary(file))
print(totals(crates,limit))


