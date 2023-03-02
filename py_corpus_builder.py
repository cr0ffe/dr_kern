import os
import re

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def create_corpus(output_file='/Users/zulDrak/Documents/GitHub/dr_kern/corpus_for_drkern.txt'):
    corpus = []
    playbook_dir = '/Users/zulDrak/Documents/GitHub/SentryWire_xSOAR'
    for filename in os.listdir(playbook_dir):
        if filename.endswith('.py'):
            with open(os.path.join(playbook_dir, filename), 'r') as file:
                for line in file:
                    text = preprocess_text(line)
                    corpus.append(text)
    with open(output_file, 'w') as file:
        file.write('\n'.join(corpus))
    return corpus