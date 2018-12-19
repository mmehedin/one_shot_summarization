import nltk
from nltk import tokenize
import string

def tokenize_this(text):
	return nltk.tokenize.word_tokenize(text) 

def remove_punctuation(text):
	#table = str.maketrans(string.punctuation, '                                ')
	punct = [p for p in string.punctuation]
	punct.append(' ')
	punct.append('``')
	punct.append('\'\'')
	punct.append('--')
	return [w.lower() for w in text if not w in punct]

def remove_stop(text):
	stop_words =set(nltk.corpus.stopwords.words('english'))
	return [w for w in text if w not in stop_words]


def stem_this(text):
	stemmer = nltk.porter.PorterStemmer()
	return [stemmer.stem(w) for w in text]

def process_text(text):
	#return stem_this(remove_stop(remove_punctuation(tokenize_this(text))))
	return remove_stop(remove_punctuation(tokenize_this(text)))