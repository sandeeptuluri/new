from os import link
import trafilatura
from keybert import KeyBERT
from textblob import TextBlob


from flask import Flask
app = Flask(__name__)

@app.route('/')
def show_name():
    url = "https://www.telesurenglish.net/news/Uruguays-Gender-Violence-Courts-Have-No-Funding-20210115-0014.html"
    html = trafilatura.fetch_url(url)
    data = trafilatura.extract(html)
    data_clean = data.replace("\n"," ").replace("\'", "")
    text = data_clean

    kb = KeyBERT('distilbert-base-nli-mean-tokens')
    keywords = kb.extract_keywords(text, stop_words='english')

    analysis = TextBlob(text)
    a = analysis.polarity
    def type():
        if (a>0):
            return("Positive")
        else:
            return("Negative")
    c = type()
    
    dc = {}
    dc['KEYWORDS']=keywords
    dc['SENTIMENT']=c

    return dc

if __name__ == '__main__':
    app.run(debug=True)
