import string
from collections import Counter

def get_word_frequencies(text):
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    word_freq = Counter(text.split())
    return word_freq

def find_common_words(file1, file2):
    freq1 = get_word_frequencies(file1)
    freq2 = get_word_frequencies(file2)

    common_words = set(freq1.keys()) & set(freq2.keys())
    return common_words

def calculate_plagiarism_percentage(file1, file2):
    common_words = find_common_words(file1, file2)
    total_unique_words = set(get_word_frequencies(file1).keys()) | set(get_word_frequencies(file2).keys())

    if not total_unique_words:
        return 0.0

    plagiarism_percentage = len(common_words) / len(total_unique_words) * 100
    return plagiarism_percentage

num_files = int(input("\nEnter the number of files to check for plagiarism: "))

file_contents = []
file_names = []

for i in range(num_files):
    file_name = input(f"\nEnter the name of file {i+1}: ")
    with open(file_name, 'r') as file:
        content = file.read()
        file_contents.append(content)
        file_names.append(file_name)

print("\nFiles to check for plagiarism: ")
for file_name in file_names:
    print(file_name)

# Perform plagiarism checking and print the plagiarism percentage
for i in range(num_files):
    for j in range(i+1, num_files):
        plagiarism_percentage = calculate_plagiarism_percentage(file_contents[i], file_contents[j])
        if plagiarism_percentage > 0.0:
            print(f"\nPlagiarism detected between {file_names[i]} and {file_names[j]}")
            print(f"Plagiarism Percentage: {plagiarism_percentage:.2f}%")
            print()
