# -*- coding: utf-8 -*-
"""
Created on Thu May 14 17:09:31 2020

@author: LENOVO
"""

import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'experience':2, 'test_score':9, 'interview_score':6})

print(r.json())