class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.time, tweetId])
        self.time -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        newsFeed = []
        heap = []

        self.following[userId].add(userId)
        for followeeId in self.following[userId]:
            if followeeId in self.tweets:
                idx = len(self.tweets[followeeId])-1
                time, tweetId = self.tweets[followeeId][idx]
                heap.append([time, tweetId, followeeId, idx])
        heapq.heapify(heap)

        while heap and len(newsFeed) < 10:
            time, tweetId, followeeId, idx = heapq.heappop(heap)
            newsFeed.append(tweetId)

            if idx > 0:
                idx -= 1
                time, tweetId = self.tweets[followeeId][idx]
                heapq.heappush(heap, [time, tweetId, followeeId, idx])
        
        return newsFeed


        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
        
