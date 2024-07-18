from bs4 import BeautifulSoup       #importing BeautifulSoup package from BS4.
import re       #importing regular expression package.
import sys      #importung sys package.
import time     #importing time package.
import math     #importing math package.
import matplotlib.pyplot as plt  #importing matplotlib package.
import os       #importing os package.
import numpy as np
from scipy.cluster.hierarchy import linkage, fcluster

cwd = os.getcwd()                       # getting the current working directory using getcwd function.

inputsource = cwd + "//files//"         # concatenating files to the end of the cwd and storing it in inputsource.

stopwords = ['a', 'about', 'above', 'according', 'across', 'actually', 'adj', 'after', 'afterwards', 'again', 'against', 'all', 'almost', 'alone', 'along', 'already', 'also', 'although', 'always', 'among', 'amongst', 'an', 'and', 'another', 'any', 'anybody', 'anyhow', 'anyone', 'anything', 'anywhere', 'are', 'area', 'areas', "aren't", 'around', 'as', 'ask', 'asked', 'asking', 'asks', 'at', 'away', 'b', 'back', 'backed', 'backing', 'backs', 'be', 'became', 'because', 'become', 'becomes', 'becoming', 'been', 'before', 'beforehand', 'began', 'begin', 'beginning', 'behind', 'being', 'beings', 'below', 'beside', 'besides', 'best', 'better', 'between', 'beyond', 'big', 'billion', 'both', 'but', 'by', 'c', 'came', 'can', "can't", 'cannot', 'caption', 'case', 'cases', 'certain', 'certainly', 'clear', 'clearly', 'co', 'come', 'could', "couldn't", 'd', 'did', "didn't", 'differ', 'different', 'differently', 'do', 'does', "doesn't", "don't", 'done', 'down', 'downed', 'downing', 'downs', 'during', 'e', 'each', 'early', 'eg', 'eight', 'eighty', 'either', 'else', 'elsewhere', 'end', 'ended', 'ending', 'ends', 'enough', 'etc', 'even', 'evenly', 'ever', 'every', 'everybody', 'everyone', 'everything', 'everywhere', 'except', 'f', 'face', 'faces', 'fact', 'facts', 'far', 'felt', 'few', 'fifty', 'find', 'finds', 'first', 'five', 'for', 'former', 'formerly', 'forty', 'found', 'four', 'from', 'further', 'furthered', 'furthering', 'furthers', 'g', 'gave', 'general', 'generally', 'get', 'gets', 'give', 'given', 'gives', 'go', 'going', 'good', 'goods', 'got', 'great', 'greater', 'greatest', 'group', 'grouped', 'grouping', 'groups', 'h', 'had', 'has', "hasn't", 'have', "haven't", 'having', 'he', "he'd", "he'll", "he's", 'hence', 'her', 'here', "here's", 'hereafter', 'hereby', 'herein', 'hereupon', 'hers', 'herself', 'high', 'higher', 'highest', 'him', 'himself', 'his', 'how', 'however', 'hundred', 'i', "i'd", "i'll", "i'm", "i've", 'ie', 'if', 'important', 'in', 'inc', 'indeed', 'instead', 'interest', 'interested', 'interesting', 'interests', 'into', 'is', "isn't", 'it', "it's", 'its', 'itself', 'j', 'just', 'k', 'l', 'large', 'largely', 'last', 'later', 'latest', 'latter', 'latterly', 'least', 'less', 'let', "let's", 'lets', 'like', 'likely', 'long', 'longer', 'longest', 'ltd', 'm', 'made', 'make', 'makes', 'making', 'man', 'many', 'may', 'maybe', 'me', 'meantime', 'meanwhile', 'member', 'members', 'men', 'might', 'million', 'miss', 'more', 'moreover', 'most', 'mostly', 'mr', 'mrs', 'much', 'must', 'my', 'myself', 'n', 'namely', 'necessary', 'need', 'needed', 'needing', 'needs', 'neither', 'never', 'nevertheless', 'new', 'newer', 'newest', 'next', 'nine', 'ninety', 'no', 'nobody', 'non', 'none', 'nonetheless', 'noone', 'nor', 'not', 'nothing', 'now', 'nowhere', 'number', 'numbers', 'o', 'of', 'off', 'often', 'old', 'older', 'oldest', 'on', 'once', 'one', "one's", 'only', 'onto', 'open', 'opened', 'opens', 'or', 'order', 'ordered', 'ordering', 'orders', 'other', 'others', 'otherwise', 'our', 'ours', 'ourselves', 'out', 'over', 'overall', 'own', 'p', 'part', 'parted', 'parting', 'parts', 'per', 'perhaps', 'place', 'places', 'point', 'pointed', 'pointing', 'points', 'possible', 'present', 'presented', 'presenting', 'presents', 'problem', 'problems', 'put', 'puts', 'q', 'quite', 'r', 'rather', 'really', 'recent', 'recently', 'right', 'room', 'rooms', 's', 'said', 'same', 'saw', 'say', 'says', 'second', 'seconds', 'see', 'seem', 'seemed', 'seeming', 'seems', 'seven', 'seventy', 'several', 'she', "she'd", "she'll", "she's", 'should', "shouldn't", 'show', 'showed', 'showing', 'shows', 'sides', 'since', 'six', 'sixty', 'small', 'smaller', 'smallest', 'so', 'some', 'somebody', 'somehow', 'someone', 'something', 'sometime', 'sometimes', 'somewhere', 'state', 'states', 'still', 'stop', 'such', 'sure', 't', 'take', 'taken', 'taking', 'ten', 'than', 'that', "that'll", "that's", "that've", 'the', 'their', 'them', 'themselves', 'then', 'thence', 'there', "there'd", "there'll", "there're", "there's", "there've", 'thereafter', 'thereby', 'therefore', 'therein', 'thereupon', 'these', 'they', "they'd", "they'll", "they're", "they've", 'thing', 'things', 'think', 'thinks', 'thirty', 'this', 'those', 'though', 'thought', 'thoughts', 'thousand', 'three', 'through', 'throughout', 'thru', 'thus', 'to', 'today', 'together', 'too', 'took', 'toward', 'towards', 'trillion', 'turn', 'turned', 'turning', 'turns', 'twenty', 'two', 'u', 'under', 'unless', 'unlike', 'unlikely', 'until', 'up', 'upon', 'us', 'use', 'used', 'uses', 'using', 'v', 'very', 'via', 'w', 'want', 'wanted', 'wanting', 'wants', 'was', "wasn't", 'way', 'ways', 'we', "we'd", "we'll", "we're", "we've", 'well', 'wells', 'were', "weren't", 'what', "what'll", "what's", "what've", 'whatever', 'when', 'whence', 'whenever', 'where', "where's", 'whereafter', 'whereas', 'whereby', 'wherein', 'whereupon', 'wherever', 'whether', 'which', 'while', 'whither', 'who', "who'd", "who'll", "who's", 'whoever', 'whole', 'whom', 'whomever', 'whose', 'why', 'will', 'with', 'within', 'without', "won't", 'work', 'worked', 'working', 'works', 'would', "wouldn't", 'x', 'y', 'year', 'years', 'yes', 'yet', 'you', "you'd", "you'll", "you're", "you've", 'young', 'younger', 'youngest', 'your', 'yours', 'yourself', 'yourselves', 'z'] #list of stopwords

global_dict_list = []         #global dictionary to maintain entire catalog of words present in all the 503 documents along with their combined frequency.

global_dict = {}               #global dictionary to store all the tokens in the document corpus.

df = dict()                    #dictionary to maintain document frequency of each term.

start_time = time.time()        #variable to store start time in seconds.

for i in range(1,504):          #looping through all the 502 html documents.

    local_dict_freq = dict()         #local dictionary to maintain individual catalog of words present in each document along with their frequency in that particular document.

    filename = "%03d.html" % i  #storing the current filename in filename variable.
    filepath = inputsource + filename   #variable to store the source of the filename.

    with open(filepath, "r", encoding='ISO-8859-1') as file:       #opening the file using open command.
        input_html = file.read()                            #reading the contents of the file.

    parsed_soup = BeautifulSoup(input_html, 'html.parser')  #parsing the file using beautifulsoup to remove all the html tags.

    parsed_text = parsed_soup.get_text()                    #getting the text and storing it in parsed_text variable using get_text() function.

    parsed_text = re.sub(r"\d+", '', parsed_text)           #removing digits from the parsed_text.

    parsed_text = re.sub(r"’", '', parsed_text)             #removing apostrophes from the parsed_text.

    parsed_text = re.sub(r"_", '', parsed_text)             #removing underscores from the parsed_text.

    parsed_text = re.sub(r"-", '', parsed_text)             #removing dashes from the parsed_text.
    
    final_words = re.findall(r'\w+', parsed_text)           #segregating the parsed_text into words.

    final_words = [word.lower() for word in final_words]    #converting all the into lowercase.
    
    for word in final_words:                                #storing the words in the local_dictionary.
        if word not in stopwords and len(word) != 1:        #if the word not in stopwords and the length is greater than 1 we proceed to add it in the dictionary.
            if word in local_dict_freq:
                local_dict_freq[word] = local_dict_freq[word] + 1         #if the word already exists in the dictionary we increase its frequency.
            else:
                local_dict_freq[word] = 1                            #else we create a new record and mark its frequency to 1.

    for word in final_words:                                #storing the words in the global dictionary.
        if word not in stopwords and len(word) != 1:        #if the word not in stopwords and the length is greater than 1 we proceed to add it in the dictionary.
            if word in global_dict:
                global_dict[word] = global_dict[word] + 1     #if the word already exists we increase its frequency.    
            else:
                global_dict[word] = 1                       #else we create a new record.
    
    global_dict_list.append(local_dict_freq)                #we append the local_dict_freq to the list of all local_dicts.

ele_once  = []                  #list that we populate with all the words that occur only once.

for k, v in global_dict.items():    #populating the list.
    if v == 1:
        ele_once.append(k)


for once in ele_once:           #remove the elements that occur only once in the whole corpus from the global dictionary.
    del global_dict[once]

for local in global_dict_list:      #removing elements that occur only once in the entire corpus.
    for once in ele_once:
        if once in local:
            del local[once]
        
for local in global_dict_list:
    for word in local:                            #we start to populate df dictionary.
        if word not in df:                                  #if word not in df we create a new record and update it.
            df[word] = {}
            df[word][filename] = local[word]
        else:
            df[word][filename] = local[word]     #else we just update the existing record of the document.

idf = {}                                                    #dictionary to maintain inverse document frequency values.

for token in df:                                            #for all the tokens in the df dictionary we calculate the idf and store the value in idf dictionary.
        idf[token] = math.log(502 / len(df[token]))

sum_doc_length = sum(len(doc) for doc in global_dict_list)      #we calculate sum of length of all the documents.
avg_doc_length = sum_doc_length / 502                       #we calculate the average document length.

global_tfidf_list = {}                                      #list to store all the tfidf values of each document of the corpus.

for i in range(1,503):
    cur_dict = global_dict_list[i-1]                        #we fetch the current dictionary.

    tf_idf = {}                                             #dictionary to maintain tf_idf scores.

    for word in cur_dict:                                   #we calculate tf_idf of all the tokens.
        tf_idf[word] = idf[word] * math.sqrt(cur_dict[word])
 
    squaresumroot = math.sqrt(sum(item ** 2 for item in tf_idf.values()))          #we calculate squaresumroot to perform normalization.

    finaltfidf = {}                                                                #tfidf values after normalization.

    for word in cur_dict:
        finaltfidf[word] = tf_idf[word]/squaresumroot
    
    filename = "%03d.html" % i 

    global_tfidf_list[filename] = finaltfidf
    
tdm = {}                                            #dictionary to store the number of odcuments each word occurs in.

for word in global_dict:                            #looping using each word and counting the number of dictionaries it exists in.
    num_of_docs = 0
    for local in global_dict_list:
        if word in local:
            num_of_docs = num_of_docs + 1   
    tdm[word] = num_of_docs

postings_dict = {}                                 #dictinary to store the postings file position.

temp_post = 1

for word in tdm:                                    #assigning posting position for each word.
    postings_dict[word] = temp_post
    temp_post = temp_post + tdm[word]

final_postings = []                                 # creating a list of postings.

for word in tdm:                                    # for every word in tdm
    some_temp = []
    for i in range(1,503):
        filename = "%03d.html" % i                  # we are iterating through each document to see if exists and if it does we insert a record in the postings list.
        if word in global_tfidf_list[filename].keys():
            temp_post = []
            temp_post.append(filename)
            temp_post.append(global_tfidf_list[filename][word])
            some_temp.append(temp_post)
    final_postings.append(some_temp)

num = np.zeros((503,503)) # initilazing a numerator matrix with all zeros.

den = []                    # creating a denominator list.
for i in range(504):
    den.append(0)

for word_postings in final_postings:        # iterating through each posting of each word in postings list.
    l = len(word_postings)
    for i in range(0, l):                   # for each posting of the word, we are updating num and den values of the files in which the said words are present.
        for j in range(i+1, l):
            first_file = word_postings[i][0]    # extracting first and second file numbers from their naming format i.e., "001.html"
            second_file = word_postings[j][0]
            first_file_int = ""
            second_file_int = ""

            for char in first_file:
                if char.isdigit():
                        first_file_int += char
            first = int(first_file_int) - 1
            for char in second_file:
                if char.isdigit():
                        second_file_int += char
            second = int(second_file_int) - 1

            num[second, first] = num[second, first] + (word_postings[i][1] * word_postings[j][1])       #updating the num values.
            num[first, second] = num[first, second] + (word_postings[i][1] * word_postings[j][1])

        den[first] = den[first] + (word_postings[i][1] ** 2) #updating the den values.

for i in range(0, 503):
    for j in range(0, 503):
        if den[i] != 0 and den[j] != 0: #updating the num values by dividing with values from den.
            num[i,j] = (num[i, j]) / (math.sqrt(den[i]) * math.sqrt(den[j]))

with open('similairty_matrix.txt', 'w') as f: #writing the similairt matrix to similairty_matrix.txt.
    for i in range(0,503):
        for j in range(0, 503):
                x = num[i, j]
                f.write(str(x) + " ")
        f.write("\n")

min = np.min(num)   #fetching the minimum value from num.
max = np.max(num)   #fetching the maximum value from num.
normalized_matrix = (num - min) / (max - min)   #normalizing num matrix.

dis = np.zeros((503,503))       #initializing dis matrix.

dis = 1 - normalized_matrix     #updating the dis matrix.

linkage_matrix = linkage(dis, method='complete') #performing clustering.

max_dist = 0.4 # assigning max_dis as 0.4 so that we can stop clustering once max distance is 0.4.
labels = fcluster(linkage_matrix, max_dist, criterion='distance')   #creating labels to store the clusters.

# printing the merged clusters at each step.
for i in range(1, len(labels)):
    if labels[i] != labels[i-1]:
        print(f"Cluster {labels[i-1]} merged with Cluster {labels[i]}")

end_time = time.time()      #stopping the clock.

print("\n" + "Execution time in milliseconds : ", (end_time-start_time)*1000)  #caluculating the execution time in ms.
