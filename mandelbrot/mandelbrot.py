import numpy as np
from PIL import Image
import sys

# Size and area to explore.
left = -2
top = -2
size = 4

# Resolution.
resolution = 4096
max_count = 255
arr = np.empty((resolution, resolution, 3), dtype=np.uint8)

# Progress bar.
bar_width = 50
sys.stdout.write(f'[{" " * bar_width}]')
sys.stdout.flush()
sys.stdout.write("\b" * (bar_width + 1)) # return to start of line, after '['
progress = 0

for i in range(resolution):
    for ii in range(resolution):
        # Reset count.
        count = 0
        # Find the c for this point.
        imag = top + i*size/resolution
        real = left + ii*size/resolution
        c = np.complex(real, imag)
        # Reset z.
        z = 0 + 0j

        # Repeat z*z + c until it escapes or reaches limit.
        while count < max_count:
            z = z*z + c
            # Check whether the magnitude of z has gone above 2.
            if np.absolute(z) > 2: break
            count += 1

        # Set the colour by count.
        # TODO Make a colour function.
        arr[i, ii, :] = count
    
    # Update the progress bar.
    if i > progress*(resolution/bar_width):
        progress += 1
        sys.stdout.write(u'\u2588')
        sys.stdout.flush()

# End the progress bar.
sys.stdout.write("]\n")

# Save and show the image.
print('Saving image...')
mandelbrot = Image.fromarray(arr, 'RGB')
mandelbrot.save('mandelbrot.png')
mandelbrot.show()