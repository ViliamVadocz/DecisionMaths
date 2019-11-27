import numpy as np
from PIL import Image

def cartesian_product(X, Y):
    x_m = X.shape[0]
    x_n = X.shape[1]
    y_m = Y.shape[0]
    y_n = Y.shape[1]
    arr = np.empty((x_m * y_m, x_n * y_n))
    for row in range(x_m):
        for col in range(x_n): 
            if X[row,col] == 1:
                arr[row*y_m : (row+1)*y_m, col*y_m : (col+1)*y_m] = Y
            elif X[row,col] == -1:
                arr[row*y_m : (row+1)*y_m, col*y_m : (col+1)*y_m] = -Y
            else:
                print("I don't know what is supposed to happen.")
    return arr

# Generate the Hadamard matrices.
H1 = np.array([
    [ 1,  1],
    [ 1, -1]
])

def H(n):
    """
    Generate Hadamard matrix.
    """
    if n == 1: return H1
    return cartesian_product(H(n-1), H1)

def M(n):
    """
    Generate Hadamard matrix and replace all -1 with 1 and 1 with 0.
    """
    return  np.abs((H(n) - 1) / 2)

def M2(n):
    return  (H(n) + 1) / 2

reed_muller = M(5)
    
test = M2(5).astype('uint8') * 255

print(reed_muller)
print(test)

Reed_Muller = Image.fromarray(test)
Reed_Muller.save('reed-muller.png')
Reed_Muller.show()
    