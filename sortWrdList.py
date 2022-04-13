# words = open('wordListDE.txt', 'r').read().split()
# words2 = []
# for i in words:
#     if i not in words2:
#         words2.append(i)

# sortedWords = open('newList.txt', 'w')
# for i in words2:
#     if len(i) == 5:
#         sortedWords.write(i + '\n')
# sortedWords.close()

words = open('wordListDE.txt', 'r').read().split()
words2 = open('filterdList.txt', 'a')
words3 = open('wordListDE.txt', 'w')

for i in words:
    print(i)
    uIn = input()
    if(uIn == ''):
        words2.write(i + '\n')
    elif uIn == 's':
        for w in words:
            words3.write(w + '\n')
        exit()
    words.remove(i)
words2.close()
