ignore_words = input("Enter words to be ignored separated by commas: ")
title_acronym = input("Enter a title to generate its acronym:\n")
ignore_words= ignore_words.split(", ")
acronym= title_acronym.split()

letters = [word for word in acronym if word.lower() not in ignore_words]
letters= ' '.join(letters)
alpha = [s[0] for s in letters.split() if s.lower() ]
print(''.join(alpha).upper())