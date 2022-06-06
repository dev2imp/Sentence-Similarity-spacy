import Model
import spacy

# Scikit Learn to cacluate cosine similarity
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

class SimilarityClass:
    # do necessary cleaning for texts,remove some punctuations
    # length of both texts
    # similarity between both texts
    length1 = 0
    length2 = 0
    def __init__(self):
        pass
    def run(self, text1, text2,model):
        nlp = spacy.load(str(model))#Downloading the model that we will use
        doc1 = nlp(text1)
        doc2 = nlp(text2)
        similarity=doc1.similarity(doc2)
        length1 = len(text1)
        length2 = len(text2)
        print("model->"+str(model))
        CosinesimilarityFun(text1,text2)
        #Create Model and return it to main
        return Model.ResultModel(length1 , length2 , similarity,model)
def CosinesimilarityFun(input1,input2):
    #get both input from user
    documents = [input1 ,input2]
    count_vectorizer = CountVectorizer()
    sparse_matrix = count_vectorizer.fit_transform(documents)
    doc_term_matrix = sparse_matrix.todense()

    df = pd.DataFrame(doc_term_matrix,
                      columns=count_vectorizer.get_feature_names(),
                      index=['input1', 'input2'])
    print(df)
    print(cosine_similarity(df,df))
