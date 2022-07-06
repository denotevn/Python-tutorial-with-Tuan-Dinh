from pathlib import Path
from webbrowser import get

# Absulute path
# Relative path
path = Path("/home/tuandinh/Desktop/python/tutorial/working_with_Directories/dictionary")
print(path.exists())

import os
print(os.getcwd()) # /home/tuandinh/Desktop/python
print(os.listdir())


for file in path.glob('*.py'):
    print(file)

path = Path("/home/tuandinh/Desktop/python/tutorial")
for file in path.glob('*.py'):
    print(file)