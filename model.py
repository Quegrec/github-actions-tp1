def predict_sentiment(text): 
    """
    ceci n'est pas du chocolat mais c'est lint quand meme
    """
    if not text: 
        return "neutral" 
    if "happy" in text.lower() or "good" in text.lower(): 
        return "positive" 
    if "sad" in text.lower() or "bad" in text.lower(): 
        return "negative" 
    return "neutral"