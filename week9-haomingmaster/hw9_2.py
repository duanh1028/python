
import nltk
import math
import numpy as np
from helper import remove_punc

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

#Clean and lemmatize the contents of a document
#Takes in a file name to read in and clean
#Return a list of words, without stopwords and punctuation, and with all words stemmed
# NOTE: Do not append any directory names to doc -- assume we will give you
# a string representing a file name that will open correctly
def readAndCleanDoc(doc) :
    #1. Open document, read text into *single* string
    f = open(doc, 'r')
    words = f.read()
    f.close()

    #2. Tokenize string using nltk.tokenize.word_tokenize
    words = nltk.tokenize.word_tokenize(words)

    #3. Filter out punctuation from list of words (use remove_punc)
    words = remove_punc(words)

    #4. Make the words lower case
    tempWords = []
    for content in words:
        tempWords.append(content.lower())
    words = tempWords

    #5. Filter out stopwords
    stopwords = nltk.corpus.stopwords.words('english')
    words = [content for content in words if content not in stopwords]

    #6. Stem words
    stemmer = nltk.stem.PorterStemmer()
    words = [stemmer.stem(content) for content in words]    

    return words
    
#Builds a doc-word matrix for a set of documents
#Takes in a *list of filenames*
#
#Returns 1) a doc-word matrix for the cleaned documents
#This should be a 2-dimensional numpy array, with one row per document and one 
#column per word (there should be as many columns as unique words that appear
#across *all* documents. Also, Before constructing the doc-word matrix, 
#you should sort the wordlist output and construct the doc-word matrix based on the sorted list
#
#Also returns 2) a list of words that should correspond to the columns in
#docword
def buildDocWordMatrix(doclist) :
    #1. Create word lists for each cleaned doc (use readAndCleanDoc)
    wordlist = []
    for content in doclist:
        wordlist += readAndCleanDoc(content)

    wordlist = sorted(list(set(wordlist)))

    #2. Use these word lists to build the doc word matrix
    freqWord = []
    for content in doclist:
        col = dict.fromkeys(wordlist, 0)
        words = readAndCleanDoc(content)
        for i in words:
            col[i] += 1.0
        freqWord.append(list(col.values()))
    docword = np.array(freqWord)

    return docword, wordlist
    
#Builds a term-frequency matrix
#Takes in a doc word matrix (as built in buildDocWordMatrix)
#Returns a term-frequency matrix, which should be a 2-dimensional numpy array
#with the same shape as docword
def buildTFMatrix(docword) :
    #fill in
    row, col = docword.shape
    tf = np.zeros([row, col]) #initializa the matrix

    for r in range(0, row):
        sum_r = sum(docword[r])
        for c in range(0, col):
            tf[r][c] = docword[r][c] / sum_r

    return tf
    
#Builds an inverse document frequency matrix
#Takes in a doc word matrix (as built in buildDocWordMatrix)
#Returns an inverse document frequency matrix (should be a 1xW numpy array where
#W is the number of words in the doc word matrix)
#Don't forget the log factor!
def buildIDFMatrix(docword) :
    #fill in
    row, col = docword.shape
    idf = np.zeros([1, col]) #initializa the matrix

    n = np.zeros([col])
    for c in range(0, col):
        for r in range(0, row):
            if(docword[r][c] > 0):
                n[c] += 1.0
    
    for c in range(0, col):
        idf[0][c] = math.log(row/n[c], 10)

    return idf
    
#Builds a tf-idf matrix given a doc word matrix
def buildTFIDFMatrix(docword) :
    #fill in
    tf = buildTFMatrix(docword)
    idf = buildIDFMatrix(docword)

    row, col = docword.shape
    tfidf = np.zeros([row, col])

    for r in range(0, row):
        for c in range(0, col):
            tfidf[r][c] = idf[0][c]*tf[r][c]

    return tfidf
    
#Find the three most distinctive words, according to TFIDF, in each document
#Input: a docword matrix, a wordlist (corresponding to columns) and a doclist 
# (corresponding to rows)
#Output: a dictionary, mapping each document name from doclist to an (ordered
# list of the three most common words in each document
def findDistinctiveWords(docword, wordlist, doclist) :
    
    distinctiveWords = {}
    #fill in
    #you might find numpy.argsort helpful for solving this problem:
    #https://docs.scipy.org/doc/numpy/reference/generated/numpy.argsort.html
    tfidf = buildTFIDFMatrix(docword)
    
    distinctiveList = []
    row = len(doclist)
    col = len(wordlist)
    for r in range(0, row):
        freq = dict.fromkeys(wordlist, 0)
        for c in range(0, col):
            freq[wordlist[c]] = tfidf[r][c]
        distinctiveList.append(sorted(freq.items(), key=lambda kv: kv[1], reverse=True)[:3])

    distinctiveWords = dict.fromkeys(doclist, 0)
    x = 0
    for content in doclist:
        distinctiveWords[content] = [x[0] for x in distinctiveList[x]]
        x += 1
        
    return distinctiveWords


if __name__ == '__main__':
    from os import listdir
    from os.path import isfile, join, splitext
    
    ### Test Cases ###
    directory='lecs'
    path1 = join(directory, '1_vidText.txt')
    path2 = join(directory, '2_vidText.txt')
    
    # Uncomment and recomment ths part where you see fit for testing purposes

    print("*** Testing readAndCleanDoc ***")
    print(readAndCleanDoc(path1)[0:5])
    print("*** Testing buildDocWordMatrix ***") 
    doclist =[path1, path2]
    docword, wordlist = buildDocWordMatrix(doclist)
    print(docword.shape)
    print(len(wordlist))
    print(docword[0][0:10])
    print(wordlist[0:10])
    print(docword[1][0:10])
    print("*** Testing buildTFMatrix ***") 
    tf = buildTFMatrix(docword)
    print(tf[0][0:10])
    print(tf[1][0:10])
    print(tf.sum(axis =1))
    print("*** Testing buildIDFMatrix ***") 
    idf = buildIDFMatrix(docword)
    print(idf[0][0:10])
    print("*** Testing buildTFIDFMatrix ***") 
    tfidf = buildTFIDFMatrix(docword)
    print(tfidf.shape)
    print(tfidf[0][0:10])
    print(tfidf[1][0:10])
    print("*** Testing findDistinctiveWords ***")
    print(findDistinctiveWords(docword, wordlist, doclist))
