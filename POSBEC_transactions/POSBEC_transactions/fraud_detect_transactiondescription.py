# Using descriptions of transaction data from 'posbec.csv' (replace with the relevant csv file)
# to detect suspicious transactions. Here the three columns of 'posbec.csv' are (in order): 'date',
# 'transaction' and 'amount'. 

import pandas as pd
import spacy_cleaner
from spacy_cleaner.processing import removers, replacers, mutators
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

df = pd.read_csv("posbec.csv")
df.drop_duplicates
df = df.drop(df[df.transaction == 'transaction'].index)

model = spacy.load("en_core_web_sm")
pipeline = spacy_cleaner.Pipeline(
    model,
    removers.remove_stopword_token,
    removers.remove_punctuation_token,
    removers.remove_number_token,
    mutators.mutate_lemma_token,
)
clean_transaction = pipeline.clean(df['transaction'])
vect = CountVectorizer().fit(clean_transaction)
doc_word_count_vect = vect.transform(clean_transaction)
tfidf_transformer = TfidfTransformer(smooth_idf = True, use_idf = True)
tfidf_transformer.fit(doc_word_count_vect)

df_idf = pd.DataFrame(tfidf_transformer.idf_, index = vect.get_feature_names_out(), columns=['idf_weight'])
outlier_score = []
for s in clean_transaction:
    total_score = 0
    doc = CountVectorizer().build_tokenizer()(s.lower())
    for token in doc:
        total_score += df_idf.loc[token, 'idf_weight']
    outlier_score.append(total_score/len(doc))
        
df['outlier_score'] = outlier_score

# Function to return transactions of top n outlier scores. 
def top_suspicious_transactions(n):
    return df.sort_values(by='outlier_score', ascending=False).head(n)
