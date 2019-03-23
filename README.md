# Inverted-Index-TF-IDF-model
Implement an indexing scheme based on the vector space model

=======================================================================

Name:- TRIPARNA BHATTACHARYA, UIN: 677270035, Net ID:- tbhatt22
=======================================================================

Python Version:- 3.7
IDE used:- PyCharm

========================================================================
Running Instructions:- Three arguments should be passed:- Path of Document, Path of Relevance text, Path of Queries

Example:- python3 IR_Homework2.py /Users/triparnabhattacharya/PycharmProjects/IRAssignment2/cranfieldDocs/ /Users/triparnabhattacharya/PycharmProjects/IRAssignment2/relevance.txt /Users/triparnabhattacharya/PycharmProjects/IRAssignment2/queries.txt

=======================================================================

Functions Implemented:-

1.def doc_preprocessing(file_content):- Called for preprocessing the corpus, each file is passed at a time. It extracts the text between the two SGML tags mentioned, performs stemming, removes stop-words, numbers and less than 2 character words. Document number is also extracted from in between the tags. Used nltk.corpus import stop-words for removing stop-words from the corpus and the query.

2.def vocabulary_dictionary(final, doc_number):- This is called from doc_preprocessing(file_content) with the arguments file and doc_number extracted from each file of the corpus to create a dictionary of       dictionary (inverted index) where Word as the key and sub-dictionary document number and term frequency as the key and values. Term frequency is normalized in my code.

3.def queries_preprocessing(text, k):- Called for preprocessing the query files, each file is passed at a time. It performs stemming, removes stop-words, numbers and less than 2 character words.

4. def query_dictionary(text, query_number):- Creating a dictionary with each word of the query as index and value is a sub dictionary where query number is key and value is the term frequency of the word in that query.

5. def find_numerator_of_cosine_similarity(q_no, di2, query_idf):- Calculating numerator of cosine similarity by taking dot product of the tf-idf of the common words between the query and the corpus.

6. def calculate_cosine_similarity(relevance, di2, q_no):- Calculating the denominator by summing the square of weight of each word in query and multiply it with the sum of square of weight of all the words of the relevant documents. 

7. def calculate_precision_recall(ranks, x):- Calculating precision, recall and average precision & recall for the top 10, 50, 100, 500 documents for each query provided. 


=========================================================================
Results:-


Top 10 documents in rank list
1. Precision- 0.0 Recall- 0.0
2. Precision- 0.2 Recall- 0.13333333333333333
3. Precision- 0.2 Recall- 0.13333333333333333
4. Precision- 0.1 Recall- 0.05555555555555555
5. Precision- 0.1 Recall- 0.05263157894736842
6. Precision- 0.3 Recall- 0.16666666666666666
7. Precision- 0.6 Recall- 0.6666666666666666
8. Precision- 0.2 Recall- 0.5
9. Precision- 0.2 Recall- 0.25
10. Precision- 0.2 Recall- 0.08333333333333333

Avg Precision- 0.21000000000000002 Avg Recall- 0.20415204678362575

==========================================================================
Top 50 documents in rank list
1. Precision- 0.0 Recall- 0.0
2. Precision- 0.1 Recall- 0.3333333333333333
3. Precision- 0.12 Recall- 0.4
4. Precision- 0.04 Recall- 0.1111111111111111
5. Precision- 0.14 Recall- 0.3684210526315789
6. Precision- 0.12 Recall- 0.3333333333333333
7. Precision- 0.16 Recall- 0.8888888888888888
8. Precision- 0.06 Recall- 0.75
9. Precision- 0.1 Recall- 0.625
10. Precision- 0.04 Recall- 0.08333333333333333

Avg Precision- 0.088 Avg Recall- 0.38934210526315793

==========================================================================
Top 100 documents in rank list
1. Precision- 0.0 Recall- 0.0
2. Precision- 0.08 Recall- 0.5333333333333333
3. Precision- 0.09 Recall- 0.6
4. Precision- 0.05 Recall- 0.2777777777777778
5. Precision- 0.13 Recall- 0.6842105263157895
6. Precision- 0.09 Recall- 0.5
7. Precision- 0.09 Recall- 1.0
8. Precision- 0.03 Recall- 0.75
9. Precision- 0.05 Recall- 0.625
10. Precision- 0.03 Recall- 0.125

Avg Precision- 0.064 Avg Recall- 0.5095321637426901

===========================================================================
Top 500 documents in rank list
1. Precision- 0.002 Recall- 1.0
2. Precision- 0.03 Recall- 1.0
3. Precision- 0.03 Recall- 1.0
4. Precision- 0.03 Recall- 0.8333333333333334
5. Precision- 0.038 Recall- 1.0
6. Precision- 0.032 Recall- 0.8888888888888888
7. Precision- 0.018 Recall- 1.0
8. Precision- 0.008 Recall- 1.0
9. Precision- 0.016 Recall- 1.0
10. Precision- 0.026 Recall- 0.5416666666666666

Avg Precision- 0.023 Avg Recall- 0.9263888888888889

============================================================================
Process Completed

============================================================================







