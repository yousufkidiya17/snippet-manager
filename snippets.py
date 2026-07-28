"""Snippet manager"""
import json
from pathlib import Path

DATA = Path("snippets.json")

def load(): return json.loads(DATA.read_text()) if DATA.exists() else {}
def save(d): DATA.write_text(json.dumps(d, indent=2))
