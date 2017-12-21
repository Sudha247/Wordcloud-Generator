import nltk
import wordcloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
f = open("file1.txt","r")
data = f.read()
tokens = nltk.word_tokenize(data)
text = nltk.pos_tag(tokens)
lis = []
for word,pos in text:
    # print(word, pos)
    if(pos == "NN" or pos == "NNS" or pos == "NNP" or pos == "NNPS"):
        lis.append(word)
#print(lis)
fdist = nltk.FreqDist(lis)
# print(fdist.most_common(20))

words = []
for w,c in fdist.most_common(40):
	if len(w) > 3:
		words.append(w)

wc = wordcloud.WordCloud(font_path='/home/sudha/pfiles/intern/Chewy-Regular.ttf', height=500, width=500,background_color='white').generate(" ".join(words))
plt.figure()
plt.imshow(wc)
plt.axis("off")
plt.show()
f.close()
