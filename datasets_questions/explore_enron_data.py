#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

counter = 0
for person in enron_data:
    if (enron_data[person]["total_stock_value"]=='NaN'):
        counter = counter + 1

print counter

maxi = 0
for person in enron_data:
    if (enron_data[person]["salary"] != 'NaN'  and enron_data[person]["salary"] != 26704229 and enron_data[person]["salary"] > maxi ):
        maxi = enron_data[person]["salary"]

print maxi

print    enron_data
