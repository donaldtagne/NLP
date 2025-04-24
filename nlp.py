import spacy
from textblob import TextBlob
from deep_translator import GoogleTranslator

# Lade englisches NLP-Modell
nlp = spacy.load("en_core_web_sm")

# Beispieltext
text = "Angela Merkel was the chancellor of Germany until 2021. Tesla will open a factory in Berlin in 2025. I love their innovation!"

# NLP-Analyse mit spaCy
doc = nlp(text)

# 1. Textklassifikation – nicht direkt mit spaCy, aber wir tun so:
print("Textklassifikation (manuell zugewiesen):")
if "Tesla" in text or "factory" in text:
    print("Kategorie: Wirtschaft / Technologie\n")

# 2. Sentimentanalyse mit TextBlob
print("Sentimentanalyse:")
blob = TextBlob(text)
print(f"Polarity: {blob.sentiment.polarity} (Positiv wenn > 0)")
print()

# 3. Fragebeantwortung – simuliert
print("Fragebeantwortung:")
print("Frage: Wer war Kanzler von Deutschland?")
print("Antwort: Angela Merkel\n")

# 4. Named Entity Recognition (NER)
print("Named Entities:")
for ent in doc.ents:
    print(f"{ent.text} -> {ent.label_}")
print()

# 5. Part-of-Speech-Tagging
print("Wortarten (POS):")
for token in doc:
    print(f"{token.text} -> {token.pos_}")
print()

# 6. Übersetzung mit TextBlob (EN -> DE)
print("Übersetzung:")
text = "I love natural language processing."
translated = GoogleTranslator(source='auto', target='de').translate(text)

print("Original:", text)
print("Übersetzt (DE):", translated)

