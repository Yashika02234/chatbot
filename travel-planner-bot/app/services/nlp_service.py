import spacy

nlp = spacy.load("en_core_web_sm")

def extract_destination(text):
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "GPE":  # Geopolitical Entity (e.g., cities, countries)
            return ent.text
    return None