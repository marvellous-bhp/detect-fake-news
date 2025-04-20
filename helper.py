import joblib
import re
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import string
vectorization = TfidfVectorizer()


def wordopt(text):
    text = re.findall(r'<a\s+href="(.*?)"', text)
    text = " ".join(map(str, text))
    text = text.lower()
    text = re.sub('\[.*?\]','', text)
    text = re.sub("\\W"," ",text )
    text = re.sub('http?://\S+|www\.\S+','',text)
    text = re.sub('<.*?>+','',text)
    text = re.sub('[%s]' % re.escape(string.punctuation),'',text)
    text = re.sub('\n','',text)
    text = re.sub('\w*\d\w*','',text)
    return text
def output_lable(n):
    if n==0:
        return "Fake NEWS"
    elif n==1:
        return "Real NEWS"
    
# def output_lable(n):
#     if n==0:
#         return False
#     elif n==1:
#         return True
    
pipeline_lr = joblib.load('pipeline_lr.joblib')
pipeline_dt = joblib.load('pipeline_dt.joblib')
pipeline_rf = joblib.load('pipeline_rf.joblib')
pipeline_gb = joblib.load('pipeline_gb.joblib')

def manual_testing(news):
    testing_news = {'text':[news]}
    new_def_test = pd.DataFrame(testing_news)
    vectorization.fit(new_def_test)
    new_def_test["text"] = new_def_test["text"].apply(wordopt)
    new_x_test = new_def_test["text"]

    pred_dt=pipeline_dt.predict(new_x_test)
    pred_lr = pipeline_lr.predict(new_x_test)
    predict_gb=pipeline_gb.predict(new_x_test)
    predict_rf=pipeline_rf.predict(new_x_test)

    result = round((int(pred_dt[0]) + int(pred_lr[0]) + int(predict_gb[0]) +1.5*int(predict_rf[0]))/4.5)
    print('...............',result)
    result=str(result)
    return result
