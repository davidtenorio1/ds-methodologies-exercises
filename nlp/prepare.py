import unicodedata
import re
import json
import nltk
from nltk.stem import WordNetLemmatizer 
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords
import pandas as pd
import acquire

original_df = acquire.get_blog_posts()
edited_df = original_df.copy()

test = '''The rumors are true! The time has arrived. Codeup has officially opened applications to our new Data Science career accelerator, with only 25 seats available! This immersive program is one of a kind in San Antonio, and will help you land a job in Glassdoor’s #1 Best Job in America.
Data Science is a method of providing actionable intelligence from data. The data revolution has hit San Antonio, resulting in an explosion in Data Scientist positions across companies like USAA, Accenture, Booz Allen Hamilton, and HEB. We’ve even seen UTSA invest $70 M for a Cybersecurity Center and School of Data Science. We built a program to specifically meet the growing demands of this industry.
Our program will be 18 weeks long, full-time, hands-on, and project-based. Our curriculum development and instruction is led by Senior Data Scientist, Maggie Giust, who has worked at HEB, Capital Group, and Rackspace, along with input from dozens of practitioners and hiring partners. Students will work with real data sets, realistic problems, and the entire data science pipeline from collection to deployment. They will receive professional development training in resume writing, interviewing, and continuing education to prepare for a smooth transition to the workforce.
We focus on applied data science for immediate impact and ROI in a business, which is how we can back it all up with a 6 month tuition refund guarantee – just like our existing Web Dev program. We’re focusing on Data Science with Python, SQL, and ML, covered in 14 modules: 1) Fundamentals; 2) Applied statistics; 3) SQL; 4) Python; 5) Supervised machine learning – regression; 6) Supervised machine learning – classification; 7) Unsupervised machine learning – clustering; 8) Time series analysis; 9) Anomaly detection; 10) Natural language processing; 11) Distributed machine learning; 12) Advanced topics (deep learning, NoSQL, cloud deployment, etc.); 13) Storytelling with data; and 14) Domain expertise development.
Applications are now open for Codeup’s first Data Science cohort, which will start class on February 4, 2019. Hurry – there are only 25 seats available! To further our mission of cultivating inclusive growth, scholarships will be available to women, minorities, LGBTQIA+ individuals, veterans, first responders, and people relocating to San Antonio.
If you want to learn about joining our program or hiring our graduates, email datascience@codeup.com!'''


def basic_clean(string):
    string = string.lower()
    string = unicodedata.normalize('NFKD', string).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    string = re.sub(r"[^a-z0-9'\s]", '', string)
    return string


def tokenize(string):
    tokenizer = nltk.tokenize.ToktokTokenizer()
    return tokenizer.tokenize(string, return_str=True)


def stem(string):
    ps = nltk.porter.PorterStemmer()
    stems = [ps.stem(word) for word in string.split()]
    string_stemmed = ' '.join(stems)
    return string_stemmed


def lemmatize(string):
    wnl = WordNetLemmatizer()
    lemmas = [wnl.lemmatize(word) for word in string.split()]
    string_lemmatized = ' '.join(lemmas)
    return string_lemmatized


def remove_stopwords(string, extra_words = [], exclude_words = []):
    stopword_list = stopwords.words('english')
    stopword_list = set(stopword_list) - set(exclude_words)
    stopword_list = stopword_list.union(set(extra_words))
    words = string.split()
    filtered_words = [w for w in words if w not in stopword_list]
    string_without_stopwords = ' '.join(filtered_words)
    return string_without_stopwords


def prep_blog_posts():
    df = acquire.get_blog_posts()
    return prep_articles(df)


def prep_articles(df):
    df["original"] = df.body
    df["stemmed"] = df.body.apply(basic_clean).apply(stem)
    df["lemmatized"] = df.body.apply(basic_clean).apply(lemmatize)
    df["clean"] = df.body.apply(basic_clean).apply(remove_stopwords)
    df.drop(columns=["body"], inplace=True)
    return df