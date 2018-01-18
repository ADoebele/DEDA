import re
import nltk
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
import string

cdir = os.getcwd()

article_str = "".join(str(content_list))

'''
split the resulting string into words and clean up the resulting string
'''

#split into words
from nltk.tokenize import word_tokenize
nltk.download('punkt')
tokens = word_tokenize(article_str)
print(tokens[:100])

#remove all tokens that are not alphabetic
words = [word for word in tokens if word.isalpha()]
print(words[:100])
#convert to lower case
words = [w.lower() for w in words]

#filter out stopwords
from nltk.corpus import stopwords
nltk.download('stopwords')
stop_words = stopwords.words('english')
print(stop_words)
words = [w for w in words if not w in stop_words]
stopwords.add("would","also","one")
words = [w for w in words if not w in more_stopwords]
print(words[:100])

#Combine words to stem words
from nltk.stem.porter import PorterStemmer
porter = PorterStemmer()
stemmed = [porter.stem(word) for word in words]
print(stemmed[:100])
words = [w for w in words if not w in stemmed]
print(words[:100])



'''
Basic statistics
'''


'''
Histogram of words
'''

#Only the most frequent n words are observed
counts = dict(Counter(words).most_common(200))
labels, values = zip(*counts.items())

#Sort the values by decending order
indSort = np.argsort(values)[::-1]

#Rearrange your data
labels = np.array(labels)[indSort]
values = np.array(values)[indSort]

indexes = np.arange(len(labels))

bar_width = 0.35

plt.bar(indexes, values)

plt.xticks(indexes + bar_width, labels)
plt.show()




'''
word could
'''

from wordcloud import WordCloud
from PIL import Image

btc_string = "".join(str(words))

def wordcloud(text,image):

    picture = np.array(Image.open(image))

    wc = WordCloud(background_color = "white",
                   mask = picture,
                   max_words = 150)
    wc.generate_from_frequencies(text)

    wc.to_file("btc_wordcloud.jpg")


wordcloud(counts)





btc_text = open('btc_text.txt', 'w')
btc_text.write(article_str)
btc_text.close()