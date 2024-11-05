def sentiment_analysis(note_id):
    from textblob import TextBlob
    content = read_note(note_id)
    sentiment = TextBlob(content).sentiment
    return sentiment.polarity

def extract_key_phrases(note_id):
    from yake import KeywordExtractor
    content = read_note(note_id)
    kw_extractor = KeywordExtractor()
    keywords = kw_extractor.extract_keywords(content)
    return [kw[0] for kw in keywords]
