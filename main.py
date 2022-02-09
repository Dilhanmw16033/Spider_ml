from bs4 import BeautifulSoup
from langdetect import detect
from iso639 import languages
import pandas as pd 
import requests

paths = []
df = pd.read_excel(r"C:\Users\sachin.dilhan\Desktop\spider_ml\Url_dataset.xlsx")
df.columns = ['URL']
for i in df['URL']: 
  paths.append(i)
print(df)