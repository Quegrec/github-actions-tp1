def predict_sentiment(text): 
    """
    Predicts the sentiment of a given text. drgdrdhdththtfhth

    Args:
        text (str): The input text to analyze. Can be an empty string.

    Returns:
        str: The predicted sentiment, which can be one of the following:
            - "positive": If the text contains words like "happy" or "good".
            - "negative": If the text contains words like "sad" or "bad".
            - "neutral": If the text is empty or does not contain any of the above keywords.

    Note:
        The sentiment analysis is case-insensitive.
    """
    if not text: 
        return "neutral" 
    if "happy" in text.lower() or "good" in text.lower(): 
        return "positive" 
    if "sad" in text.lower() or "bad" in text.lower(): 
        return "negative" 
    return "neutral"