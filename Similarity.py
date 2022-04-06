import Model
class SimilarityClass:
    # do necessary cleaning for texts,remove some punctuations
    # length of both texts
    # similarity between both texts
    length1 = 0
    length2 = 0

    def __init__(self):
        pass

    def run(self, text1, text2):
        length1 = len(text1)
        length2 = len(text2)
        return Model.ResultModel(length1 , length2 , 0)

    def get_result(self):
        return self.length1
