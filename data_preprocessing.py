from imports import *

def clean(text):
    text = re.sub(r'[^a-zA-Z\s]', '', str(text))
    text = re.sub('https?://\S+', '', text)
    # Convert to lower
    text = text.lower()
    # Remove extra whitespaces
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# Function to lemmatize text
def lemmatize_text(text):
    w_tokenizer = nltk.tokenize.WhitespaceTokenizer()
    lemmatizer = nltk.stem.WordNetLemmatizer()
    st = " ".join(lemmatizer.lemmatize(w) for w in w_tokenizer.tokenize(text))
    return st

# Function to preprocess texts for training
def preprocess_texts_train(texts, vectorizer=None):
    if vectorizer is None:
        vectorizer = TfidfVectorizer()
        vectorizer.fit(texts)
    transformed_texts = vectorizer.transform(texts)
    return vectorizer, transformed_texts

# Function to preprocess new texts
def preprocess_new_texts(texts, vectorizer):
    transformed_texts = vectorizer.transform(texts)
    return transformed_texts