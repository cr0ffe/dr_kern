import os
import yaml
import re

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def create_corpus():
    corpus = []
    playbook_dir = 'SentryWire_xSOAR/playbooks'
    for filename in os.listdir(playbook_dir):
        if filename.endswith('.yml'):
            with open(os.path.join(playbook_dir, filename), 'r') as file:
                playbook = yaml.load(file, Loader=yaml.FullLoader)
                for task in playbook.get('tasks', []):
                    for key, value in task.items():
                        if isinstance(value, str):
                            text = preprocess_text(value)
                            corpus.append(text)
    return corpus
