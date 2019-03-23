"""Name:- Triparna Bhattacharya, UIN:- 677270035, CS 582 Assignment 2 """

import os
import re
from nltk.stem import PorterStemmer
import string
import math
import operator
from nltk.corpus import stopwords
import sys

path_doc = sys.argv[1]
path_relevance = sys.argv[2]
path_queries = sys.argv[3]

di = {}
querystrings = []

di_idf = {}
di_final = {}
stop_words = []
ranks = []
#f = open("stopwords.txt")  # the stopwords list provided in the assignment
#stop_words = f.read().splitlines()

stemmer = PorterStemmer()
punctuations = string.punctuation
reg_pattern = '[' + punctuations + ']'

stop_words = set(stopwords.words('english'))


def doc_preprocessing(file_content):
    pattern = r"<TEXT>(.*?)</TEXT>" # extracting text between the SGML tags named as <TEXT>
    pattern2 = r"<TITLE>(.*?)</TITLE>" # extracting text between the SGML tags named as <TITLE>
    pattern3 = r"<DOCNO>(.*?)</DOCNO>" # extracting document_number between the SGML tags named as <DOCNO>
    document_number = str(re.findall(pattern3, str(file_content), flags=re.DOTALL))
    doc_no = re.sub(reg_pattern, '', document_number).rstrip("\\n").lstrip("\\n")
    doc_no = (doc_no).replace("\\n", "")
    doc_no = int(doc_no[1:-2])
    # print (doc_no)
    file_processed = str(re.findall(pattern, str(file_content), flags=re.DOTALL) + re.findall(pattern2, str(file_content),flags=re.DOTALL))
    file_processed1 = file_processed.replace('\\n', ' ')

    final = []
    for word in file_processed1.split():
        y = re.sub(reg_pattern, '', word).lower()
        y = re.sub(r'[^a-zA-Z]', "", y)  # replacing digits with null space
        y = y.strip("\\n")
        y = stemmer.stem(y)
        if (y != "") & (len(y) > 2) & (y not in stop_words):
            final.append(str(y))

    vocabulary_dictionary(final, doc_no)
    # print(len(di))
    return final


max_freq = []
for x in range(1400):
    max_freq.append(1.0)


def vocabulary_dictionary(final,doc_number):  # creating dictionary of dictionary to store corpus words, document number and term frequency
    global max_freq
    for word in final:
        if word not in di:
            di[word] = {}
        if word in di:
            if doc_number in di[word]:
                di[word][doc_number] += 1
                if (di[word][doc_number] > max_freq[int(doc_number) - 1]):
                    max_freq[int(doc_number) - 1] = di[word][doc_number]
            else:
                di[word][doc_number] = 1


def document_idf(di):  # creating a dictionary for storing only idf values of corpus words
    global di_idf
    for word in di:
        di_idf[word] = (math.log(1400 / len(di[word]), 2))

def create_final_dictionary():  # creating a dictionary with corpus word, document number and tf-idf values of words
    global di_final
    for word in di:
        di_final[word] = {}
        for doc_number in di[word]:
            di_final[word][doc_number] = ((float(di[word][doc_number]) / max_freq[int(doc_number) - 1]) * di_idf[word])

def queries_preprocessing(text, k):  # preprocessing steps of all queries performed
    query_final = []
    for word in text.split():
        y = re.sub(r'[^a-zA-Z]', "", word)
        z = stemmer.stem(y)
        if (z != "") & (len(z) > 2) & (z not in stop_words):
            query_final.append(z)

    return query_dictionary(query_final, k)

def query_dictionary(text, query_number):  # calculating frequency of query word and storing in di2 along with query number.

    di2 = {}
    for word in text:
        if word not in di2:
            di2[word] = {}
        if word in di2:
            if query_number in di2[word]:
                di2[word][query_number] += 1
            else:
                di2[word][query_number] = 1
    return di2

def calculate_query_idf(di2):
    # global query_idf
    query_idf = {}
    for word in di2:
        if word in di:
            query_idf[word] = (math.log(1400 / len(di[word]), 2))

    return query_idf

relevance = []

def find_numerator_of_cosine_similarity(q_no, di2, query_idf):
    relevance.append({})

    for word in di2:
        for x in di2[word]:
            if word in di_final:
                for doc_number in di_final[word]:
                    if doc_number not in relevance[x - 1]:
                        relevance[x - 1][doc_number] = (float(((di2[word][x]) * query_idf[word]) * (di_final[word][doc_number])))
                    else:
                        relevance[x - 1][doc_number] = (float((di2[word][x] * query_idf[word]) * (di_final[word][doc_number]))) + relevance[x - 1][doc_number]

    calculate_cosine_similarity(relevance, di2, q_no)

    # print relevance
solution = {}

def calculate_cosine_similarity(relevance, di2, q_no):
    weight = 0
    for word in di2:
        if word in di_idf:
            weight += math.pow((di_idf[word] * di2[word][q_no]), 2)
    query_length = math.sqrt(weight)

    similarity_list = {}

    for doc in range(1400):
        numerator = 0
        denomenator = 1
        if doc + 1 in relevance[q_no - 1]:
            numerator = relevance[q_no - 1][doc + 1]
        denomenator = query_length * doc_length_vector[doc + 1]
        sim = numerator / denomenator
        similarity_list[doc] = sim
        temp_list = sorted(similarity_list.items(), key=operator.itemgetter(1), reverse=True)

    #solution[q_no] = temp_list
    # print similarity_list
    # print("Top TEN documents of query- " + str(q_no))
    abc = []
    for x in temp_list[:500]:
        abc.append(x[0] + 1)
    # print(abc)
    ranks.append(abc)

doc_length_vector = {}


def calculate_document_vector_length():
    for word in di_final:
        for doc in di_final[word]:
            doc = int(doc)
            if doc in doc_length_vector:
                doc_length_vector[doc] += di_final[word][doc] * di_final[word][doc]
            else:
                doc_length_vector[doc] = di_final[word][doc]

    for doc_no in doc_length_vector:
        doc_length_vector[doc_no] = math.sqrt(doc_length_vector[doc_no])


relevant_di = {}
f = open(path_relevance)  # the stopwords list provided in the assignment
relevant_words = f.read().splitlines()
for rel in relevant_words:
    query_id = int(rel.split()[0])
    doc_id = int(rel.split()[1])
    if query_id not in relevant_di:
        relevant_di[query_id] = [doc_id]
    else:
        relevant_di[query_id].append(doc_id)

#print(relevant_di)


def calculate_precision_recall(ranks, x):

    tot_pre = 0
    tot_rec = 0
    size = len(ranks)

    for a in range(len(ranks)):
        b = ranks[a][:x]
        num = 0
        for z in b:
            if z in relevant_di[a+1]:
                num += 1

        precision = num/x
        recall = num/len(relevant_di[a+1])
        tot_pre += precision
        tot_rec += recall
        print(str(a+1) + ". Precision- " + str(precision) + " Recall- " + str(recall))
    print()
    print("Avg Precision- " + str(tot_pre/size) + " Avg Recall- " + str(tot_rec/size))
    print()
    print("===========================================")

def main():
    path = path_doc
    c = 0
    for file in sorted(os.listdir(path)):
        with open(path + file, 'r') as x:
            # print(file)
            vocabulary = x.readlines()
            word_list = doc_preprocessing(vocabulary)
        # print word_list
    # print di
    #print(len(di))
    document_idf(di)
    create_final_dictionary()
    calculate_document_vector_length()

    f = open(path_queries)
    querystrings = f.read()
    # print querystrings
    q_no = 1
    for line in querystrings.split('\n'):
        di2 = queries_preprocessing(line, q_no)
        query_idf = calculate_query_idf(di2)
        find_numerator_of_cosine_similarity(q_no, di2, query_idf)
        q_no += 1
    #print(ranks)
    ab = [10, 50, 100, 500]
    for x in ab:
        print("Top",x,"documents in rank list")
        calculate_precision_recall(ranks, x)
    print("Process Completed")


main()
