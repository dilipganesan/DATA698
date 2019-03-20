# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 07:42:32 2019

@author: Teacher
"""

import pandas as pd 

Diabetes = pd.read_csv("C:/Users/Teacher/Documents/R/diabetic_data.csv") 
print(Diabetes.head())
print(Diabetes.tail())
print(Diabetes.info())

FomatedDiabetes = pd.read_csv("C:/Users/Teacher/Documents/R/FinalDataSet.csv") 
print(FomatedDiabetes.head())
print(Diabetes.tail())
print(FomatedDiabetes.info())


print(len(Diabetes['encounter_id'].unique().tolist()))

result = pd.merge(Diabetes,
                 FomatedDiabetes[['encounter_id', 'DRG', 'Payment']],
                 on='encounter_id')

print(result.head())
print(Diabetes.head())
print(FomatedDiabetes.head())


print(result.tail())
print(Diabetes.tail())
print(Diabetes.tail())

result["DRG"] = result["DRG"].fillna("0").astype(int)
result["diag_1"] = result["diag_2"].replace("?","")
result["diag_2"] = result["diag_2"].replace("?","")
result["diag_3"] = result["diag_2"].replace("?","")
    
print(result.head())   

result.to_csv("OldDataSetWithDRG", index=False)

