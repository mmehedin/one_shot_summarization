
# coding: utf-8

# Based on:
# - https://machinelearningmastery.com/prepare-news-articles-text-summarization/

# In[1]:


import pandas as pd
import nltk
import matplotlib


# In[2]:


import os
from os import listdir


# In[3]:


import keras


# In[4]:


import string


# ---

# In[5]:


current_dir = os.getcwd()
#os.path.join(os.path.dirname(current_dir), '..', '/cnn/stories/')
#os.path.abspath(current_dir)
#os.path.abspath(os.path.join(os.path.dirname(current_dir),'..', "cnn/stories/"))


# In[6]:


cnn_dir = os.path.abspath(os.path.join(os.path.dirname(current_dir), 'cnn/stories/'))
#print(cnn_dir)


# In[7]:


#for dirname in listdir(cnn_dir):
#    print(dirname)


# In[8]:


# load doc into memory
def load_doc(filename):
	# open the file as read only
	file = open(filename, encoding='utf-8')
	# read all text
	text = file.read()
	# close the file
	file.close()
	return text


# In[9]:


# split a document into news story and highlights
def split_story(doc):
	# find first highlight
	index = doc.find('@highlight')
	# split into story and highlights
	story, highlights = doc[:index], doc[index:].split('@highlight')
	# strip extra white space around each highlight
	highlights = [h.strip() for h in highlights if len(h) > 0]
	return story, highlights


# In[10]:


# load all stories in a directory
def load_stories(directory):
	stories = list()
	for name in listdir(directory):
		filename = directory + '/' + name
		# load document
		doc = load_doc(filename)
		# split into story and highlights
		story, highlights = split_story(doc)
		# store
		stories.append({'story':story, 'highlights':highlights})
	return stories


# In[11]:


# clean a list of lines
def clean_lines(lines):
	cleaned = list()
	# prepare a translation table to remove punctuation
	table = str.maketrans('', '', string.punctuation)
	for line in lines:
		# strip source cnn office if it exists
		index = line.find('(CNN) -- ')
		if index > -1:
			line = line[index+len('(CNN)'):]
		# tokenize on white space
		line = line.split()
		# convert to lower case
		line = [word.lower() for word in line]
		# remove punctuation from each token
		line = [w.translate(table) for w in line]
		# remove tokens with numbers in them
		line = [word for word in line if word.isalpha()]
		# store as string
		cleaned.append(' '.join(line))
	# remove empty strings
	cleaned = [c for c in cleaned if len(c) > 0]
	return cleaned


# In[12]:


# load stories
#directory = 'cnn/stories/'
def get_stories():
    stories = load_stories(cnn_dir)
    print('Loaded Stories %d' % len(stories))
    return stories


# In[13]:


#print(stories[1])


# In[14]:


# clean stories
def clean_stories(stories):
    for example in stories:
        example['story'] = clean_lines(example['story'].split('\n'))
        example['highlights'] = clean_lines(example['highlights'])
    return stories


# In[15]:


#print(stories[1])


# In[18]:


def get_cnn_stories():
    stories = get_stories()
    return clean_stories(stories)


# In[19]:


stories = get_cnn_stories()
#print(stories[0])

