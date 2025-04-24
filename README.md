# NLP-Natural Language Processing-Beispielprojekt

Dieses Projekt demonstriert die grundlegenden Aufgaben der natürlichen Sprachverarbeitung (Natural Language Processing, NLP) mit Python. Ziel ist es, einen einfachen Einstieg in verschiedene NLP-Techniken zu geben, darunter Sentimentanalyse, Named Entity Recognition, Part-of-Speech-Tagging, maschinelle Übersetzung und Fragebeantwortung.

## Inhalt

- Textklassifikation (einfach simuliert)
- Sentimentanalyse mit TextBlob
- Named Entity Recognition (NER) mit spaCy
- Part-of-Speech-Tagging (POS)
- Maschinelle Übersetzung mit deep-translator
- Simulierte Fragebeantwortung

## Voraussetzungen

Installiere die benötigten Python-Bibliotheken:

```bash
pip install spacy textblob deep-translator
python -m spacy download en_core_web_sm
python -m textblob.download_corpora
