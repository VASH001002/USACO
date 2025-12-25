T = int(input())
list_of_num = list(input() for _ in range(T))

def main(list_of_num):
    for int1 in list_of_num:
        score = 0
        string = '0123456789'
        power = len(int1) - 1
        in1 = int(int1)
        string_2 = '4' + '9' * power
        if in1 >= int(string_2):
            score = 5 * (int(string[:power+1]))
        elif in1 < int(string_2):
            score = 5 * (int(string[:max(power, 1)])) + max(0, in1 - int('4' * power + '5')+1)

        print(score)

main(list_of_num)

