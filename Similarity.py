class SimilarityClass:
    # do necessary cleaning for texts,remove some punctuations
    # length of both texts
    # similarity between both texts
    length1 = 0
    length2 = 0
    def __init__(self, text1, text2):
        length1 = len(text1)
        length2 = len(text2)
        print(length1)
        print(length2)
        print("Similarity Functions " + text1 + text2)
