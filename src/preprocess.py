import os
import pandas as pd

# Notice: Only in Python Terminal  
# FIXME : ModuleNotFoundError : No module named 'settings_3'
# -> ToDO: Set PYTHONPATH environment variable  
import data_path_setting  

DATA_ROOT = os.path.join(data_path_setting.PROJ_ROOT, "data") # setting the data root
df = pd.read_csv(f"{DATA_ROOT}/linkedin_jobs.csv") # Load data

########## Pre-processing ##########

# Leave only the first city name in the 'company_location' column
df['company_location'] = df['company_location'].apply(lambda x: x.split(',')[0])   

# Splitting and removing 'ago' from 'job_listed' column
df['job_listed_time'] = [z.replace(' ago', '') for z in df['job_listed_time']]   

# Preprocessing the 'job_listed_time' column
# For example,
# n day(s) -> n
# n week(s) -> n * 7
# n month(s) -> n * 30
# n year(s) -> n * 365
# n hour(s) -> 1
def preprocess(s):
    if s.endswith('day'):
        return int(s[:-4])
    elif s.endswith('days'):
        return int(s[:-5])
    elif s.endswith('week'):
        return int(s[:-5]) * 7
    elif s.endswith('weeks'):
        return int(s[:-6]) * 7
    elif s.endswith('month'):
        return int(s[:-6]) * 30
    elif s.endswith('months'):
        return int(s[:-7]) * 30
    elif s.endswith('year'):
        return int(s[:-5]) * 365
    elif s.endswith('years'):
        return int(s[:-6]) * 365
    elif s.endswith('hour'):
        return 1    
    elif s.endswith('hours'):
        return 1    
    elif s.endswith('minutes'):
        return 1
    else:
        return None

df['job_listed_time'] = df['job_listed_time'].apply(preprocess)

# Save as csv file
df.to_csv('data/preprocessed_jobs.csv', index=False, encoding='utf-8')


