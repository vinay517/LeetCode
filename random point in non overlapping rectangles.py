class Solution(object):

    def __init__(self, rects):
        """
        :type rects: List[List[int]]
        """
        self.cumul_area = [0]
        self.x_dimensions = [0]
        self.rects = rects
        
        for x1, y1, x2, y2 in rects:
            x_dim, y_dim = x2 - x1 +1, y2 - y1 +1
            self.x_dimensions.append(x_dim)
            self.cumul_area.append(self.cumul_area[-1] + x_dim * y_dim)

    def pick(self):
        """
        :rtype: List[int]
        """
        n = random.randint(1, self.cumul_area[-1])
        i = bisect.bisect_left(self.cumul_area, n)
        n -= (self.cumul_area[i-1] +1)
        
        dy, dx = divmod(n,self.x_dimensions[i])
        x, y = self.rects[i-1][:2]
        return [x + dx, y + dy]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()