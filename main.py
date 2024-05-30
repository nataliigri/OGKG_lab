import os
import re

class FileReader:
    def read_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                return file.read()
        except IOError as e:
            raise IOError("Unable to read the file:", e)

class VowelWordExtractor:
    def is_vowel(self, c):
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        if not c.isalpha():
            raise ValueError("The input must be a letter.")
        return c in vowels

    def get_unique_vowel_words(self, file_content):
        # Clear file content and split into words
        words = re.findall(r'\b[a-zA-Z]+\b', file_content)

        # Filter unique vowel words
        unique_words = set()
        for word in words:
            if all(self.is_vowel(char) for char in word):
                unique_words.add(word)
        return list(unique_words)

if __name__ == "__main__":
    file_path = "/Users/nataliiagricisin/Documents/3 курс/II семестр/Lab2_MSTest/Lab2_MSTest/input.txt"
    file_reader = FileReader()
    vowel_word_extractor = VowelWordExtractor()

    try:
        if not os.path.exists(file_path):
            print("File does not exist:", file_path)
            exit()

        file_content = file_reader.read_file(file_path)
        print("File Content:")
        print(file_content)

        unique_vowel_words = vowel_word_extractor.get_unique_vowel_words(file_content)

        print("Filtered Words:")
        for word in unique_vowel_words:
            print(word)

    except IOError as e:
        print("An error occurred while reading the file:", e)
    except Exception as e:
        print("An error occurred:", e)
