import pandas as pd
import numpy as np
import os
import random
import matplotlib.pyplot as plt
from scipy import stats
import math

first_df = pd.DataFrame(columns=["id", "sex", "age", "conditon", "progress", "organization_id"])

progress = ["worse", "better", "improving", "the same"]
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
    age = math.floor(genAge(sex))
    condition = ""
    organization = ""
    current_progress = random.choice(progress)
    
    first_df.loc[num] = [num, sex, age, condition, current_progress, organization]
    

print(first_df)
