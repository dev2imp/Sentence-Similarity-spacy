class ResultModel():
    length1 = 0
    length2 = 0
    similarity = 0
    model=""

    def __init__(self, length1, length2, similarity,model):
        self.length1 = length1
        self.length2 = length2
        self.similarity = similarity
        self.model=model
