import heapq
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = list(zip(nums1, nums2))
        pairs.sort(key=lambda x: x[1], reverse=True)
        
        heap = []
        sum_nums1 = 0
        max_score = 0
        
        for a, b in pairs:
            heapq.heappush(heap, a)
            sum_nums1 += a
            if len(heap) > k:
                sum_nums1 -= heapq.heappop(heap)
            if len(heap) == k:
                max_score = max(max_score, sum_nums1 * b)
                
        return max_score        