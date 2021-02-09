import networkx as nx
import pandas as pd
import json
import csv
import pickle
import math 
import os
from datetime import datetime
import pyhrv
import pyhrv.nonlinear as nl
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pandas import Grouper
import os

first=49
second=79
for el in range(first,second):
    un_labels=[]
    if len(str(el))<2:
        #os.system('cd /Users/olgabuchel/Sites/sg-social-distancing2/0'+str(el))
        arr = os.listdir('/Users/olgabuchel/Sites/sg-social-distancing2/0'+str(el))
        for item in arr:
            #print(item[:4])
            if str(item[:4]) not in un_labels:
                un_labels.append(str(item[:4]))
                #os.system('mkdir '+str(item[:4]))
    else:
        #os.system('cd /Users/olgabuchel/Sites/sg-social-distancing2/'+str(el))
        arr = os.listdir('/Users/olgabuchel/Sites/sg-social-distancing2/'+str(el))
        #print(arr)
        for item in arr:
            #print(item[:4])
            if str(item[:4]) not in un_labels:
                un_labels.append(str(item[:4]))
    for item in un_labels:            
        os.system('mkdir '+str(item[:2])+'/'+str(item))


for el in range(first,second):
    if len(str(el))<2:
        arr = os.listdir('/Users/olgabuchel/Sites/sg-social-distancing2/0'+str(el))
        for item in arr:
            #print(item)
            os.system('mv /Users/olgabuchel/Sites/sg-social-distancing2/'+ str(item[:2])+'/'+item+' /Users/olgabuchel/Sites/sg-social-distancing2/'+ str(item[:2])+'/'+str(item[:4])+'/'+item)                                                                                            
    else:
        arr = os.listdir('/Users/olgabuchel/Sites/sg-social-distancing2/'+str(el))
        for item in arr:
            #print(item)
            os.system('mv /Users/olgabuchel/Sites/sg-social-distancing2/'+ str(item[:2])+'/'+item+' /Users/olgabuchel/Sites/sg-social-distancing2/'+ str(item[:2])+'/'+str(item[:4])+'/'+item)
