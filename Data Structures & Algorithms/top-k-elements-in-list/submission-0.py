class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        ordered= sorted(count, key= count.get, reverse= True)

        return ordered[:k]