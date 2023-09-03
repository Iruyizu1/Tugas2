pip install requests pandas

import requests
import pandas as pd

# Ganti dengan informasi repositori Anda
repo_owner = 'nama-pemilik-repo'
repo_name = 'nama-repo'
token = 'token-api-github'

# URL API untuk mengambil issue
url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/issues'

# Header dengan token API
headers = {
    'Authorization': f'token {token}'
}

# Mengambil data issue dari GitHub
response = requests.get(url, headers=headers)
data = response.json()

# Membuat DataFrame dengan data issue
df = pd.DataFrame(data)

# Menyimpan DataFrame ke dalam file CSV
df.to_csv('issues.csv', index=False)
