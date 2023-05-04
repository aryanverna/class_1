from nltk.sentiment.vader import SentimentIntensityAnalyzer
vader_analyzer=SentimentIntensityAnalyzer()

text1="I purchased headphones online. I am very happy with the product"
print(text1)
result=vader_analyzer.polarity_scores(text1)
print(result)

print("The sentence is rated as",result['pos']*100,"%Positive")
print("The sentence is rated as",result['neg']*100,"%Negative")
print("The sentence is rated as",result['neu']*100,"%Neutral")
print("\n")



text2="I saw the movie yesterday. The animation was really good but the script was ok."
print(text2)
result=vader_analyzer.polarity_scores(text2)
print(result)

print("The sentence is rated as",result['pos']*100,"%Positive")
print("The sentence is rated as",result['neg']*100,"%Negative")
print("The sentence is rated as",result['neu']*100,"%Neutral")
print("\n")



text3="I enjoy listening to music"
print(text3)
result=vader_analyzer.polarity_scores(text3)
print(result)

print("The sentence is rated as",result['pos']*100,"%Positive")
print("The sentence is rated as",result['neg']*100,"%Negative")
print("The sentence is rated as",result['neu']*100,"%Neutral")
print("\n")



text4="I take a walk in the park everday."
print(text4)
result=vader_analyzer.polarity_scores(text4)
print(result)

print("The sentence is rated as",result['pos']*100,"%Positive")
print("The sentence is rated as",result['neg']*100,"%Negative")
print("The sentence is rated as",result['neu']*100,"%Neutral")
print("\n")



