from imports import *
from data_preprocessing import *
from web_scrapper import *
from model import*

# Download necessary NLTK data
nltk.download('wordnet')
nltk.download('omw-1.4')

st.set_page_config(page_title="News Sentiment Analysis")
st.title("News Sentiment Analysis")

use_logistic = False

model_used = st.radio("Select model for analysis",["Bert(Preferred)","Logistic"])
if model_used=="Logistic":
    use_logistic=True
else:
    use_logistic = False

if use_logistic:
    logistic_model()
    #Load the trained model and preprocessing objects
    logreg = joblib.load('logreg_model.pkl')
    with open('vectorizer.pkl', 'rb') as handle:
        vectorizer = pickle.load(handle)
    with open('label_encoder.pkl', 'rb') as handle:
        label_encoder = pickle.load(handle)
else:
    model_name = "nlptown/bert-base-multilingual-uncased-sentiment"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)

domain = st.radio("Select Domain of news for analysis",["Sports","Tech","Politics","Entertainment","Business"],index=None)
if domain!=None:
    if domain=="Sports":
        titles, links = scrape_sports(url="https://www.indiatoday.in/search/sports", driver_path='chromedriver.exe')
    elif domain=="Tech":
        titles, links = scrape_sports(url="https://indianexpress.com/section/technology/", driver_path='chromedriver.exe')
    elif domain=="Politics":
        titles, links = scrape_sports(url="https://indianexpress.com/section/political-pulse/", driver_path='chromedriver.exe')
    elif domain=="Entertainment":
        titles, links = scrape_sports(url="https://indianexpress.com/section/entertainment/", driver_path='chromedriver.exe')
    elif domain=="Business":
        titles, links = scrape_sports(url="https://indianexpress.com/section/business/", driver_path='chromedriver.exe')

    if use_logistic:
        # Clean and preprocess titles
        cleaned_titles = [clean(title) for title in titles]
        lemmatized_titles = [lemmatize_text(title) for title in cleaned_titles]
        transformed_titles = vectorizer.transform(lemmatized_titles)
        # Make predictions
        predictions = logreg.predict(transformed_titles)
        predicted_labels = label_encoder.inverse_transform(predictions)
        for title, link,sentiment in zip(titles, links,predicted_labels):
            st.write(f"Title: {title}")
            st.write(f"Link: {link}")
            st.write(f"Predicted Sentiment: {sentiment}")
            st.write("-----")
    else:
    # Display results
        for title, link in zip(titles, links):
            sentiment = analyze_sentiment(title,tokenizer,model)
            st.write(f"Title: {title}")
            st.write(f"Link: {link}")
            st.write(f"Predicted Sentiment: {sentiment}")
            st.write("-----")
