from textblob import TextBlob

def get_sentiment(text):
    # Create a TextBlob object
    blob = TextBlob(text)
    
    # Get the polarity score
    polarity = blob.sentiment.polarity
    
    # Classify sentiment
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Get user input
text = input("Enter a text string: ")

# Analyze sentiment
sentiment = get_sentiment(text)
print(f"The sentiment of the text is: {sentiment}")
