# This program checks the similarity between two text files using cosine similarity.
# Author: Irfan Zainudin (m.irfan.zain@gmail.com)
# Date: 30th December 2025
# Note: Assisted by autocomplete tool in VSCode.

import sys
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
    
def compute_cosine_similarity(text1, text2):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([text1, text2])
    similarity_matrix = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    return similarity_matrix[0][0]

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python similarity_check.py <file1> <file2>")
        sys.exit(1)

    file1_path = sys.argv[1]
    file2_path = sys.argv[2]

    text1 = read_file(file1_path)
    text2 = read_file(file2_path)

    similarity = compute_cosine_similarity(text1, text2)
    print(f"Cosine Similarity: {similarity:.4f}")