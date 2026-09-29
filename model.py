from imports import*
from data_preprocessing import*

def analyze_sentiment(headline,tokenizer,model):
    # Tokenize the input text
    inputs = tokenizer(headline, return_tensors="pt", truncation=True, padding=True, max_length=512)
    
    # Get model predictions
    with torch.no_grad():
        outputs = model(**inputs)
    
    # Get the predicted sentiment
    predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
    sentiment = torch.argmax(predictions, dim=1).item()
    
    # Convert sentiment to human-readable format
    sentiment_labels = ["negative", "neutral", "neutral", "neutral", "positive"]
    return sentiment_labels[sentiment]

def delete_files():
    files_to_delete = ['label_encoder.pkl', 'logreg_model.pkl', 'max_length.pkl', 'tokenizer.pkl','vectorizer.pkl']
    for file in files_to_delete:
        try:
            os.remove(file)
            print(f"Deleted {file}")
        except FileNotFoundError:
            print(f"{file} not found")
        except Exception as e:
            print(f"Error deleting {file}: {e}")

# Delete the files before training the model
delete_files()

def logistic_model():
    # Load and preprocess the dataset
    df = pd.read_csv('Train_Dataset.csv')
    df['sentiment'] = df['sentiment'].fillna("neutral")
    df['text'] = df['text'].apply(clean).apply(lemmatize_text)

    # Preprocess texts and encode labels
    vectorizer, train_transformed_texts = preprocess_texts_train(df['text'])
    label_encoder = LabelEncoder()
    labels = label_encoder.fit_transform(df['sentiment'])

    # Train the logistic regression model
    logreg = LogisticRegression(max_iter=1000)
    logreg.fit(train_transformed_texts, labels)

    # Save the model and preprocessing objects
    joblib.dump(logreg, 'logreg_model.pkl')
    with open('vectorizer.pkl', 'wb') as handle:
        pickle.dump(vectorizer, handle, protocol=pickle.HIGHEST_PROTOCOL)
    with open('label_encoder.pkl', 'wb') as handle:
        pickle.dump(label_encoder, handle, protocol=pickle.HIGHEST_PROTOCOL)