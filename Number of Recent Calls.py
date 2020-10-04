class RecentCounter(object):

    def __init__(self):
        self.times = deque()
        self.WINDOW = 3000
        

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.times.append(t)
        while t - self.times[0] > self.WINDOW:
            self.times.popleft()
            
        return len(self.times)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)