import numpy as np
import matplotlib.pyplot as plt
import timeit

using_einsum = []
using_linalg_norm = []
N = np.linspace(1, 100_000, 100)
repeats = 1000

for i in N:
    n = int(i)
    print(n)

    # EINSUM
    SETUP_CODE = 'import numpy as np'

    TEST_CODE = f'''
A = np.random.rand({n},3)
np.sqrt(np.einsum('ij,ij->i', A, A))'''

    time = timeit.timeit(setup = SETUP_CODE, 
                        stmt = TEST_CODE, 
                        number = repeats)

    # print('EINSUM\n', times)
    using_einsum.append(1_000*time/repeats)


    # LINALG NORM
    SETUP_CODE = 'import numpy as np'

    TEST_CODE = f'''
A = np.random.rand({n},3)
np.linalg.norm(A, axis=1)'''

    time = timeit.timeit(setup = SETUP_CODE, 
                        stmt = TEST_CODE, 
                        number = repeats)

    # print('LINALG NORM\n', times)
    using_linalg_norm.append(1_000*time/repeats)


# Plot
plt.plot(N, using_einsum, label='using einsum')
plt.plot(N, using_linalg_norm, label='using linalg norm')
plt.xlabel('n')
plt.ylabel('execution time [ms]') # mu: \u03BC
plt.legend()
plt.show()