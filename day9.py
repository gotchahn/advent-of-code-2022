class Dot:
    def __init__(self, x, y):
        self.setCoords(x, y)

    def setCoords(self, x, y):
        self.x = x
        self.y = y

class Day9:

    def __init__(self, dots, initx, inity):
        self.tailVisited = []
        self.dots = []
        self.totalDots = dots
        # set the rope
        for d in range(dots):
            self.dots.append(Dot(initx, inity))
        self.tailVisited.append(f"{inity}-{initx}")

    def nextToHead(self, dotn):
        if dotn == 0:
            return True

        difx = self.dots[dotn-1].x - self.dots[dotn].x
        dify = self.dots[dotn-1].y - self.dots[dotn].y

        return (difx in range(-1, 2)) and (dify in range(-1, 2))

    def move(self, puzzle):
        instructions = puzzle.split("\n")

        for instruction in instructions:
            detail = instruction.split()
            direction = detail[0]
            amount = int(detail[1])

            for a in range(amount):
                print("\nMove 1 to the", direction)

                if direction == 'U':
                    self.dots[0].y -= 1
                elif direction == 'D':
                    self.dots[0].y += 1
                elif direction == 'L':
                    self.dots[0].x -= 1
                else:
                    self.dots[0].x += 1

                print('Moving H to [', self.dots[0].y, ',', self.dots[0].x, ']')

                for d in range(1, self.totalDots):

                    if not self.nextToHead(d):
                        print('Need to move the T', d)

                        if self.dots[d-1].x == self.dots[d].x:
                            # same column
                            self.dots[d].y += -1 if self.dots[d-1].y < self.dots[d].y else 1
                        elif self.dots[d-1].y == self.dots[d].y:
                            # same row
                            self.dots[d].x += -1 if self.dots[d-1].x < self.dots[d].x else 1
                        else:
                            # diagonal
                            if self.dots[d-1].y < self.dots[d].y:
                                if self.dots[d-1].x > self.dots[d].x:
                                    # go up right
                                    self.dots[d].x += 1
                                    self.dots[d].y -= 1
                                else:
                                    # go up left
                                    self.dots[d].x -= 1
                                    self.dots[d].y -= 1
                            else:
                                if self.dots[d-1].x > self.dots[d].x:
                                    # go down right
                                    self.dots[d].x += 1
                                    self.dots[d].y += 1
                                else:
                                    # go down left
                                    self.dots[d].x -= 1
                                    self.dots[d].y += 1

                        print('Moving T',d,'to [', self.dots[d].y, ',', self.dots[d].x, ']')

                        if d == (self.totalDots - 1):
                            print('Was the tail')
                            coord = f"{self.dots[d].y}-{self.dots[d].x}"
                            if not (coord in self.tailVisited):
                                print("Saving coord", coord)
                                self.tailVisited.append(coord)
                    else:
                        break

                # print('Moving T to [', self.tailx, ',', self.taily, ']')

        return len(self.tailVisited)
