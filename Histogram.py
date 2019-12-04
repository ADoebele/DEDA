import numpy as np
from collections import Counter
import matplotlib.pyplot as plt


#Filter the most common ten words:
word_list = [item for sublist in magazin_list for item in sublist]
counts = dict(Counter(word_list).most_common(10))
labels, values = zip(*counts.items())

#Sort values by decending order:
indSort = np.argsort(values)[::-1]

#Rearrange the data:
labels = dict.keys(counts)
values = np.array(values)[indSort]
indexes = np.arange(len(labels))
bar_width = 0.3

#Plot the results:
plt.bar(indexes, values)
plt.xticks(indexes + bar_width, labels, size=7)
plt.title("Most frequent Words in Bitcoinmagazin")
plt.savefig("btc_Hist_2.png",transparent=True)
plt.show()
