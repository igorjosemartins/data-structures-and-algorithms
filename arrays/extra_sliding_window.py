# 219. Contains Duplicate II

# Verificar se há números duplicados entre um limite 'k'

def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    l, r = 0, 0
    counter = {}
    counter[nums[0]] = 1

    while r < (len(nums) - 1):
        r += 1

        if counter.get(nums[r]):
            counter[nums[r]] += 1
        else:
            counter[nums[r]] = 1

        while counter[nums[r]] == 2:
            if abs(r - l) <= k:
                return True
            
            counter[nums[l]] -= 1
            l += 1
    
    return False

print(containsNearbyDuplicate([1, 3, 5, 1], 3)) # True
print(containsNearbyDuplicate([1, 3, 5, 1], 2)) # False