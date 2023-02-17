# DBS-POSB-Credit-Card-Fraud-Detection
Scripts to detect suspicious transactions on DBS/POSB credit cards
1. Extract transaction data from the transaction page using Scrapy and XPath.  
2. Detection of suspicious transactions based on descriptions of transactions:
- Build a vocabulary by applying CountVectorizer to the collection of transaction descriptions
- Calculate the Inverse Document Frequency (IDF) of each token
- Calculate the average IDF of each tokenized transaction description
- Transactions with a higher average IDF are more "suspicious"
3. Detection of suspicious transactions based on daily transaction amount
- Group the transactions by date 
- Sum the transaction amounts for each group
- Transactions on days where there are higher transaction amounts are more "suspicious"
