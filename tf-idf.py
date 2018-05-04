import spacy
nlp = spacy.load("en_core_web_sm")
from collections import Counter

#Need to connect to files, Excel or csv would probably be user friendlier

phrase = nlp(u"Job wise I think you'd excel at user or topical research, design, project management, evangelism/marketing/brand roles, or anything involving speaking, storytelling, or presentation. If you want to do something really different, maybe graphic art or story boarding. I'm probably not the best person to ask on education or training, but continue to surround yourself with engaging people who support you and encourage you to challenge yourself, grow, and reflect.")


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



#shiny
