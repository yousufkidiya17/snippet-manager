"""Snippet manager"""
import json
import sys
from pathlib import Path

DATA = Path("snippets.json")

def load(): return json.loads(DATA.read_text()) if DATA.exists() else {}
def save(d): DATA.write_text(json.dumps(d, indent=2))

def add(name, code):
    d = load(); d[name] = code; save(d); print(f"saved {name}")

def search(term):
    for name, code in load().items():
        if term.lower() in name.lower() or term.lower() in code.lower():
            print(f"--- {name} ---\n{code}")

def delete(name):
    d = load(); d.pop(name, None); save(d); print(f"deleted {name}")

cmd, name = sys.argv[1], sys.argv[2]
if cmd == "add":
    add(name, sys.stdin.read().strip())
elif cmd == "search":
    search(name)
elif cmd == "delete":
    delete(name)
