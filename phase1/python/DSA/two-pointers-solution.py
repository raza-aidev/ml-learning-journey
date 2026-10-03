# TWO SUM list = [2, 1, 5, 3]
# from itertools import sort

def get_sum(items, target):
    left , right = 0, len(items)-1

    items.sort()
    # print(items)

    while left < right:
        total = items[left] + items[right]

        if total == target:
            return items[left], items[right] 
        elif total < target:
            left += 1
        else:
            right -= 1

# value = get_sum([2, 1, 5, 3], 4)
value = get_sum([12, 2, 33, 1], 34)

print(f"{value}")