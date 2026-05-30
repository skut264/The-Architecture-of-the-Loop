#!/usr/bin/env python3
import os, re, json, base64, subprocess, sys

# Read .env and extract GitHub token (not exposed in terminal output)
env_path = os.path.expanduser('/root/.hermes/.env')
token = None
with open(env_path) as f:
    for line in f:
        m = re.search(r'(ghp_[A-Za-z0-9_]{36,})|([A-Za-z0-9]{35,40})', line)
        if m:
            token = m.group(0)
            break

if not token:
    print('ERROR: GitHub token not found in .env')
    sys.exit(1)

print(f'Token found (len={len(token)})')

# Create the repo via GitHub API
import urllib.request

headers = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github.v3+json',
    'Content-Type': 'application/json; charset=utf-8',
}

body = json.dumps({
    'name': 'The-Architecture-of-the-Loop',
    'description': 'A living mystical book — The Architecture of the Loop. Where hidden truths find their voice.',
    'private': False,
    'has_pages': True,
}).encode('utf-8')

req = urllib.request.Request(
    'https://api.github.com/user/repos',
    headers=headers, data=body, method='POST',
)

try:
    resp = urllib.request.urlopen(req)
    data = json.loads(resp.read())
    print(f"REPO_URL={data['html_url']}")
    print(f"CLONE_URL={data['clone_url']}")
    print(f"DEFAULT_BRANCH={data['default_branch']}")
except urllib.error.HTTPError as e:
    err = json.loads(e.read())
    if 'already exists' in str(err) or err.get('status') == '422':
        print('REPO_ALREADY_EXISTS')
    else:
        print(f'ERROR: {err}')
        sys.exit(1)
