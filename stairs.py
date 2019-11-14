def num_ways(stairs : int, step_variants : list = [1,2]):
    if stairs == 0: return 1

    ways = 0
    for variant in step_variants:
        if stairs >= variant:
            ways += num_ways(stairs - variant, step_variants)
            
    return ways

def num_ways_bottom_up(stairs : int, step_variants : list = [1,2]):
    if stairs == 0: return 1
    
    solutions = [1]
    for i in range(1, stairs+1):
        ways = 0
        for variant in step_variants:
            if i >= variant:
                ways += solutions[i - variant]
        solutions.append(ways)

    return solutions[stairs]

variants = [1,2,5]
for i in range(10):
    print(num_ways(i, variants), num_ways_bottom_up(i, variants))
    