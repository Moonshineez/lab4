import re
def count_words(text):
    stop_words = {'и', 'в', 'на', 'под', 'за', 'с', 'the', 'a', 'an', 'and', 'in', 'on'}
    text = text.lower()
    words = re.findall(r'\b\w+\b', text)
    word_counts = {}
    for word in words:
        if word not in stop_words:
            word_counts[word] = word_counts.get(word, 0) + 1          
    for word, count in word_counts.items():
        print(f"{word} -> {count}")
input_text = "Cat, dog, and cat! Bird, dog, on the cat."
print("Исходный текст:", input_text)
print("\nРезультат подсчета:")
count_words(input_text)
