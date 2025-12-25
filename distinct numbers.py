n = int(input())
distinct_numbers = set()
nums = list(map(int, input().split()))

for num in nums:
    distinct_numbers.add(num)

print(len(distinct_numbers))
