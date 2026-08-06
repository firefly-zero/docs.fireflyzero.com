import requests
from pathlib import Path

HEADERS = {'Accept': 'application/vnd.github.v3+json'}
URL = 'https://api.github.com/orgs/firefly-zero/repos'
ROOT = Path(__file__).parent

urls = []
for page in range(1, 4):
    if page > 1:
        print(f'  page {page}')
    response = requests.get(
        URL,
        params=dict(per_page=100, page=page),
        headers=HEADERS,
    )
    response.raise_for_status()
    org_projects = response.json()
    for project in org_projects:
        if not project['archived']:
            urls.append(project['html_url'])
    if len(org_projects) < 100:
        break

text = (ROOT / 'content' / 'internal' / 'projects.md').read_text()
for url in urls:
    if url not in text:
        print(url)
