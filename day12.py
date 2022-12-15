import math

class Job:
    def __init__(self, r, c):
        self.row = r
        self.column = c

class Day12:
    minHeight = 97
    maxHeight = 122

    def __init__(self, board):
        self.board = board.split("\n")
        self.maxCols = len(self.board[0])
        self.maxRows = len(self.board)
        self.visited = []
        self.queue = []

    def initVisited(self):
        self.visited = []
        # init visited
        for r in range(self.maxRows):
            self.visited.append([-1 for x in range(self.maxCols)])
        self.queue = []

    def ordinal(self, element):
        if element == 'S':
            return self.minHeight
        elif element == 'E':
            return self.maxHeight
        else:
            return ord(element)

    def enqueueIfGoodStep(self, row, col, currentHeight, currentStep):
        if self.visited[row][col] >= 0:
            print('Already visited')
            return

        stepElement = self.board[row][col]

        diff = self.ordinal(stepElement) - currentHeight
        if diff <= 1:
            # add as a visited
            self.visited[row][col] = currentStep + 1
            # add to the queue
            print(f'Adding {row},{col} to the queue')
            self.queue.append(Job(row, col))
        else:
            print(f'Diff {diff} unreachable')

    def shortest(self, fromRow, fromCol):
        self.initVisited()
        self.queue.append(Job(fromRow, fromCol))
        self.visited[fromRow][fromCol] = 0
        stepsEnd = 0

        while len(self.queue) > 0:
            dequeue = self.queue.pop(0)
            print(f'Dequeuing {dequeue.row},{dequeue.column}')
            # get element
            element = self.board[dequeue.row][dequeue.column]
            elementHeight = self.ordinal(element)

            # get step
            step = self.visited[dequeue.row][dequeue.column]

            if element == 'E':
                print('E reached')
                return step

            # check if I can go up
            if dequeue.row > 0:
                print('Up', end=' ')
                self.enqueueIfGoodStep(dequeue.row - 1, dequeue.column, elementHeight, step)

            # check if I can go down
            if dequeue.row < self.maxRows - 1:
                print('Down', end=' ')
                self.enqueueIfGoodStep(dequeue.row + 1, dequeue.column, elementHeight, step)

            # check if I can go left
            if dequeue.column > 0:
                print('Left', end=' ')
                self.enqueueIfGoodStep(dequeue.row, dequeue.column - 1, elementHeight, step)

            # check if I can go right
            if dequeue.column < self.maxCols - 1:
                print('Right', end=' ')
                self.enqueueIfGoodStep(dequeue.row, dequeue.column + 1, elementHeight, step)

        #for r in range(self.maxRows):
            #for c in range(self.maxCols):
                #print(f"{self.visited[r][c]}", end = ",")
            #print("")

        #maxes = []
        #for r in range(self.maxRows):
            #maxes.append(max(self.visited[r]))
        return math.inf

    def shortest2(self):
        steps = []

        for r in range(self.maxRows):
            for c in range(self.maxCols):
                element = self.board[r][c]

                if element in ['a', 'S']:
                    steps.append(self.shortest(r, c))

        return min(steps)
