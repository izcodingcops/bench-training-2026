import string

def word_frequency(text):
    text = text.lower()
    for p in string.punctuation:
        text = text.replace(p, "")

    words = text.split()

    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    return freq


paragraph = """
    Machine learning is a branch of artificial intelligence. 
    Machine learning allows systems to learn from data. 
    Learning from data means systems can improve over time. 
    Artificial intelligence and machine learning are closely related fields. 
    Data is at the heart of every machine learning system.
"""

freq = word_frequency(paragraph)
most_common = sorted(freq.items(), key=lambda item: item[1], reverse=True)

for word, count in most_common:
    if count > 1:
        print(f"  '{word}': {count}")