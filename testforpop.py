import random
list1 = [random.randint(1, 1000000) for x in range(10)]

list1.sort()

print(list1)

secret_num = list1[random.randint(0, 9)]

print("Secret number is:", secret_num)

#binary search

counter = 0

low = 0
high = 9
while low < high:
    median = (low + high) // 2
    if list1[median] == secret_num:
        print("the secret is: what what poop", list1[median])
        counter = 1
        break
    elif list1[median] < secret_num:
        low = median + 1
    else:
        high = median - 1

if counter == 0:
    print('the secret number is:', list1[low])