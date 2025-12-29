# This program checks the similarity between two text files using Levenshtein distance (https://en.wikipedia.org/wiki/Levenshtein_distance).
# Author: Irfan Zainudin (m.irfan.zain@gmail.com)
# Date: 30th December 2025
# Note: Assisted by autocomplete tool in VSCode.

import sys

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
    
def levenshtein_distance(s1, s2):
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)

    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]

def compute_levenshtein_similarity(text1, text2):
    distance = levenshtein_distance(text1, text2)
    print(distance)
    max_len = max(len(text1), len(text2))
    if max_len == 0:
        return 1.0
    similarity = 1 - distance / max_len
    return similarity

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python levenshtein_similarity_check.py <file1> <file2>")
        sys.exit(1)

    file1_path = sys.argv[1]
    file2_path = sys.argv[2]

    text1 = read_file(file1_path)
    text2 = read_file(file2_path)

    similarity = compute_levenshtein_similarity(text1, text2)
    print(f"Levenshtein Similarity: {similarity:.4f}")