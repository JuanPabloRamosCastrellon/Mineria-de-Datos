import pandas as pd
import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt

file_path = 'C:/Users/Juan Pablo/Desktop/Mineria-de-Datos/Nashville Housing Data.xlsx'

spreadsheet = pd.ExcelFile(file_path)
spreadsheet.sheet_names
df = pd.read_excel(file_path, sheet_name='Sheet1')
# df.info(), df.head()

# Combine all text entries into one string
text_data = df['PropertyAddress'].dropna().str.cat(sep=' ')

# Function to remove punctuation, numbers, and lowercase all words
def preprocess_text(text):
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\d+', '', text)
    text = text.lower()
    return text

cleaned_text_data = preprocess_text(text_data)

# Create the WordCloud
wordcloud = WordCloud(width=800, height=400, background_color='white', max_words=200).generate(cleaned_text_data)

plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
