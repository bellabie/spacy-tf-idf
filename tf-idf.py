import spacy
nlp = spacy.load("en_core_web_sm")
from collections import Counter
from spacy.lang.en.stop_words import STOP_WORDS
#print(STOP_WORDS) #if you want to see what they are

#Need to connect to files, Excel or csv would probably be user friendlier

source = open("goodAtStuff.txt","r")
text = source.read()
source.close()

#Swaps line breaks for spaces
text = text.replace("\n", " ")

phrase = nlp(text)

#Returns lemmatized text without stop words, punctuation, and white space characters
words = [token.lemma_ for token in phrase if not (token.is_stop or token.is_punct or token.is_space)]

#Create a list of all the lemmatized tokens (words)
word_freq = Counter(words)
word_list = list(word_freq.items()) 
word_list.sort(key=lambda tup: tup[1], reverse=True) #list sorted by frequency

#Total number of lemmatized tokens in the phrase
print(len(word_list))

#Prints each word and its count on a new line
i=0
while i<len(word_list):
	print(word_list[i])
	i=i+1
	pass


#comments = nlp(u"")

# tfidf = (count of text / all the text in the document) * natural? log of (document count / documents containing that text)

# NOTE: So far, I've been using:
#* **spaCy version:** 2.0.11
#* **Platform:** Darwin-17.3.0-x86_64-i386-64bit
#* **Python version:** 3.6.4
#* **Models:** en_core_web_sm
