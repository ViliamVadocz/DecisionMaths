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
    Generate Hadamard matrix but with
        -1 as 1,
        1 as 0.
    """
    return  np.abs((H(n) - 1) / 2)

def M2(n):
    """
    Generate Hadamard matrix but with
        -1 as 0,
        1 as 1.
    """
    return  (H(n) + 1) / 2

def reed_muller_img(n):
    """
    Create image of Reed Muller code.
    """
    img = Image.fromarray(M2(n).astype('uint8') * 255)
    img.save('reed-muller.png')
    img.show()

def hamming_dis(a, b):
    """
    Find the Hamming distance between a and b.
    """
    count = 0
    for i in range(len(a)):
        if a[i] != a[i]:
            count += 1
    return count

### ### ### ### ### ### ### ### ### ### ### ### ###

# Generate Reed-Muller code for 256 bit data.
reed_muller = M(8)

# Message to send (example img)
data = np.asarray(Image.open('test_img.png'))

# Convert to Reed-Muller code.
origin_bits = np.empty((data.shape[0]*data.shape[1]*data.shape[2], 256), dtype='uint8')
i = 0
for row in data:
    for pixel in row:
        for colour in pixel:
            origin_bits[i] = reed_muller[colour]
            i += 1

# Corrupt per pixel code.
corrupt_bits = origin_bits.copy()
max_mistakes = 100
for code in corrupt_bits:
    # Randomise number of mistakes.
    for i in range( int(np.random.rand(1)*(max_mistakes+1)) ):
        # Flip a bit at a random position.
        position = int(np.random.rand(1)*len(code))
        code[position] += 1
        code[position] %= 2

# Reconstruct message.
# FIXME
reconstruction = np.empty_like(corrupt_bits.shape[0])
for i, code in enumerate(corrupt_bits):

    # Find closest.
    closest = 0
    lowest_dis = 256
    for ii, row in enumerate(reed_muller):
        dis = hamming_dis(code, row)
        if dis < lowest_dis:
            closest = ii
            lowest_dis = dis

    # Replace with closest.
    reconstruction[i] = closest

# Create image
reconstruction = reconstruction.reshape(data.shape)
img = Image.fromarray(reconstruction)
# img.save('test_img_reconstructed.png')
img.show()