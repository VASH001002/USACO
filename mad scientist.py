n = int(input())
target = input()
given = input()

def main(n, target, given):
    answer = 0
    similar = False
    for i in range(n):
        if target[i] != given[i]:
            if not similar:
                answer += 1
                similar = True
        else:
            similar = False
    return answer

print(main(n, target, given))
        
            

    