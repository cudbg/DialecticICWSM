# DialecticICWSM

This repository contains the code and data for

Title: Leveraging Quality Prediction Models for Automatic Writing Feedback
Authors: Hamed Nilforoshan and Eugene Wu
Conference: ICWSM 2018

We collected all data on Amazon's Mechanical Turk, per the experiment design descriptions in the above paper. Data is organized as follows:

/data/airbnb.csv and data/amazon.csv - Data from our Evaluation experiments of the system feedback
/data/segment/ Directory containing data for our evaluation of the weak supervision hypothesis

Code is in /src/ and contains the following packages

apriori.py - Apriori algorithm to extract jargon from documents
featureExtraction.py - Extract feature vector from document text
generateExplainerNew.py	- Perturbation Analysis
lda.py - LDA in gensim
liwc.py - LIWC python interface for web application
segmentation.py - TopicTiling
