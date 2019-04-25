blue    = 23 + 1
red     = 43
purple  = 33
eggs    = [blue,red,purple]

def fuse(eggs):
    new_eggs = [egg-1 for egg in eggs]
    new_eggs[eggs.index(min(eggs))] = min(eggs)+1
    return new_eggs

def sum(eggs):
    sumtin = 0
    for egg in eggs:
        sumtin += egg
    return sumtin

print(eggs)
while sum(eggs) > 1:
    eggs = fuse(eggs)
    print(eggs)