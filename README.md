# Sentiment Analysis Using Natural Language Processing Techniques
### Project Overview
This project leverages Natural Language Processing (NLP) techniques to analyze the sentiment expressed in web content, providing insights into overall sentiment polarity, subjectivity, and readability of overall content.
### Data Sources
Website URLs: The primary data used for this analysis is the "Input.xlsx" file, containing website URLs.  
### Data Extraction
- Identified Pages to perform sentiment analysis
- Implemented web scraping techniques using the Python library BeautifulSoup
- Stored the extracted data into a Python dictionary
### Text Processing
- Cleaned the extracted data by removing unnecessary elements such as HTML tags, special characters, and punctuations
- Removed the stop words (Stored in stop words.txt file) from the text data
- Tokenize the text data into words and sentences using the NLTK library
### Sentiment Analysis
- Utilize sentiment analysis techniques to determine the text data's sentiment polarity (positive, negative, or neutral)
- Assigned sentiment scores to each piece of text based on the presence of positive and negative words(data for positive and negative words is taken from Positive words.txt and Negative words.txt)
- Calculated additional sentiment-related metrics such as subjectivity scores or polarity scores
### Readability Analysis
- Analyzed the readability of the text data using metrics such as average sentence length, and percentage of complex words.
- Calculated the average number of words per sentence and other readability metrics to assess the ease of understanding of the text.
### Data Analysis and Visualization
- Analyzed the sentiment and readability metrics to gain insights into the text data.
- Visualized the results using plots, charts, or graphs to present the findings in a clear and understandable manner.
- Explored relationships between sentiment scores, readability metrics, and other variables to uncover patterns or trends.
- Saved the extracted variables into the "Output.xlsx"
### Variables Derived/ Text Analysis
|Variables|Description|Formula|
|--------|------------|-------|
|Positive Score| No of positive words per webpage |Calculated by assigning +1 for each word found in the positive score CSV and adding all the values|
|Negative Score|No of negative words per web page| Calculated by assigning -1 for each word found in negative words CSV and multiplying its sum with -1|
|Polarity Score| This is the score that determines if a given text is positive or negative in nature|Polarity Score = (Positive Score – Negative Score)/ ((Positive Score + Negative Score) + 0.000001) Range is from -1 to +1|
|Subjectivity Score| Determines if a given text is objective or subjective| Subjectivity Score = (Positive Score + Negative Score)/ ((Total Words after cleaning) + 0.000001)|
|Average Sentence Length|-|Average Sentence Length = the number of words / the number of sentences|
|Percentage of Complex words|Complex words are words in the text that contain more than two syllables|The number of complex words / the number of words|
|Fog Index| Is a readability metric designed to estimate the readability of a piece of text|Fog Index = 0.4 * (Average Sentence Length + Percentage of Complex words)|
|Average Number of Words Per Sentence|-|Average Number of Words Per Sentence = the total number of words / the total number of sentences|
|Complex Word Count|Complex words are words in the text that contain more than two syllables|Assigning +1 for each word having more than two syllables and calculating its sum|
|Word Count|-|Calculated total no of words by removing stop words and punctuations|
|Syllable Count Per Word|-|Calculated by assigning +1 for each vowel found per word|
|Personal Pronouns| I, we, my, ours, us are some personal pronouns |Used regex to find the count of words - “I,” “we,” “my,” “ours,” and “us”|
|Average Word Length|-|Average Word Length = Sum of the total number of characters in each word/Total number of words|




