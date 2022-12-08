class Day8:
    treeMap = []

    def __init__(self, board):
        self.buildMap(board.split("\n"))

    def buildMap(self, coords):
        for coord in coords:
            row = list(int(x) for x in coord)
            self.treeMap.append(row)
        self.xLen = len(self.treeMap[0])
        self.yLen = len(self.treeMap)

    def vTop(self, val, x, y):
        treeVal = self.treeMap[x][y]
        if treeVal >= val:
            # tree top will hide trip
            return False
        else:
            if y == 0:
                return True
            else:
                return self.vTop(val, x, y - 1)

    def vDown(self, val, x, y):
        treeVal = self.treeMap[x][y]
        if treeVal >= val:
            # tree top will hide trip
            return False
        else:
            if y == self.yLen - 1:
                return True
            else:
                return self.vDown(val, x, y + 1)

    def vLeft(self, val, x, y):
        treeVal = self.treeMap[x][y]
        if treeVal >= val:
            # tree top will hide trip
            return False
        else:
            if x == 0:
                return True
            else:
                return self.vLeft(val, x - 1, y)

    def vRight(self, val, x, y):
        treeVal = self.treeMap[x][y]
        if treeVal >= val:
            # tree top will hide trip
            return False
        else:
            if x == self.xLen - 1:
                return True
            else:
                return self.vRight(val, x + 1, y)

    def visible(self):
        totalVisible = (self.xLen * 2 ) + (self.yLen - 2) * 2
        print('visible starts with', totalVisible)

        for x in range(1, self.xLen - 1):
            for y in range(1, self.yLen - 1):
                treeVal = self.treeMap[x][y]
                visibleTop = self.vTop(treeVal, x, y - 1)
                visibleDown = self.vDown(treeVal, x, y + 1)
                visibleLeft = self.vLeft(treeVal, x - 1, y)
                visibleRight = self.vRight(treeVal, x + 1, y)

                if visibleTop or visibleDown or visibleLeft or visibleRight:
                    totalVisible += 1

        return totalVisible

    def sTop(self, val, x, y):
        treeVal = self.treeMap[x][y]
        if treeVal >= val:
            # tree top will hide trip
            return 1
        else:
            if y == 0:
                return 1
            else:
                return 1 + self.sTop(val, x, y - 1)

    def sDown(self, val, x, y):
        treeVal = self.treeMap[x][y]
        if treeVal >= val:
            # tree top will hide trip
            return 1
        else:
            if y == self.yLen - 1:
                return 1
            else:
                return 1 + self.sDown(val, x, y + 1)

    def sLeft(self, val, x, y):
        treeVal = self.treeMap[x][y]
        if treeVal >= val:
            # tree top will hide trip
            return 1
        else:
            if x == 0:
                return 1
            else:
                return 1 + self.sLeft(val, x - 1, y)

    def sRight(self, val, x, y):
        treeVal = self.treeMap[x][y]
        if treeVal >= val:
            # tree top will hide trip
            return 1
        else:
            if x == self.xLen - 1:
                return 1
            else:
                return 1 + self.sRight(val, x + 1, y)

    def score(self):
        totalScore = []

        for x in range(1, self.xLen - 1):
            for y in range(1, self.yLen - 1):
                treeVal = self.treeMap[x][y]
                scoreTop = self.sTop(treeVal, x, y - 1)
                scoreDown = self.sDown(treeVal, x, y + 1)
                scoreLeft = self.sLeft(treeVal, x - 1, y)
                scoreRight = self.sRight(treeVal, x + 1, y)

                totalScore.append(scoreTop * scoreDown * scoreLeft * scoreRight)

        return max(totalScore)
