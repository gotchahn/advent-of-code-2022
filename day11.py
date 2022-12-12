import re
import math

class Monkey:
    def __init__(self, initItems, formula, testDiv, ifTrue, ifFalse):
        self.items = initItems
        self.itemsInspected = 0
        self.formula = formula
        self.testDiv = testDiv
        self.toMokeyIfTrue = ifTrue
        self.toMokeyIfFalse = ifFalse

    def inspectElement(self, option, lcm):
        item = self.items.pop(0)
        self.itemsInspected += 1
        # eval formula
        context = dict(old = item)
        newWorry = lambda: eval(self.formula, context)

        if option == 1:
            bored = int(newWorry() / 3)
        else:
            bored = newWorry() % lcm
        throwTo = self.toMokeyIfTrue if bored % self.testDiv == 0 else self.toMokeyIfFalse

        return {'item': bored, 'toMonkey': throwTo}

    def receiveItem(self, item):
        self.items.append(item)

class Day11:
    def __init__(self, puzzle):
        self.inputs = puzzle.split("\n\n")
        self.divisibleBys = []
        self.createMonkeys(input)

    def extractNumbers(self, instruction):
        temp = re.findall(r'\d+', instruction)
        return list(map(int, temp))

    def createMonkeys(self, puzzle):
        self.monkeys = []
        for input in self.inputs:
            instruction = [s.strip() for s in input.split("\n")]
            #items
            items = self.extractNumbers(instruction[1])
            #new worry formula
            vals = [s.strip() for s in instruction[2].split("=")]
            formula = vals[1]
            # divisible
            divisible = self.extractNumbers(instruction[3])[0]
            self.divisibleBys.append(divisible)
            #if true
            ifTrue = self.extractNumbers(instruction[4])[0]
            #if else
            ifFalse = self.extractNumbers(instruction[5])[0]

            print('Creating monkey with items', *items, 'Formula:', formula, end = " ")
            print('Divisible:', divisible, 'test true:', ifTrue, 'test false:', ifFalse)

            self.monkeys.append(Monkey(items, formula, divisible, ifTrue, ifFalse))

    def rounds(self, amount, option):
        m = 0
        lcm = math.lcm(*self.divisibleBys)
        print('LCM', lcm)

        for round in range(amount):
            for monkey in self.monkeys:
                lenItems = len(monkey.items)
                for item in range(lenItems):
                    inspection = monkey.inspectElement(option, lcm)
                    # print('Monkey', m, 'throw item', inspection['item'], 'to monkey', inspection['toMonkey'])
                    self.monkeys[inspection['toMonkey']].receiveItem(inspection['item'])
                m += 1

        m = 0
        maxInspected = []
        for monkey in self.monkeys:
            maxInspected.append(monkey.itemsInspected)
            print('Monkey', m, 'inspected', monkey.itemsInspected, 'items')
            m += 1

        max2 = sorted(maxInspected, reverse=True)[:2]
        return max2[0] * max2[1]
