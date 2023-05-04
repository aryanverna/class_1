from nltk.tokenize import sent_tokenize,word_tokenize

paragraph_text="""
Hello all , Welcome to Python Programming Academy. Python Programming Academy is a nice platform to learn new programming skills. It is difficult to get enrolled in this Academy.
"""

tokenized_text_data=sent_tokenize(paragraph_text)
tokenized_words=word_tokenize(paragraph_text)
print("Tokenized Sentences:\n",tokenized_text_data,"\n")
print("Tokenized Words:\n",tokenized_words,"\n")

from nltk.probability import FreqDist
frequency_distribution=FreqDist(tokenized_words)
print(frequency_distribution)

import matplotlib.pyplot as plt
frequency_distribution.plot(32,cumulative=False)
plt.show()

import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
stop_words_data=set(stopwords.words("english"))
print(stop_words_data)

filtered_words_list=[]
for words in tokenized_words:
    if words not in stop_words_data:
        filtered_words_list.append(words)

print("Tokenized Words:\n",tokenized_words,"\n")
print("Filtered Words:\n",filtered_words_list,"\n")

from wordcloud import WordCloud, get_single_color_func
word_cloud= WordCloud(collocations='false', background_color='white').generate(paragraph_text)
plt.imshow(word_cloud,interpolation='bilinear')
plt.axis("off")
plt.show()

