import nltk

##Clean text data from Bitcoin magazin:

#Split sentences into words:
from nltk.tokenize import word_tokenize
nltk.download('punkt')
tokenized_sents = [word_tokenize(i) for i in content_list]
print(tokenized_sents[:100])

#Remove all tokens that are non alphabetic:
magazin_list = []
for article in tokenized_sents :
    alpha = [word for word in article if word.isalpha()]
    magazin_list.append(alpha)

#Convert to lower case:
magazin_list = [[words.lower() for words in article] for article in magazin_list]


#Filter out stopwords:
from nltk.corpus import stopwords
nltk.download('stopwords')
stop_words = stopwords.words('english')
print(stop_words)
count=0
for article in magazin_list :
    count += 1
    print(count)
    non_stops = [w for w in article if not w in stop_words]
    magazin_list[count-1] = non_stops

#Additional stopwords from McDonald:
#Stopwords consisting of dates and numbers:
dates = list(open('StopWords_DatesandNumbers.txt','r'))
dates_str = "".join(str(dates))
dates = dates_str.lower()
dates = dates.replace('\\n','')

magazin_list_L = []
count = 0
for article in magazin_list :
    count += 1
    print(count)
    non_stops = [w for w in article if not w in dates]
    magazin_list[count-1] = non_stops
    magazin_list_L.append(len(non_stops))

#More stopwords from McDonald:
more_w = list(open('StopWords_Generic.txt','r'))
more_str = "".join(str(more_w))
more_w = more_str.replace('\\n','')
more_w = more_w.lower()
count = 0
for article in magazin_list :
    count += 1
    print(count)
    non_stops = [w for w in article if not w in more_w]
    magazin_list[count-1] = non_stops



