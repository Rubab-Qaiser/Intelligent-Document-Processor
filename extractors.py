import re
import spacy

# Load spacy model
nlp = spacy.load('en_core_web_md')

def extract_dates(text):
    """Extract dates from text using regex patterns."""
    patterns = [
        r'\d{1,2}/\d{1,2}/\d{4}',                      # MM/DD/YYYY or DD/MM/YYYY
        r'\d{1,2}-\d{1,2}-\d{4}',                      # DD-MM-YYYY
        r'\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* \d{1,2},? \d{4}',
        r'\d{4}-\d{2}-\d{2}'                           # YYYY-MM-DD
    ]

    dates = []

    for pattern in patterns:
        matches = re.findall(pattern, text)
        dates.extend(matches)

    return dates


def extract_amounts(text):
    """Extract currency amounts from text and convert to float."""
    pattern = r'\$?\d+(?:,\d{3})*(?:\.\d{2})?'
    
    amounts = re.findall(pattern, text)
    
    cleaned = []
    for amount in amounts:
        clean = amount.replace('$', '').replace(',', '')
        cleaned.append(float(clean))
    
    return cleaned


def extract_entities(text):
    """Extract named entities from text using spacy NER."""
    doc = nlp(text)
    entities = {
        'persons': [],
        'organizations': [],
        'locations': [],
        'dates': [],
        'money': []
    }
    for ent in doc.ents:
        if ent.label_ == 'PERSON':
            entities['persons'].append(ent.text)
        elif ent.label_ == 'ORG':
            entities['organizations'].append(ent.text)
        elif ent.label_ in ['GPE', 'LOC']:
            entities['locations'].append(ent.text)
        elif ent.label_ == 'DATE':
            entities['dates'].append(ent.text)
        elif ent.label_ == 'MONEY':
            entities['money'].append(ent.text)
        
    return entities
