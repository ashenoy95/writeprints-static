
import nltk
import string
import numpy as np

def character_count(text):
    return len(text.replace(' ',''))

def average_characters_per_word(text):
    return character_count(text)/len(text.split())

def character_frequency(text):
    return tuple(text.lower().count(char) for char in string.ascii_lowercase)

def pos_tag_frequency(text):
    """
    Using universal tags, the sentence "Chairs have legs." yields the
    part-of-speech tag sequence ('NOUN', 'VERB', 'NOUN'), and two 2grams
    ('NOUN', 'VERB') and ('VERB', NOUN').

    Returns:
        tuple of str: Frequency of part-of-speech tags
    """
    words = nltk.word_tokenize(text)
    pos_tags = nltk.pos_tag(words, tagset='universal')
    tagset = ['ADJ','ADP','ADV','CONJ','DET','NOUN','NUM','PRT','PRON','VERB','.','X']
    tags = [tag[1] for tag in pos_tags]
    return tuple(tags.count(tag) for tag in tagset)

def legomena(text):																	    #returns ratio of hapax and dis legomena
	'''
	hapax legomena	:	terms which occur only once in the corpus
	dis legomena	:	terms which occur twice in the corpus	 	
	'''
    freq = nltk.FreqDist(word for word in text.split())
    hapax = [key for key,val in freq.items() if val==1]
    dis = [key for key,val in freq.items() if val==2]
    return len(hapax)/len(dis)

def punctuation_freq(text):
    punctuations = ':;?.!,"' + "'"
    return [text.count(punctuation) for punctuation in punctuations] 

def extract_features(texts):														     #extracts features to list of lists 
	#each sublist consists of all 239 features of a particular text
    features = []
    for text in texts:
        row = ([len(text.split())] + [average_characters_per_word(text)] + [len([word for word in text.split() if len(word) <=3])]
            + [character_count(text)] + [sum([char.isdigit() for char in text])*100/len(text)] + [sum([char.isupper() for char in text])*100/len(text)]
            + [text.count(x) for x in '#$%&\()*+/<=>@[\\]^_{|}~'] + list(character_frequency(text)) + [text.lower().count(char) for char in string.digits])
        row += [legomena(text)] + list(pos_tag_frequency(text)) + punctuation_freq(text) + [sum(punctuation_freq(text))*100/len(text)]
        row += [text.count(word) for word in nltk.corpus.stopwords.words('english')]    #function words
        features.append(row)														    #single merged list is appended to list of lists
    return features




