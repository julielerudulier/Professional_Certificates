from cs50 import get_string
import re
import numpy as np

text = get_string("Text: ")


def letters(text):
    letter_count = 0
    edited_text = re.sub("[\W_]+", "", text)
    for i in edited_text:
        letter_count += 1
    return letter_count


def words(text):
    word_count = 1
    for i in text:
        if i == " ":
            word_count += 1
    return word_count


def sentences(text):
    sentence_count = 0
    for i in text:
        if i == "?" or i == "!" or i == ".":
            sentence_count += 1
    return sentence_count


total_letters = letters(text)
total_words = words(text)
total_sentences = sentences(text)

L = (total_letters * 100) / total_words
S = (total_sentences * 100) / total_words

index = 0.0588 * L - 0.296 * S - 15.8
i = int(np.around(index, decimals=0))

if i < 1:
    print("Before Grade 1")

elif i >= 1 and i < 16:
    print(f"Grade {i}")

elif i >= 16:
    print("Grade 16+")
