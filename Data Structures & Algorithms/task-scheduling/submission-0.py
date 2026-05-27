from collections import defaultdict, Counter
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cooldown = deque([]) # (available_at, count)
        clock = 0
        queue = [count for count in Counter(tasks).values()]
        heapq.heapify_max(queue)

        while queue or cooldown:
            clock += 1
        	# First process the available after cooldown
            while cooldown and cooldown[0][0] <= clock:
                heapq.heappush_max(queue, cooldown.popleft()[1])

            # Then process the highest priority
            if queue:
	            count = heapq.heappop_max(queue)
	            if count > 1: 
	            	cooldown.append((clock+n+1, count-1))

        return clock
        