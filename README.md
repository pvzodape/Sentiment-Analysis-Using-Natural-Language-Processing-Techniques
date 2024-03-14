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
- Assigned sentiment scores to each piece of text based on the presence of positive and negative words(data for positive and negative words is taken form Positive words.txt and Negative words.txt)
- Calculated additional sentiment-related metrics such as subjectivity scores or polarity scores
### Readability Analysis
- Analyzed the readability of the text data using metrics such as average sentence length, percentage of complex words, and Flesch-Kincaid Grade Level.
- Calculated the average number of words per sentence and other readability metrics to assess the ease of understanding of the text.
### Data Analysis and Visualization
- Analyzed the sentiment and readability metrics to gain insights into the text data.
- Visualized the results using plots, charts, or graphs to present the findings in a clear and understandable manner.
- Explored relationships between sentiment scores, readability metrics, and other variables to uncover patterns or trends.
- Saved the extracted matrices into the "Output.xlsx" 




