
# Created on Sat Aug 28 15:27:27 2021

# @author: Salman Hossain
# Purpose: Perform sentiment analysis on a text file



# Importing nltk to provide a sentiment score & 
# to utilize functions
import nltk
nltk.download([
    "stopwords",
    "averaged_perceptron_tagger",
    "vader_lexicon"
])
nltk.download('stopwords')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
sid = SentimentIntensityAnalyzer()


# Opening text file
originalText = open('./input.txt', 'r')
ourText = originalText.read()


# Tokenizing contents in string to create a list of words
tokenizedText = word_tokenize(ourText)


# Comparing tokenized list with a list of stopwords and only retaining those
# words from the tokenized list not contained in the stopwords list
cleanedText = [word for word in tokenizedText if not word in stopwords.words()]

# Joining list of words to a string
reformattedText = " ".join(cleanedText)

# Performing sentiment analysis with .polarity_scores method from imported
# SentimentIntensityAnalyzer
print(sid.polarity_scores(reformattedText))

# Closing file
originalText.close()