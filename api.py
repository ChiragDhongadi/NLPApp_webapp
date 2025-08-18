import nlpcloud

def ner(text):
    client = nlpcloud.Client("finetuned-llama-3-70b", "086bf5b3bfc32b8f5e39757040094483c6bdbe20", gpu=True)
    ner = client.entities(text,searched_entity="programming languages")
    return ner


def sentiment_analysis(text):
    client = nlpcloud.Client("finetuned-llama-3-70b", "086bf5b3bfc32b8f5e39757040094483c6bdbe20", gpu=True)
    response = client.sentiment(text, target="NLP Cloud")
    return response

def language_detection(text):
    client = nlpcloud.Client("python-langdetect", "086bf5b3bfc32b8f5e39757040094483c6bdbe20", gpu=False)
    response = client.langdetection(text)
    return response
