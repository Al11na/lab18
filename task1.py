#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def load_text(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            text = file.readlines()
        return text
    except FileNotFoundError:
        print("Файл не найден.")
        return []

def vowel(text):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    words_starting_with_vowel = []
    for line in text:
        words = line.strip().split()
        for word in words:
            if word.lower()[0] in vowels:
                words_starting_with_vowel.append(word)
    return words_starting_with_vowel

def main():
    file_name = 'taskk1.txt'
    text = load_text(file_name)
    if text:
        words_starting_with_vowel = vowel(text)
        print("Слова, начинающиеся с гласных букв:")
        for word in words_starting_with_vowel:
            print(word)

if __name__ == "__main__":
    main()
