import spacy
nlp = spacy.load("en_core_web_sm")
from collections import Counter
from spacy.lang.en.stop_words import STOP_WORDS
#Change to spacy/lang/lex_attrs.py was made to fix capitalization issue
#More info here: https://github.com/explosion/spaCy/pull/1891/files
nlp.vocab["s"].is_stop = True
#Adding s to the list of stop words
#print(STOP_WORDS) #if you want to see what they are

#Excel or csv files would probably be user friendlier

file = "goodAtStuff.txt"
print(file)
source = open(file,"r")
text = source.read()
source.close()

#Swaps line breaks for spaces, also remove apostrophes & single quotes
text = text.replace("\n", " ").replace("'","").replace("’","")
#"Be" stop words weren't caught before lemmatization with the apostrophe
text = text.lower()
#spaCy is_stop was not working on words with capitalized letters
text = nlp(text)
#print(phrase) #Print before cleansing to

#Returns lemmatized text without stop words, punctuation, & white space characters
words = [token.lemma_ for token in text if not (token.is_stop or token.is_punct or token.is_space)]

#print(words) #Print after cleansing to debug

#Create a list of all the lemmatized tokens (words)
word_count = Counter(words)
word_list = list(word_count.items()) 
word_list.sort(key=lambda tup: tup[1], reverse=True) #list sorted by frequency

#Total number of lemmatized tokens in the phrase
totalunique = len(word_list)

#Now we'll do some math to find the relative frequency of each word within this text
word_freq = list()
i=0
while i<len(word_list):
	word, count = word_list[i]
	count = count/totalunique
	word_freq.append((word, count))
	print(word_freq[i])
	i=i+1
	pass




#comments = nlp(u"")

# tfidf = (count of text / all the text in the document) * natural? log of (document count / documents containing that text)

# NOTE: So far, I've been using:
#* **spaCy version:** 2.0.11
#* **Platform:** Darwin-17.3.0-x86_64-i386-64bit
#* **Python version:** 3.6.4
#* **Models:** en_core_web_sm
