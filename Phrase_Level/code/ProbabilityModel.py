from Replacer import *
from senti_classifier import senti_classifier


def probTraining(priorScore):
    #Returns a Dictonary containing the probability of word being positive, negative, neutral

    wordProb = {}
    for i in priorScore.keys():
        if i:
            wordProb[i] = [0.0, 0.0, 0.0]
            posScore, negScore = senti_classifier.polarity_scores(list(i))
            if priorScore[i] > 0.0:
                wordProb[i][positive] = priorScore[i] / 5.0
                wordProb[i][negative] = negScore
            elif priorScore[i] < 0.0:
                wordProb[i][negative] = -(priorScore[i] / 5.0)
                wordProb[i][positive] = posScore
            else:
                wordProb[i][positive] = posScore
                wordProb[i][negative] = negScore

    return wordProb
