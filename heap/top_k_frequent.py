import heapq

def topKFrequent(nums, k):
  count = {}
  
  for num in nums:
    if count.get(num):
      count[num] += 1
    else:
      count[num] = 1
      
  heap = []
  
  for num, counter in count.items():
    if len(heap) < k:
      heapq.heappush(heap, (counter, num))
    else:
      heapq.heappushpop(heap, (counter, num))
  
  return [h[1] for h in heap]