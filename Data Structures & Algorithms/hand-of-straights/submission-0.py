class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        count = Counter(hand)
        for value in hand:
            if count[value] > 0:
                for next_val in range(value, value+groupSize):
                    if count[next_val] == 0:
                        return False
                    count[next_val] -= 1
        return True
                    