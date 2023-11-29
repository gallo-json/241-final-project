markovMatrix = [[0.0, 0.5, 0.333333],
                [0.0, 0.0, 0.333333],
                [1.0, 0.5, 0.333333]]

vector = [1, 4, 7, 5, 2, 9, 11]
length = len(vector)
newVector = []
for x in range(length):
    newVector.append((vector[x], x + 1))
newVector = sorted(newVector)
print(newVector)



# dampeningFactor = 0.85
# randomPageProb = 1 - dampeningFactor
# numberStates = len(markovMatrix)
# markovMatrixPrime = []
# for row in markovMatrix:
#     newRow = []
#     for val in row:
#         firstHalf = randomPageProb * val
#         secondHalf = (dampeningFactor / numberStates)
#         newRow.append(firstHalf + secondHalf)
#     markovMatrixPrime.append(newRow)
# markovMatrix = markovMatrixPrime
# # print(markovMatrix)

# surfDistribution = []
# lengthMarkov = len(markovMatrix[0])
# startingProbs = 1 / lengthMarkov
# for val in range(lengthMarkov):
#     surfDistribution.append(startingProbs)
# newSurfers = []
# while surfDistribution != newSurfers:
#     newSurfers = []
#     for row in range(len(markovMatrix)):
#         sum = 0
#         for col in range(len(markovMatrix[0])):
#             newVal = markovMatrix[row][col] * surfDistribution[col]
#             sum += newVal
#         newSurfers.append(sum)
#     surfDistribution = newSurfers
# print(surfDistribution)

