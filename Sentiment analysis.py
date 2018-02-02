import pandas as pd

#xlrd must be downloaded first
import xlrd


##Use LoughranMcDonald dictionary to extract sentiment
#df = pd.read_excel('LoughranMcDonald_MasterDictionary_2014.xlsx')

#Rearrange the negativ/positive words of the McDonalds Textfile
McD_neg = list(open('LoughranMcDonald_Negative.csv'))
McD_neg_str = "".join(str(McD_neg))
McD_neg = McD_neg_str.lower()
McD_neg = McD_neg.replace(',2009\\n','')

McD_pos = list(open('LoughranMcDonald_Positive.csv'))
McD_pos_str = "".join(str(McD_pos))
McD_pos = McD_pos_str.lower()
McD_pos = McD_pos.replace(',2009\\n','')


#Find all negatives in Bitcoin Magazin articles:
neg_list = []
neg_list_L = []
for article in magazin_list :
    negatives = [w for w in article if w in McD_neg]
    neg_list.append(negatives)
    neg_list_L.append(len(negatives))

#Find all positivs in Bitcoin Magazin articles
pos_list = []
pos_list_L = []
for article in magazin_list :
    positives = [w for w in article if w in McD_pos]
    pos_list.append(positives)
    pos_list_L.append(len(positives))



#Bullish/Bearish indicators:(Not working yet, wrong formula)
count = 0
indic_list = []
for article in magazin_list :
    count += 1
    indic_list.append((math.log(math.log(1 + pos_list_L[count-1] / magazin_list_L[count-1]))/
                                math.log(1 + neg_list_L[count-1] / magazin_list_L[count-1]))/
                                math.log(2))





