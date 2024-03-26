from langchain_community.document_loaders import JSONLoader
import json
from pathlib import Path
from pprint import pprint

file_path='./index.json'
data = json.loads(Path(file_path).read_text())
pprint(data)