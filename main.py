import pandas as pd
import numpy as np
import os
import random
import matplotlib.pyplot as plt
from scipy import stats

first_df = pd.DataFrame(columns=["id", "sex", "age", "conditon", "organization_id"])

sex_probability = .49

def genAge(isMale): 
    age = 0
    if isMale==0:
        age = stats.norm.rvs(50, 15) 
    else:
        age = stats.norm.rvs(55,18)
    return age
  

for num in range(100):
    sex = np.random.binomial(1,sex_probability)
    age = genAge(sex)
    condition = ""
    organization = ""
    
    first_df.loc[num] = [num, sex, age, condition, organization]
    

print(first_df)
