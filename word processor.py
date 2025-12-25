N, K = map(int, input().split())
words = input().split()

count = 0
lenword = 0
current_list = []

for word in words:
    if lenword + len(word) <= K:
        current_list.append(word)
        lenword += len(word)
    else:
        print(" ".join(current_list))  # print current group as words separated by spaces
        current_list = [word]   # start new group with current word
        lenword = len(word)

if current_list:
    print(" ".join(current_list))  # print any remaining words in the last group
