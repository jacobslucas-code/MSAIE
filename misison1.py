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

def totals(file,limit):
    crates=manifest_dictionary(file)
    total={}
    totalweight=0
    for type,weight in crates:
        total[type]=total.get(type,0)+weight
        totalweight+=weight
    if totalweight>limit:
        print('Limit exceeded')
    return total

print(manifest_dictionary(file))
print(totals(crates,limit))


