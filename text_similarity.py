"""
# Вычисление меры сходства текстов при помощи косинусного расстояния
Дан набор предложений, скопированных с Википедии. Каждое из них имеет "кошачью тему" в одном из трех смыслов:

- кошки (животные);
- UNIX-утилита cat для вывода содержимого файлов;
- версии операционной системы OS X, названные в честь семейства кошачьих.

Задача — найти предложения, которые ближе всего по смыслу к расположенному в самой первой строке. 
В качестве меры близости по смыслу использовано косинусное расстояние.
"""

import pandas as pd
import numpy as np
import re
from scipy.spatial.distance import cosine


def load_data(filepath):
    with open('sentences.txt', 'r') as f:
        text = f.readlines()
    return text


def get_text_lower(text):
    return [sentence.lower() for sentence in text]


def tokenize_text(text):
    words = []
    for sentence in text:
	words_freqs = {}
	for word in re.split('[^a-z]', sentence): # разделение по всему, чему только можно, кроме букв
	    if word: # это условие позволяет исключить всякую ненужную пунктуацию
	        if word in words_freqs.keys():
		    words_freqs[word] += 1
		else:
		    words_freqs[word] = 1
	    words.append(words_freqs)
    return words


def create_words_freqs_matrix(words):
    df = pd.DataFrame()
    df = df.from_dict(words)
    df.fillna(0, inplace=True) # пустые ячейки заполнить нулями, получится матрица
    return df


def define_cos_distances(df):
    cos_distances = np.empty(0)
    for row in df.values:
        # Измеряем расстояние между первым предложением и всеми остальными предложениями (row = строка = предложение):
	cos_distance = cosine(df.values[0], row)
	cos_distances = np.append(cos_distances, cos_distance)
    sorted_cos_distances = pd.DataFrame(cos_distances, columns=['cos distances'])
    sorted_cos_distances.sort_values(axis=0, by='cos distances', inplace=True)
    return sorted_cos_distances


def main():
    filepath = '/Users/User/Desktop/similarity/sentences.txt' # укажите путь до вашего файла с текстом
    data = load_data(filepath)
    data_lower = get_text_lower(data)
    data_tokenized = tokenize_text(data_lower)
    words_freqs_matrix = create_words_freqs_matrix(data_tokenized)
    cos_distances = define_cos_distances(words_freqs_matrix)
    print(cos_distances)


if __name__ == '__main__':
    main()
