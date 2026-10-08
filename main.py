word = open('romeo.txt')
words_list = []

for line in word:
    for word in line.split():
        if word not in words_list:
            words_list.append(word)

words_list.sort()
print(words_list)