import json
import requests

with open('data/user.json', encoding='utf-8') as f:
    user = json.loads(f.read())

for u in user:
    r = requests.post('http://127.0.0.1:5000/user/new', json = u)
    print(f"Created u {u['name']} {u['email']} with ID {r.text}")

with open('data/video.json', encoding='utf-8') as f:
    video = json.loads(f.read())

for vid in video:
    r = requests.post('http://127.0.0.1:5000/video/new', json = vid)
    print(f"Created vid {vid['title']} {vid['likes']} with ID {r.text}")
