from collections import defaultdict
class Twitter:
    def __init__(self):
        self.tweets = defaultdict(list)
        self.followers = defaultdict(set)
        self.time = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = self.tweets[userId][:]
        for followee in self.followers[userId]:
            feed.extend(self.tweets[followee])
        
        topk = heapq.nlargest(10, feed)
        return [tweetId for _, tweetId in topk]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followers[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)