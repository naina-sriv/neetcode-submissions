import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[-i for i in stones]
        heapq.heapify(heap)
        while len(heap)>1:
            first=heapq.heappop(heap)
            sec=heapq.heappop(heap)
            if first!=sec:
                heapq.heappush(heap,first-sec)
        return -heap[0] if heap else 0