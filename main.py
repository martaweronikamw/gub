import pandas as pd
import numpy as np
import os
import random
import matplotlib.pyplot as plt
from scipy import stats

isMale = random.randint(0,1)

def genAge(isMale): 
	if isMale==0:
		stats.norm.rvs(50, 15) 
	else:
		stats.norm.rvs(55,18)

for num in range(100):
    user_id = num
    sex = isMale
    age = genAge(sex)
    condition = ""
    


