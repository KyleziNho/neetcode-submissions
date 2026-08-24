class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        for num in nums:
            if num in frequencies:
                frequencies[num] += 1
            else:
                frequencies[num] = 1
        # Organise by bucket
        buckets = [[] for _ in range(len(nums)+1)]
        for num, freq in frequencies.items():
            buckets[freq].append(num)
        results = []
        for freq in range(len(buckets)-1, 0, -1):
            for num in buckets[freq]:
                results.append(num)
                if len(results) == k:
                    return results
        return results
            
        
        