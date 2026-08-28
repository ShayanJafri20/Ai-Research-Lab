import os 
import pandas as pd 
import matplotlib.pyplot as plt 
from collections import Counter
import re


def analyze_dataset(filepath): 
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read() 
    text = clean_gutenberg_text(text)
    words = text.split()
    return {
        "filename" : os.path.basename(filepath), 
        "word_count": len(words), 
        "unique_words": len(set(words)) 
    }

def top_words(text, n=10): 
    words = re.findall(r"\b\w+\b", text.lower())
    counts = Counter(words) 
    return counts.most_common(n)

def clean_gutenberg_text(text): 
    start_marker = "*** START OF THE PROJECT GUTENBERG EBOOK"
    end_marker = "*** END OF THE PROJECT GUTENBERG EBOOK"

    start_index = text.find(start_marker) 
    start_index = text.find("\n", start_index) + 1 

    end_index = text.find(end_marker)

    return text[start_index:end_index]

if __name__ == "__main__":
    folder = "datasets" 
    results = [] 
    for filename in os.listdir(folder): 
        filepath = os.path.join(folder, filename)
        results.append(analyze_dataset(filepath))

    df = pd.DataFrame(results) 
    df.plot(x='filename', y='word_count', kind='bar')
    plt.show()
    print(df)

    with open(os.path.join(folder, "peter_rabbit.txt"), "r", encoding="utf-8") as f:
        sample_text = f.read()
    sample_text = clean_gutenberg_text(sample_text)
    print(top_words(sample_text))

    top = top_words(sample_text, n=10)
    words_df = pd.DataFrame(top, columns=["word", "count"])
    words_df.plot(x="word", y="count", kind="bar")
    plt.show()