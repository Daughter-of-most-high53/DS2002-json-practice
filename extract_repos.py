import json
import pandas as pd

# Read JSON file
with open('data/schacon.repos.json', 'r') as file:
    data = json.load(file)

# Extract required fields
repos = [
    (repo["name"], repo["html_url"], repo["updated_at"], repo["visibility"])
    for repo in data
]

# Convert to Pandas DataFrame
df = pd.DataFrame(repos, columns=["name", "html_url", "updated_at", "visibility"])

# Save first 5 rows to chacon.csv
df.head(5).to_csv("chacon.csv", index=False, header=False)

print("chacon.csv has been created with the first 5 repositories.")

