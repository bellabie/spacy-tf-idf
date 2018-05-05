import spacy
nlp = spacy.load("en_core_web_sm")
from collections import Counter
from spacy.lang.en.stop_words import STOP_WORDS
#print(STOP_WORDS)

#Need to connect to files, Excel or csv would probably be user friendlier

source = open("BestPractest.txt","r")
text = source.read()

phrase = nlp(text)


words = [token.lemma_ for token in phrase]

#Create a list of all the lemmatized tokens (words)
word_freq = Counter(words)
word_list = list(word_freq.items()) 
word_list.sort() #list alphabetized just for fun

#Total number of lemmatized tokens in the phrase
print(len(word_list))

#Prints each word and its count on a new line
i=0
while i<len(word_list):
	print(word_list[i])
	i=i+1
	pass


#for token in test:
#	lemmalist[token] = token.lemma_
#	print(lemmalist)

#comments = nlp(u"")

# tfidf = (count of text / all the text in the document) * natural? log of (document count / documents containing that text)
