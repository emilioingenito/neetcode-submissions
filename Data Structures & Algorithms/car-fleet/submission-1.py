class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arrivals_positions = [(pos, (target-pos)/vel) for pos, vel in zip(position, speed)]
        arrivals_positions.sort()
        arrivals = [arrival for _, arrival in arrivals_positions]

        
        fleets = 0
        while arrivals:
            arrival = arrivals.pop()
            while arrivals and arrivals[-1] <= arrival:
                arrivals.pop()
            fleets += 1
        
        return fleets

        