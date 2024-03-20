#!/usr/bin/env python
# coding: utf-8

# # Data Extraction

# In[61]:


import pandas as pd
from bs4 import BeautifulSoup
import requests
import os
import nltk
from nltk.corpus import cmudict
nltk.download('punkt')
nltk.download('cmudict')
import string
import re


# In[48]:


df=pd.read_excel('Input.xlsx')
urls=df['URL'].tolist()
print(urls)


# In[3]:


for url in urls:
    print(url)


# In[4]:


excel_file="Input.xlsx"
df=pd.read_excel(excel_file)
urls=df['URL'].tolist()
print(urls)


# In[5]:


for i, url in enumerate(urls, start=1):
    page = requests.get(url)

    if page.status_code == 200:
        print(f'Data Fetched Successfully: {i}')
        soup = BeautifulSoup(page.content, 'html.parser')

        title = soup.find(attrs={'class': 'entry-title'})
        if title:
            title_text = title.text.strip()
        else:
            title_text = 'No title found'

        content = soup.find(attrs={'class': 'td-post-content tagdiv-type'})
        if content:
            content_text = content.text.replace('\n', '').strip()
        else:
            content_text = 'No content found'

        file_path = f'blackassign{str(i).zfill(4)}.txt'
        
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(f'{title_text}\n{content_text}')


# # Text Analysis/Data Analysis

# # 1 Sentiment Analysis 
# 1.1 Cleaning using stop word list

# In[7]:


# reading the .txt file back into jupyter notebook
directory_path ='D:\\NLP Data'

url_id_to_content = {}

for file_name in os.listdir(directory_path):
    if file_name.endswith(".txt"): 
        url_id = os.path.splitext(file_name)[0]
        
        file_path = os.path.join(directory_path, file_name)
        with open(file_path, 'r', encoding='ISO-8859-1') as file:
            content = file.read()
        
        url_id_to_content[url_id] = content


# In[8]:


os.getcwd()


# In[9]:


url_id_to_content


# In[10]:


type(url_id_to_content)


# In[12]:


stop_words_auditor=open('StopWords_Auditor.txt', 'r')
f= stop_words_auditor.readlines()
stopwordsauditor=[]
for lines in f:
    if lines[-1]=='\n':
        stopwordsauditor.append(lines[:-1])
    else:
        stopwordsauditor.append(lines)
stopwordsauditor


# In[ ]:





# In[13]:


stop_words_currencies=open('StopWords_Currencies.txt', 'r')
f= stop_words_currencies.readlines()
stopwordscurrencies=[]
for lines in f:
    if lines[-1]=='\n':
        stopwordscurrencies.append(lines[:-1])
    else:
        sstopwordscurrencies.append(lines)
stopwordscurrencies


# In[14]:


stop_words_datesandnumbers=open('StopWords_DatesandNumbers.txt', 'r')
f= stop_words_datesandnumbers.readlines()
stopwordsdatesandnumbers=[]
for lines in f:
    if lines[-1]=='\n':
        stopwordsdatesandnumbers.append(lines[:-1])
    else:
        stopwordsdatesandnumbers.append(lines)
stopwordsdatesandnumbers


# In[15]:


stop_words_generic=open('StopWords_Generic.txt', 'r')
f= stop_words_generic.readlines()
stopwordsgeneric=[]
for lines in f:
    if lines[-1]=='\n':
        stopwordsgeneric.append(lines[:-1])
    else:
        stopwordsgeneric.append(lines)
stopwordsgeneric


# In[16]:


stop_words_genericlong=open('StopWords_GenericLong.txt', 'r')
f= stop_words_genericlong.readlines()
stopwordsgenericlong=[]
for lines in f:
    if lines[-1]=='\n':
        stopwordsgenericlong.append(lines[:-1])
    else:
        stopwordsgenericlong.append(lines)
stopwordsgenericlong


# In[17]:


stop_words_geographic=open('StopWords_Geographic.txt', 'r')
f= stop_words_geographic.readlines()
stopwordsgeographic=[]
for lines in f:
    if lines[-1]=='\n':
        stopwordsgeographic.append(lines[:-1])
    else:
        stopwordsgeographic.append(lines)
stopwordsgeographic


# In[18]:


stop_words_names=open('StopWords_Names.txt', 'r')
f= stop_words_names.readlines()
stopwordsname=[]
for lines in f:
    if lines[-1]=='\n':
        stopwordsname.append(lines[:-1])
    else:
        stopwordsname.append(lines)
stopwordsname


# In[19]:


set_stopwordsauditor = set(stopwordsauditor)
set_stopwordscurrencies =set(stopwordscurrencies)
set_stopwordsnumbers = set(stopwordsdatesandnumbers)
set_stopwordsgeneric = set(stopwordsgeneric)
set_stopwordsgenericlong = set(stopwordsgenericlong)
set_stopwordsgeographic = set(stopwordsgeographic)
set_stopwordsname = set(stopwordsname)
Stop_words_combined=set().union(set_stopwordsauditor,set_stopwordscurrencies,set_stopwordsnumbers,set_stopwordsgeneric,set_stopwordsgenericlong,set_stopwordsgeographic,set_stopwordsname)


# In[20]:


Stop_words_combined


# In[21]:


nltk.download('punkt')


# In[22]:


cleaned_url_id_to_content = {}

def remove_stop_words(text, stop_words):
    words = text.split()
    filtered_words = [word for word in words if word.lower() not in stop_words]
    return ' '.join(filtered_words)

for url_id, content in url_id_to_content.items():
    cleaned_content = remove_stop_words(content, Stop_words_combined)
    cleaned_url_id_to_content[url_id] = cleaned_content


# In[23]:


cleaned_url_id_to_content


# 1.2 Creating a dictonary of positive and negative words

# In[24]:


positive_words=open('positive-words.txt', 'r')
f= positive_words.readlines()
positivewords=[]
for lines in f:
    if lines[-1]=='\n':
        positivewords.append(lines[:-1])
    else:
        positivewords.append(lines)
positivewords 


# In[25]:


type(positivewords) 


# In[26]:


positive_words_dict={word:'positive' for word in positivewords if word not in Stop_words_combined}


# In[27]:


positive_words_dict


# In[28]:


negative_words=open('negative-words.txt', 'r')
f= negative_words.readlines()
negativewords=[]
for lines in f:
    if lines[-1]=='\n':
        negativewords.append(lines[:-1])
    else:
        negativewords.append(lines)
negativewords


# In[29]:


negative_words_dict={word:'negative' for word in negativewords if word not in Stop_words_combined}
negative_words_dict


# # Extracting Derived variables

# In[30]:


positive_scores = {}
for url_id, content in cleaned_url_id_to_content.items():
    words=content.lower().split()
    positive_score=sum(1 for word in words if word in positive_words_dict)
    positive_scores[url_id] = positive_score
positive_scores
    
#(assigning value of +1 for each positive word found in positive dictonary and adding up the value)


# In[31]:


negative_scores={}
for url_id, content in cleaned_url_id_to_content.items():
    word= content.lower().split()
    negative_score =sum(-1 for word in word if word in negative_words_dict)*-1
    negative_scores[url_id]= negative_score
negative_scores
#(assign -1 for each negative word and adding up the value *-1 )


# In[32]:


polarity_scores= {}
for url_id in cleaned_url_id_to_content:
    positive_score= positive_scores.get(url_id,0)
    negative_score= negative_scores.get(url_id,0)
    
    denominator =  positive_score +negative_score + 0.000001
    polarity_score=  positive_score - negative_score/ denominator
    polarity_scores[url_id] = polarity_score
polarity_scores

#(checks the positivity and negtivity of a word)(Positive Score – Negative Score)/ ((Positive Score + Negative Score) + 0.000001)


# In[33]:


total_words_after_cleaning = {}
for url_id,content in cleaned_url_id_to_content.items():
    words_after_cleaning=content.split()
    total_words=len(words_after_cleaning)
    total_words_after_cleaning[url_id]=total_words
total_words_after_cleaning   


# In[69]:


subjectivity_scores = {}
for url_id in cleaned_url_id_to_content:
    total_words_after_cleaning_c = total_words_after_cleaning.get(url_id,0)
    positive_score_c= positive_scores.get(url_id, 0)
    negative_score_c= negative_scores.get(url_id, 0)
    denominator= total_words_after_cleaning_c + 0.000001
    subjectivity_score= positive_score_c +negative_score_c/denominator
    subjectivity_scores[url_id] = subjectivity_score
subjectivity_scores
#(Positive Score + Negative Score)/ ((Total Words after cleaning) + 0.000001)


# # Analysis of Readibility

# In[44]:


average_sentence_length = {}
for url_id, content in cleaned_url_id_to_content.items():
    words = nltk.word_tokenize(content)
    word_count = len(words)

    sentence= nltk.sent_tokenize(content)
    sentence_count=len(sentence)
    
    average_sentence_length[url_id] = word_count / sentence_count
average_sentence_length

#(the number of words / the number of sentences)


# In[50]:


pronouncing_dict = cmudict.dict()

percentage_of_complex_word = {}

# Function to count syllables in a word
def count_syllables(word):
    if word.lower() in pronouncing_dict:
        return max([len(list(y for y in x if y[-1].isdigit())) for x in pronouncing_dict[word.lower()]])
    else:
        return 0

# Calculate the percentage of complex words
for url_id, content in cleaned_url_id_to_content.items():
    words = nltk.word_tokenize(content)
    total_words = len(words)
    
    # Count the number of complex words
    complex_words = [word for word in words if count_syllables(word) > 2]
    num_complex_words = len(complex_words)
    
    # Calculate the percentage of complex words
    percentage_complex = (num_complex_words / total_words) * 100

    # Store the result in the dictionary
    percentage_of_complex_word[url_id] = percentage_complex

# Print the result
print(percentage_of_complex_word)


# In[51]:


type(percentage_of_complex_word)


# In[53]:


fog_indexs ={}
for url_id, content in cleaned_url_id_to_content.items():
    average_sentence_length_c = average_sentence_length[url_id]
    percentage_of_complex_word_c = percentage_of_complex_word[url_id]
    fog_index= 0.4*(average_sentence_length_c + percentage_of_complex_word_c)
    fog_indexs[url_id]= fog_index
fog_indexs
#(0.4 * (Average Sentence Length + Percentage of Complex words) 


# In[56]:


average_no_of_words_per_sentence={}
for url_id in cleaned_url_id_to_content.items():
    words = nltk.word_tokenize(content)
    sentences = nltk.sent_tokenize(content)
    
    total_words = len(words)
    total_sentences = len(sentences)
    
    if total_sentences > 0:  
        average_words_per_sentence = total_words / total_sentences
    else:
        average_words_per_sentence = 0
        
    average_no_of_words_per_sentence[url_id] = average_words_per_sentence
print(average_no_of_words_per_sentence)

#(the total number of words pre sentence / the total number of sentences) 


# In[57]:


pronouncing_dict = cmudict.dict()

complex_word_count = {}

def count_syllables(word):
    if word.lower() in pronouncing_dict:
        return max([len(list(y for y in x if y[-1].isdigit())) for x in pronouncing_dict[word.lower()]])
    else:
        return 0


for url_id, content in cleaned_url_id_to_content.items():
    words = nltk.word_tokenize(content)

   
    complex_words = [word for word in words if count_syllables(word) > 2]
    num_complex_words = len(complex_words)

    
    complex_word_count[url_id] = num_complex_words

print(complex_word_count)

#(Complex words are words in the text that contain more than two syllables) 


# In[60]:


word_count = {}

def remove_stopwords_and_punctuation(words):
    stop_words = set(["your", "stop", "words", "here"])  # Add your stop words
    words_no_stop = [word.lower() for word in words if word.lower() not in stop_words and word not in string.punctuation]
    return words_no_stop

for url_id, content in cleaned_url_id_to_content.items():
    words = nltk.word_tokenize(content)

    words_no_stop = remove_stopwords_and_punctuation(words)

    num_words = len(words_no_stop)

    word_count[url_id] = num_words
print(word_count)
#(count the no of words by removing stop words and punctuations)


# In[58]:


syllable_count_per_word = {}

def count_syllables(word):
    if word.lower() in pronouncing_dict:
        return max([len(list(y for y in x if y[-1].isdigit())) for x in pronouncing_dict[word.lower()]])
    else:
        return 0

for url_id, content in cleaned_url_id_to_content.items():
    words = nltk.word_tokenize(content)

    
    syllables_per_word = [count_syllables(word) if not word.lower().endswith(('es', 'ed')) else count_syllables(word) - 1 for word in words]

  
    syllable_count_per_word[url_id] = syllables_per_word


print(syllable_count_per_word)
#(by counting no of vowels in a word, some exceptions are the words thet ends with es ed)


# In[62]:


personal_pronouns = {}

pronoun_list = ["I", "we", "my", "ours", "us"]

def count_personal_pronouns(text):
    pronoun_counts = {pronoun: len(re.findall(r'\b' + pronoun + r'\b', text, flags=re.IGNORECASE)) for pronoun in pronoun_list}
    pronoun_counts["us"] -= len(re.findall(r'\bUS\b', text, flags=re.IGNORECASE))
    
    return pronoun_counts

for url_id, content in cleaned_url_id_to_content.items():
    pronoun_counts = count_personal_pronouns(content)
    
    personal_pronouns[url_id] = pronoun_counts

print(personal_pronouns)
#(we use regex to find the counts of the words - “I,” “we,” “my,” “ours,” and “us”. Special care is taken so that the country name US is not included in the list.)


# In[63]:


average_word_length = {}

for url_id, content in cleaned_url_id_to_content.items():
    words = nltk.word_tokenize(content)


    total_characters = sum(len(word) for word in words)

    total_words = len(words)

    if total_words > 0:  # Ensure there is at least one word to avoid division by zero
        avg_word_length = total_characters / total_words
    else:
        avg_word_length = 0

    average_word_length[url_id] = avg_word_length

print(average_word_length)
#(Sum of the total number of characters in each word/Total number of words)


# In[70]:


data={
    'URL_ID': list(cleaned_url_id_to_content.keys()),
    'POSITIVE SCORE': list(positive_scores.values()),
    'NEGATIVE SCORE': list(negative_scores.values()),
    'POLARITY SCORE': list(polarity_scores.values()),
    'SUBJECTIVITY SCORE': list(subjectivity_scores.values()),
    'AVG SENTENCE LENGTH': list(average_sentence_length.values()),
    'PERCENTAGE OF COMPLEX WORDS': list(percentage_of_complex_word.values()),
    'FOG INDEX': list(fog_indexs.values()),
    'AVG NUMBER OF WORDS PER SENTENCE': list(average_no_of_words_per_sentence.values()),
    'COMPLEX WORD COUNT': list(complex_word_count.values()),
    'WORD COUNT': list(word_count.values()),
    'SYLLABLE PER WORD': list(syllable_count_per_word.values()),
    'PERSONAL PRONOUNS': list(personal_pronouns.values()),
    'AVG WORD LENGTH': list(average_word_length.values())
}

df = pd.DataFrame(data)
df.to_excel('Output.xlsx')




# In[ ]:





# In[ ]:





# In[ ]:




