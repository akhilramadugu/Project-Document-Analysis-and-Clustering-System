from bs4 import BeautifulSoup       #importing BeautifulSoup package from BS4.
import re       #importing regular expression package.
import sys      #importung sys package.
import time     #importing time package.

inputsource = sys.argv[1]           #variable to store inputsource i.e., path to input files which we will be taking from command line interface.
outputsource = sys.argv[2]          #variable to store outputsource i.e., path to store output files which we will be taking from command line interface.

global_dict = dict()            #global dictionary to maintain entire catalog of words present in all the 503 documents along with their combined frequency.

start_time = time.time()        #variable to store start time in seconds.

for i in range(1,503):          #looping through all the 503 html documents.

    local_dict = dict()         #local dictionary to maintain individual catalog of words present in each document along with their frequency in that particular document.

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

    outputfile = "%03d.txt" % i                             #assigning the name to the output file.
    outputpath = outputsource + outputfile                  #assigning the path to the output file.

    
    for word in final_words:                                #storing the words in the local_dictionary.
        if word in local_dict:
            local_dict[word] = local_dict[word] + 1         #if the word already exists in the dictionary we increase its frequency.
        else:
            local_dict[word] = 1                            #else we create a new record and mark its frequency to 1.
    
    for word in final_words:                                #storing the words in the global_dictionary.
        if word in global_dict:
            global_dict[word] = global_dict[word] + 1       #if the word already exists in the dictionary we increase its frequency.
        else:
            global_dict[word] = 1                           #if the word doesn't exist, we create a new record.
        
    
    with open(outputpath, "w") as file:                     #opening the output file and writing all the words and their frequencies.
        for word in local_dict:
            file.write(word + ":" + str(local_dict[word]) + "\n")
    
end_time = time.time()      #stopping the clock.

print("Execution time in milliseconds : ", (end_time-start_time)*1000)  #caluculating the execution time in ms.

globalpath = outputsource + "globaldictsortedbykeys.txt"                #filename to store the global dictionary sorted by keys.

with open(globalpath, "w") as file:                                     #opening the file and writing the global dictionary sorted by keys.
    for word in dict(sorted(global_dict.items())):
        file.write(word + ":" + str(global_dict[word]) + "\n")

globalpath = outputsource + "globaldictsortedbyvalues.txt"              #filename to store the global dictionary sorted by values.

with open(globalpath, "w") as file:                                     #opening the file and writing the global dictionary sorted by values.
    for word in dict(sorted(global_dict.items(), key = lambda x:x [1], reverse=True)):
        file.write(word + ":" + str(global_dict[word]) + "\n")
