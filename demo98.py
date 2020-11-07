import glob
import os

BASE_PATH = 'c:\windows'
#search_path = os.path.join(BASE_PATH, "*\*.dll")
#search_path = os.path.join(BASE_PATH, "*\\*.dll")
search_path = os.path.join(BASE_PATH, "*/*.dll")
print(search_path)
for d in glob.glob(search_path):
    print(d)