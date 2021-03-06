#document similarity
#by Yang Tian and Xi Chen
# input query tfidf and docs-tfidf
# output a rank list for the indices of docs
import math

def vectorlength(vec):
    length = float(0)
    for num in vec:
        length += num*num
    return math.sqrt(length)

def simDistance(w1,w2):
    sim = float(0)
    for wi1, wi2 in zip(w1, w2):
        sim += wi1*wi2
    sim = sim/(vectorlength(w1)*vectorlength(w2))
    return sim
    
## output index
def computerSimilarity(query, listOfVectors, candidateIndice):
    indexList= []
    docIndices=[]
    

    
    output = []
    if not listOfVectors:
        print query + "did not match any documents."
        return indexList

    if listOfVectors:
        simiVector = [simDistance(query, value) for value in listOfVectors]
        
        #print simiVector
        indexList = sorted(range(len(simiVector)), key = lambda k: simiVector[k])
    



    for i in indexList:
        #print i
        docIndices.append(candidateIndice[i])

    docIndices.reverse()
    simiVector.sort()
    simiVector.reverse()
    output.append(docIndices)
    output.append(simiVector)

    return output
    
##out put value
"""
def computerSimilarity(query, listOfVectors):
    indexList= []
    if not listOfVectors:
        print query + "did not match any documents."
        return indexList
    
    sortedResult = listOfVectors
    if listOfVectors:
        for vector in listOfVectors:
            value = simDistance(query,vector)
            vector = value
        indexList = sorted(range(len(sortedResult)), key = lambda k: sortedResult[k])
        return indexList
"""
"""
    def computerSimilarity(query, listOfVectors):
    indexList= []
    if not listOfVectors:
    print query + "did not match any documents."
    return indexList
    if listOfVectors:
    for vector in listOfVectors:
    value = simDistance(query,vector)
    indexList.append(value)
    indexList.sort()
    return indexList
"""
"""
query = [1,2,3,0]
listOfVectors = [[1,0,0,0],[1,3,1,1],[0.5,0,0,0],[2,90,100,2],[1,1,0,0]]

output = computerSimilarity(query, listOfVectors)
print output
"""
