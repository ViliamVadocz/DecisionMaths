import matplotlib.pyplot as plt
import numpy as np
from nltk.corpus import words
word_list = words.words()

count = np.zeros((26,2))

# Add up all the first letters.
total_letters = 0
for word in word_list:
    count[ord(word[0].upper()) - 65, 0] += 1

    for letter in word:
        count[ord(letter.upper()) - 65, 1] += 1
        total_letters += 1

# Calculate the percentages.
percentages = np.empty_like(count)
percentages[:,0] = count[:,0] / len(word_list)
percentages[:,1] = count[:,1] / total_letters

# Plotting.
fig, ax = plt.subplots()
width = 1
x = np.linspace(0,2.5*width*26,26)
rects1 = ax.bar(x - width/2, percentages[:,0], width = width, label = 'First letter')
rects2 = ax.bar(x + width/2, percentages[:,1], width = width, label='Frequency')
# The actual reason I made this was to find out how many pages
# to dedicate to each letter in my 40-page notebook for new words.
#rects3 = ax.bar(x, 40 * percentages[:,0]) 
ax.set_xticks(x)
ax.set_xticklabels([chr(letter+65) for letter in range(26)])
ax.set_title('Percentage of Words Beginning with each Letter Compared to its Frequency')
ax.legend()
plt.show()
