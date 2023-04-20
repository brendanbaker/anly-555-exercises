'''
Discussion 7: Replication of Locality Sensitive Hashing for Recommender Systems

Brendan Baker

Tutorial Here by Ray McLendon: https://www.learndatasci.com/tutorials/building-recommendation-engine-locality-sensitive-hashing-lsh-python/

'''

import numpy as np
import pandas as pd
import re
import time
from datasketch import MinHash, MinHashLSHForest


#Preprocess will split a string of text into individual tokens/shingles based on whitespace.
def preprocess(text):
    text = re.sub(r'[^\w\s]','',text)
    tokens = text.lower()
    tokens = tokens.split()
    return tokens

# Example preprocessing
text = 'The devil went down to Georgia'
print('The shingles (tokens) are:', preprocess(text))


#Number of Permutations
permutations = 128

#Number of Recommendations to return
num_recommendations = 1

# Forest function
def get_forest(data, perms):
    '''
    This function creates a MinHashLSHForest object and returns it.
    '''
    start_time = time.time()
    
    minhash = []
    
    for text in data['text']:
        tokens = preprocess(text)
        m = MinHash(num_perm=perms)
        for s in tokens:
            m.update(s.encode('utf8'))
        minhash.append(m)
        
    forest = MinHashLSHForest(num_perm=perms)
    
    for i,m in enumerate(minhash):
        forest.add(i,m)
        
    forest.index()
    
    print('It took %s seconds to build forest.' %(time.time()-start_time))
    
    return forest

def predict(text, database, perms, num_results, forest):
    '''
    Predict function takes in a string of text, a database, the number of permutations, the number of results, and a forest object.
    '''
    start_time = time.time()
    
    tokens = preprocess(text)
    m = MinHash(num_perm=perms)
    for s in tokens:
        m.update(s.encode('utf8'))
        
    idx_array = np.array(forest.query(m, num_results))
    if len(idx_array) == 0:
        return None # if your query is empty, return none
    
    result = database.iloc[idx_array]['title']
    
    print('It took %s seconds to query forest.' %(time.time()-start_time))
    
    return result


# Read data
db = pd.read_csv('./data/papers.csv')
db['text'] = db['title'] + ' ' + db['abstract']
forest = get_forest(db, permutations)

# Set number of recommendations and title -- given example
num_recommendations = 5
title = 'Using a neural net to instantiate a deformable model'
result = predict(title, db, permutations, num_recommendations, forest)
print('\n Top Recommendation(s) is(are) \n', result)
result.to_csv('./data/recommendations.csv')

'''
Assignment: 

Using the code provided, repeat the experiment run in the article: Predicting NIPS articles based on titles.
Scroll through the NIPS article titles and identify 1 that would be of interest to you. Next find the top 5 recommendations using the LSH method.
Assess the recommendations -- are these titles of interest similar to your original paper titles. Share your results in the discussion!!!
'''
title = "Locality and low-dimensions in the prediction of natural experience from fMRI"
result = predict(title, db, permutations, num_recommendations, forest)
print('\n Top Recommendation(s) is(are) \n', result)

'''
Results: 

1. Neural Network Weight Matrix Synthesis Using Optimal Control Techniques
2. Using a neural net to instantiate a deformable model
3. A Self-Organizing Integrated Segmentation and Recognition Neural Net
4. Analytic Solutions to the Formation of Feature-Analysing Cells of a Three-Layer Feedforward Visual Information Processing Neural Net
5. Inferring Neural Firing Rates from Spike Trains Using Gaussian Processes

Comments: Interestingly, 4 of the 5 recommendations are related to nerual networks, but the original paper is about fMRI (not neural networks).  While neural networks are brain-inspired,
they are not 
'''