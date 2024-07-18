from bs4 import BeautifulSoup       #importing BeautifulSoup package from BS4.
import re       #importing regular expression package.
import sys      #importung sys package.
import time     #importing time package.
import math     #importing math package.

inputsource = sys.argv[1]           #variable to store inputsource i.e., path to input files which we will be taking from command line interface.
outputsource = sys.argv[2]          #variable to store outputsource i.e., path to store output files which we will be taking from command line interface.

global_dict_list = []         #global dictionary to maintain entire catalog of words present in all the 503 documents along with their combined frequency.

global_dict = {}               #global dictionary to store all the tokens in the document corpus.

df = dict()                    #dictionary to maintain document frequency of each term.

start_time = time.time()        #variable to store start time in seconds.

for i in range(1,503):          #looping through all the 502 html documents.

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

    stopwords = ['a', 'about', 'above', 'according', 'across', 'actually', 'adj', 'after', 'afterwards', 'again', 'against', 'all', 'almost', 'alone', 'along', 'already', 'also', 'although', 'always', 'among', 'amongst', 'an', 'and', 'another', 'any', 'anybody', 'anyhow', 'anyone', 'anything', 'anywhere', 'are', 'area', 'areas', "aren't", 'around', 'as', 'ask', 'asked', 'asking', 'asks', 'at', 'away', 'b', 'back', 'backed', 'backing', 'backs', 'be', 'became', 'because', 'become', 'becomes', 'becoming', 'been', 'before', 'beforehand', 'began', 'begin', 'beginning', 'behind', 'being', 'beings', 'below', 'beside', 'besides', 'best', 'better', 'between', 'beyond', 'big', 'billion', 'both', 'but', 'by', 'c', 'came', 'can', "can't", 'cannot', 'caption', 'case', 'cases', 'certain', 'certainly', 'clear', 'clearly', 'co', 'come', 'could', "couldn't", 'd', 'did', "didn't", 'differ', 'different', 'differently', 'do', 'does', "doesn't", "don't", 'done', 'down', 'downed', 'downing', 'downs', 'during', 'e', 'each', 'early', 'eg', 'eight', 'eighty', 'either', 'else', 'elsewhere', 'end', 'ended', 'ending', 'ends', 'enough', 'etc', 'even', 'evenly', 'ever', 'every', 'everybody', 'everyone', 'everything', 'everywhere', 'except', 'f', 'face', 'faces', 'fact', 'facts', 'far', 'felt', 'few', 'fifty', 'find', 'finds', 'first', 'five', 'for', 'former', 'formerly', 'forty', 'found', 'four', 'from', 'further', 'furthered', 'furthering', 'furthers', 'g', 'gave', 'general', 'generally', 'get', 'gets', 'give', 'given', 'gives', 'go', 'going', 'good', 'goods', 'got', 'great', 'greater', 'greatest', 'group', 'grouped', 'grouping', 'groups', 'h', 'had', 'has', "hasn't", 'have', "haven't", 'having', 'he', "he'd", "he'll", "he's", 'hence', 'her', 'here', "here's", 'hereafter', 'hereby', 'herein', 'hereupon', 'hers', 'herself', 'high', 'higher', 'highest', 'him', 'himself', 'his', 'how', 'however', 'hundred', 'i', "i'd", "i'll", "i'm", "i've", 'ie', 'if', 'important', 'in', 'inc', 'indeed', 'instead', 'interest', 'interested', 'interesting', 'interests', 'into', 'is', "isn't", 'it', "it's", 'its', 'itself', 'j', 'just', 'k', 'l', 'large', 'largely', 'last', 'later', 'latest', 'latter', 'latterly', 'least', 'less', 'let', "let's", 'lets', 'like', 'likely', 'long', 'longer', 'longest', 'ltd', 'm', 'made', 'make', 'makes', 'making', 'man', 'many', 'may', 'maybe', 'me', 'meantime', 'meanwhile', 'member', 'members', 'men', 'might', 'million', 'miss', 'more', 'moreover', 'most', 'mostly', 'mr', 'mrs', 'much', 'must', 'my', 'myself', 'n', 'namely', 'necessary', 'need', 'needed', 'needing', 'needs', 'neither', 'never', 'nevertheless', 'new', 'newer', 'newest', 'next', 'nine', 'ninety', 'no', 'nobody', 'non', 'none', 'nonetheless', 'noone', 'nor', 'not', 'nothing', 'now', 'nowhere', 'number', 'numbers', 'o', 'of', 'off', 'often', 'old', 'older', 'oldest', 'on', 'once', 'one', "one's", 'only', 'onto', 'open', 'opened', 'opens', 'or', 'order', 'ordered', 'ordering', 'orders', 'other', 'others', 'otherwise', 'our', 'ours', 'ourselves', 'out', 'over', 'overall', 'own', 'p', 'part', 'parted', 'parting', 'parts', 'per', 'perhaps', 'place', 'places', 'point', 'pointed', 'pointing', 'points', 'possible', 'present', 'presented', 'presenting', 'presents', 'problem', 'problems', 'put', 'puts', 'q', 'quite', 'r', 'rather', 'really', 'recent', 'recently', 'right', 'room', 'rooms', 's', 'said', 'same', 'saw', 'say', 'says', 'second', 'seconds', 'see', 'seem', 'seemed', 'seeming', 'seems', 'seven', 'seventy', 'several', 'she', "she'd", "she'll", "she's", 'should', "shouldn't", 'show', 'showed', 'showing', 'shows', 'sides', 'since', 'six', 'sixty', 'small', 'smaller', 'smallest', 'so', 'some', 'somebody', 'somehow', 'someone', 'something', 'sometime', 'sometimes', 'somewhere', 'state', 'states', 'still', 'stop', 'such', 'sure', 't', 'take', 'taken', 'taking', 'ten', 'than', 'that', "that'll", "that's", "that've", 'the', 'their', 'them', 'themselves', 'then', 'thence', 'there', "there'd", "there'll", "there're", "there's", "there've", 'thereafter', 'thereby', 'therefore', 'therein', 'thereupon', 'these', 'they', "they'd", "they'll", "they're", "they've", 'thing', 'things', 'think', 'thinks', 'thirty', 'this', 'those', 'though', 'thought', 'thoughts', 'thousand', 'three', 'through', 'throughout', 'thru', 'thus', 'to', 'today', 'together', 'too', 'took', 'toward', 'towards', 'trillion', 'turn', 'turned', 'turning', 'turns', 'twenty', 'two', 'u', 'under', 'unless', 'unlike', 'unlikely', 'until', 'up', 'upon', 'us', 'use', 'used', 'uses', 'using', 'v', 'very', 'via', 'w', 'want', 'wanted', 'wanting', 'wants', 'was', "wasn't", 'way', 'ways', 'we', "we'd", "we'll", "we're", "we've", 'well', 'wells', 'were', "weren't", 'what', "what'll", "what's", "what've", 'whatever', 'when', 'whence', 'whenever', 'where', "where's", 'whereafter', 'whereas', 'whereby', 'wherein', 'whereupon', 'wherever', 'whether', 'which', 'while', 'whither', 'who', "who'd", "who'll", "who's", 'whoever', 'whole', 'whom', 'whomever', 'whose', 'why', 'will', 'with', 'within', 'without', "won't", 'work', 'worked', 'working', 'works', 'would', "wouldn't", 'x', 'y', 'year', 'years', 'yes', 'yet', 'you', "you'd", "you'll", "you're", "you've", 'young', 'younger', 'youngest', 'your', 'yours', 'yourself', 'yourselves', 'z'] #list of stopwords
    
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

outputpath = outputsource + "tdmdictionary.txt"                  #assigning the path to the output file.

with open(outputpath, "w") as file:                                     #opening the file and writing the tdm and posting position.
        for token in global_dict:
            file.write(str(token) + "\n")
            file.write(str(tdm[token]) + "\n")
            file.write(str(postings_dict[token]) + "\n")

outputpath = outputsource + "postings.txt"

with open(outputpath, "w") as file:                                #writing the postings file.
    for word in tdm:
        for i in range(1,503):
            filename = "%03d.html" % i
            if word in global_tfidf_list[filename].keys():
                file.write(str(filename) + " " + str(global_tfidf_list[filename][word]) + "\n")
 
end_time = time.time()      #stopping the clock.

print("Execution time in milliseconds : ", (end_time-start_time)*1000)  #calculating the execution time in ms.
