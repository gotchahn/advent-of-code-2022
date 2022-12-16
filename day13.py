import ast
import functools
import copy

class Pair:
    def __init__(self, leftStr, rightStr):
        self.left = ast.literal_eval(leftStr) if type(leftStr) == str else leftStr
        self.right = ast.literal_eval(rightStr) if type(rightStr) == str else rightStr

    def compare2(self, leftColl, rightColl):
        lenLeft = len(leftColl)
        lenRight = len(rightColl)

        if lenRight == 0 and lenLeft > 0:
            print('Right is out of elements')
            return 1
        elif lenLeft == 0 and lenRight > 0:
            print('Left is out of elements')
            return -1
        elif lenLeft == 0 and lenRight == 0:
            return 0


        leftElement = leftColl.pop(0)
        rightElement = rightColl.pop(0)
        print('Compare', leftElement, 'vs', rightElement)

        if type(leftElement) == type(rightElement):
            # check if integer
            if type(leftElement) == int:
                if leftElement < rightElement:
                    return -1
                elif rightElement < leftElement:
                    return 1
                else:
                    # continue
                    return self.compare2(leftColl, rightColl)
            else:
                # both arrays
                val = self.compare2(leftElement, rightElement)
                if val == 0 and (len(leftColl) + len(rightColl)) > 0:
                    # somehow was [] vs []
                    print('Edge case empty array, continue to next one')
                    return self.compare2(leftColl, rightColl)
                else:
                    return val
        else:
            # diff type
            if type(leftElement) == int:
                leftColl.insert(0, [leftElement])
                rightColl.insert(0, rightElement)
            else:
                leftColl.insert(0, leftElement)
                rightColl.insert(0, [rightElement])

            return self.compare2(leftColl, rightColl)

    def compare(self):

        while True:
            result = self.compare2(self.left, self.right)

            if result in [-1, 1]:
                break

            if len(self.left) == 0 and len(self.right) == 0:
                return 0

        return result


class Day13:
    def __init__(self, puzzle):
        instructions = puzzle.split("\n\n")
        self.pairs = []

        for instruction in instructions:
            vals = instruction.split("\n")
            self.pairs.append(Pair(vals[0], vals[1]))

    def distress(self):
        rights = []
        counter = 1

        for pair in self.pairs:
            print(f"== Pair {counter} ==")

            if pair.compare() == -1:
                print('Adding Pair', counter, ' to the rights')
                rights.append(counter)

            counter += 1
            print("\n")

        return sum(rights)

    def cmp(self, a, b):
        pair = Pair(copy.deepcopy(a), copy.deepcopy(b))
        return pair.compare()

    def divider(self):
        allPackages = []
        for pair in self.pairs:
            allPackages.append(pair.left)
            allPackages.append(pair.right)
        allPackages.append([[2]])
        allPackages.append([[6]])

        sortedPackages = sorted(allPackages, key=functools.cmp_to_key(self.cmp))

        index = 1
        multiplier = 1

        print('\nAll Sorted:\n---------------')
        for s in sortedPackages:
            if s == [[2]] or s == [[6]]:
                multiplier *= index
            print(s)
            index += 1

        return multiplier
