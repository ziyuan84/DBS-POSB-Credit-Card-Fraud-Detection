# Using daily transaction amounts from 'posbec.csv' (replace with the relevant csv file)
# to detect suspicious transactions. Here the three columns of 'posbec.csv' are (in order): 'date',
# 'transaction' and 'amount'. 

import pandas as pd
import spacy_cleaner
from spacy_cleaner.processing import removers, replacers, mutators
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
import re

df = pd.read_csv("posbec.csv")
df.drop_duplicates
df = df.drop(df[df.transaction == 'transaction'].index)

df_daily_amount = df.loc[:,['date','amount']]
df_daily_amount['amount'] = df_daily_amount['amount'].map(lambda x: float(re.search(r'\d+\.\d+', x).group()))
df_daily_amount = df_daily_amount.groupby(by='date').sum()

# Function to return top n daily transaction amounts.
def top_daily_amount(n):
    return df_daily_amount.sort_values(by='amount', ascending=False).head(n)
