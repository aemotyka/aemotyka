import re
from datetime import datetime, timedelta

with open('README.md', 'r') as file:
    readme_content = file.read()

pattern = r'(\d+)'

matches = re.findall(pattern, readme_content)
if matches:
    days = int(matches[-1]) + 1
else:
    raise ValueError("No number of days found in README.md")

new_readme_content = re.sub(pattern, str(days), readme_content)

with open('README.md', 'w') as file:
    file.write(new_readme_content)

print(f"Number of days incremented to {days}")
