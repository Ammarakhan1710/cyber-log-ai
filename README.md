#Cyber Log AI

Cyber Log AI is an intelligent machine learning tool that classifies system logs into Normal or Suspicious, helping you quickly detect potential threats.

How It Works

1. The dataset `log_dataset.csv` contains system logs with their respective labels.  
2. Logs are transformed into numerical features using CountVectorizer.  
3. A Naive Bayes model is trained to predict whether a log is normal or suspicious.  
4. Users can paste any system log, and the AI predicts its status instantly.

Features

Quick detection of suspicious activities  
Simple and easy-to-use Python interface  
Learn basic ML text classification with real logs  



bash
python test.py
