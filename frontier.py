optima = set()
optima.add((2, 60))
optima.add((3, 30))
optima.add((6, 20))

def test_solution(solution):
    global optima
    if solution in optima:
        print(f"already an optimum {solution}")
        return
    for optimum in optima:
        for new, old in zip(solution, optimum):
            if new < old:
                break
        else:
            # it is not better in any property
            print(f"{solution} is worse than {optimum}")
            break
    else:
        # solution is better in at least some way
        print(f"new optimum {solution}")
        optima.add(solution)
    # print(optima)

test_solution((4, 25))
test_solution((4, 25))
test_solution((5, 30))
test_solution((5, 20))
test_solution((1, 100))
test_solution((10, 80))
test_solution((10, 10))
