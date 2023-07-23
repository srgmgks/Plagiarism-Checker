# Plagiarism-Checker-Python

This is a simple Python script that allows you to check for plagiarism between multiple text files. It calculates the percentage of common words shared between the files, which can give you an idea of the similarity between them.

How it works

The script uses the following steps to perform the plagiarism check:

1. Reads the content of each input file and stores it in a list.
2. Removes punctuation and converts all text to lowercase to ensure case-insensitive comparison.
3. Calculates word frequencies for each file using the get_word_frequencies function.
4. Finds the common words between any two files using the find_common_words function.
5. Computes the plagiarism percentage based on the number of common words and the total unique words between two files.
6. Prints the plagiarism percentage for all file pairs that have some degree of plagiarism.

Requirements

Python 3.x

How to use

1. Clone this repository to your local machine or download the script directly.
2. Ensure you have Python 3.x installed on your computer.
3. Run the script in your terminal or command prompt.
4. Enter the number of files you want to check for plagiarism.
5. Enter the names of the files you want to analyze. Make sure they are in the same directory as the script or provide the correct file paths.

Example Usage

$ python p.py

Enter the number of files to check for plagiarism: 3

Enter the name of file 1: file1.txt

Enter the name of file 2: file2.txt

Enter the name of file 3: file3.txt

Files to check for plagiarism:
file1.txt
file2.txt
file3.txt

Plagiarism detected between file1.txt and file2.txt

Plagiarism Percentage: 45.36%

Plagiarism detected between file1.txt and file3.txt

Plagiarism Percentage: 23.17%

Plagiarism detected between file2.txt and file3.txt

Plagiarism Percentage: 38.56%



