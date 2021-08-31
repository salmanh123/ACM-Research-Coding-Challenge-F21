# ACM Research Coding Challenge (Fall 2021)

## [](https://github.com/ACM-Research/Coding-Challenge-F21#no-collaboration-policy)No Collaboration Policy

**You may not collaborate with anyone on this challenge.**  You  _are_  allowed to use Internet documentation. If you  _do_  use existing code (either from Github, Stack Overflow, or other sources),  **please cite your sources in the README**.

## [](https://github.com/ACM-Research/Coding-Challenge-F21#submission-procedure)Submission Procedure

Please follow the below instructions on how to submit your answers.

1.  Create a  **public**  fork of this repo and name it  `ACM-Research-Coding-Challenge-F21`. To fork this repo, click the button on the top right and click the "Fork" button.

2.  Clone the fork of the repo to your computer using  `git clone [the URL of your clone]`. You may need to install Git for this (Google it).

3.  Complete the Challenge based on the instructions below.

4.  Submit your solution by filling out this [form](https://acmutd.typeform.com/to/zF1IcBGR).

## Assessment Criteria 

Submissions will be evaluated holistically and based on a combination of effort, validity of approach, analysis, adherence to the prompt, use of outside resources (encouraged), promptness of your submission, and other factors. Your approach and explanation (detailed below) is the most weighted criteria, and partial solutions are accepted. 

## [](https://github.com/ACM-Research/Coding-Challenge-S21#question-one)Question One

[Sentiment analysis](https://en.wikipedia.org/wiki/Sentiment_analysis) is a natural language processing technique that computes a sentiment score for a body of text. This sentiment score can quantify how positive, negative, or neutral the text is. The following dataset in  `input.txt`  contains a relatively large body of text.

**Determine an overall sentiment score of the text in this file, explain what this score means, and contrast this score with what you expected.**  If your solution also provides different metrics about the text (magnitude, individual sentence score, etc.), feel free to add it to your explanation.   

**You may use any programming language you feel most comfortable. We recommend Python because it is the easiest to implement. You're allowed to use any library/API you want to implement this**, just document which ones you used in this README file. Try to complete this as soon as possible as submissions are evaluated on a rolling basis.

Regardless if you can or cannot answer the question, provide a short explanation of how you got your solution or how you think it can be solved in your README.md file. However, we highly recommend giving the challenge a try, you just might learn something new!

## Resources, Documentation, & libraries  utilized to learn more about sentiment analysis
#### https://realpython.com/python-nltk-sentiment-analysis/#using-scikit-learn-classifiers-with-nltk ####
#### https://towardsdatascience.com/design-your-own-sentiment-score-e524308cf787 ####
#### https://towardsdatascience.com/sentimental-analysis-using-vader-a3415fef7664 ####
#### https://stackabuse.com/removing-stop-words-from-strings-in-python/ #### 
#### https://www.kite.com/python/docs/nltk.word_tokenize ####
* NLTK


## Expectations from reading:
Before starting the technical portion of the assessment I read the input file to compare my expectation now and the results of my coding challenge submission in the future. Reading the excerpt, I would give this text a sentiment score of negative-neutral leaning towards neutral. I say this due to the first paragraph seeming like a argument between books, knowledge, and being a fireman from the narrators dream. The second paragraph did not seem negative, more so "happy-sad", pity, and neutral with the description. With the combination of the dream & knowledge argument and the description of the man, **I give it a sentiment score of -.3** with -1 -> -.1 being negative, -.1 -> .1 being neutral, and .1 -> 1 being positive.

## Answer & Results:
* Do a pre-reading and give a personal score on the text
* I started by importing the nltk library and utilizing VADER, tokenize, sentiment intensity analyzer (SID), and stopwords to format/clean the text file so I can provide an analysis without filler words
* I first opened the file, read the contents in, and tokenized each word into a list for further modification
* Using the imported stopwords list, I compared my tokenized list and with the stopwords and appended any word not shared between the two lists to a new string
* With the new cleaned string, I used SID with a function to determine the polarity of strings called ".polarity_scores(string)" to perform my sentiment analyzation
* Using SID & polarity_scores I obtained {'neg': 0.133, 'neu': 0.588, 'pos': 0.278, 'compound': 0.9958} as my score
## Reflections
Comparing my reading expectations and my new answer it seems my answer is more of a neutral-happy sentiment than my guess of a sad-neutral. Part of this I understand as I mentioned the second paragraph being more so "happy-sad" whilst also neutral in its tone. 


