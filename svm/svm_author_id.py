#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess

features_train, features_test, labels_train, labels_test = preprocess()

from sklearn.metrics import accuracy_score

from sklearn.svm import SVC


clf = SVC(kernel="rbf" , C = 10000)

#features_train = features_train[:len(features_train)/100]
#labels_train = labels_train[:len(labels_train)/100]

t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

t0 = time()
pred = clf.predict(features_test)
print "training time:", round(time()-t0, 3), "s"
#print "10",pred[10]
#print "26",pred[26]
#print "50",pred[50]

counter = 0

for num in pred:
   if num == 1:
       counter = counter + 1

print "count ", counter
accuracy = accuracy_score(pred, labels_test)
print accuracy

#########################################################


