import spacy
from spacy.lang.en.stop_words import STOP_WORDS
# print(STOP_WORDS) #if you want to see what they are
from collections import Counter
import math
import csv # Excel or csv files would probably be user friendlier

nlp = spacy.load("en_core_web_sm")
# Change to spacy/lang/lex_attrs.py was made to fix capitalization issue
# More info here: https://github.com/explosion/spaCy/pull/1891/files

nlp.vocab["s"].is_stop = True
# Adding s to the list of stop words

# opens the target tsv with read permissions ang outputs another tsv
with open("tsvin.tsv", "r") as tsvsource, open('tsvout.tsv', 'w') as tsvout:
	tsvin = csv.reader(tsvsource, delimiter='\t')
	docnumber = -1
	for row in tsvin:
		docnumber = docnumber + 1
		pass
	print(docnumber) # this is the number of documents to be used in the inverse document frequency
	tsvsource.seek(0)
	for row in tsvin:
		text = row[1]
		# Swaps line breaks for spaces, also remove apostrophes & single quotes
		text = text.replace("\n", " ").replace("'","").replace("’","")
		# "Be" stop words weren't caught before lemmatization with the apostrophe
		text = text.lower()
		# spaCy is_stop was not working on words with capitalized letters
		
		text = nlp(text)
		#print(text) # Print before cleansing to debug

		# Returns lemmatized text without stop words, punctuation, & white space characters
		words = [token.lemma_ for token in text if not (token.is_stop or token.is_punct or token.is_space)]
		# note: I added coded/coding to the irregular verb list because something weird was happening and turning those into "cod"
		#print(words) # Print after cleansing to debug

		# Create a list of all the lemmatized tokens (words)
		word_count = Counter(words)
		word_list = list(word_count.items()) 
		word_list.sort(key=lambda tup: tup[1], reverse=True) #list sorted by frequency

		# Total number of unique lemmatized tokens in the phrase
		totalunique = len(word_list)

		# Now we'll do some math to find the relative frequency of each word in our text
		word_freq = list()
		for i in range(totalunique):
			word, count = word_list[i]
			count = count/totalunique*math.log(1/docnumber)
			word_freq.append((word, count))
			#print(word_freq[i])
			i=i+1
			pass
		pass
	tsvwriter = csv.writer(tsvout)
	#tsvwriter.writerow(["test","test3"*3,"testagain"]) #writes a row containing the following: test,test3test3test3,testagain

# tfidf = (count of word / all the words in the document) * natural? log of (document count / documents containing that word)

# natural log is math.log(x), if you want a different base you can use math.log(x,base)

# NOTE: So far, I've been using:
#* **spaCy version:** 2.0.11
#* **Platform:** Darwin-17.3.0-x86_64-i386-64bit
#* **Python version:** 3.6.4
#* **Models:** en_core_web_sm
