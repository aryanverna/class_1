import nltk
nltk.download('all')
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize,sent_tokenize

text="""
Essay topics in English can be difficult to come up with. While writing essays,many college and high school students face writer's block and have a hard time to think about topics and ideas for an essay. In this article, we will list out many good essay topics from different categories like argumentative essays, essays on technology, environment essays for students from 5th, 6th, 7th, 8th grades. Following list of essay topics are for all - from kids to college students. We have the largest collection of essays. An essay is nothing but a piece of content which is written from the perception of writer or author. Essays are similar to a story, pamphlet, thesis, etc. The best thing about Essay is you can use any type of language - formal or informal. It can biography, the autobiography of anyone. Following is a great list of 100 essay topics. We will be adding 400 more soon!
"""
print(text)
print("\n\n")

text=re.sub(r'\[[0-9]{}*]',' ',text)

formatted_text=re.sub('[^a-zA-Z]',' ',text)
print(formatted_text)
print("\n\n")

stopWords=set(stopwords.words("english"))
words=word_tokenize(formatted_text)

wordfreq={}
for word in words:
    if word in stopWords:
        continue
    if word in wordfreq:
        wordfreq[word] +=1
    else:
        wordfreq[word] = 1


maximum_frequency=max(wordfreq.values())
for word in wordfreq.keys():
    wordfreq[word] = (wordfreq[word]/maximum_frequency)

sentences = sent_tokenize(text)
sentenceValue= {}
for sentence in sentences:
    for word,freq in wordfreq.items():
        if word in sentence.lower():
            if sentence in sentenceValue:
                sentenceValue[sentence] +=freq
            else:
                sentenceValue[sentence] = freq


import heapq
summary=' '
summary_sentence = heapq.nlargest(5,sentenceValue, key=sentenceValue.get)
summary=' '.join(summary_sentence)
print(summary)


