class Day10:
    def __init__(self):
        self.checkCycles = [20, 60, 100, 140, 180, 220]
        self.sprite = []
        self.crt = []
        self.initScreen()

    def initSprite(self):
        start = self.x - 1
        self.sprite = [s for s in range(start, start + 3)]

    def initScreen(self):
        self.cycles = 1
        self.strengths = []
        self.x = 1
        self.position = 0
        row = ['.' for x in range(40)]
        for r in range(6):
            self.crt.append(row.copy())
        self.initSprite()

    def checkStrength(self):
        if self.cycles in self.checkCycles:
            self.strengths.append(self.cycles * self.x)

    def drawPixel(self):
        row = int(self.cycles/40)
        self.crt[row][self.position] = '#' if self.position in self.sprite else '.'
        self.incrementPosition()

    def incrementPosition(self):
        self.position += 1
        if self.position == 40:
            self.position = 0

    def noop(self):
        self.checkStrength()
        self.cycles += 1
        self.drawPixel()

    def addx(self, v):
        for s in range(2):
            self.checkStrength()
            self.cycles += 1
            self.drawPixel()
        self.x += v
        self.initSprite()

    def printCRT(self):
        for r in range(6):
            for c in range(40):
                print(self.crt[r][c], end = "")
            print("")
        print()

    def strength(self, program):
        self.initScreen()
        commands = program.split("\n")

        for command in commands:
            if command.startswith('noop'):
                self.noop()
            else:
                val = int(command.split()[1])
                self.addx(val)

        self.printCRT()
        return sum(self.strengths)
