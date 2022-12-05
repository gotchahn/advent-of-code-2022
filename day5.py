import re

class Day5:
    test_stacks = [
        ['Z', 'N'],
        ['M', 'C', 'P'],
        ['P']
    ]

    puzzle_stacks = [
        ['R', 'N', 'F', 'V', 'L', 'J', 'S', 'M'],
        ['P', 'N', 'D', 'Z', 'F', 'J', 'W', 'H'],
        ['W', 'R', 'C', 'D', 'G'],
        ['N', 'B', 'S'],
        ['M', 'Z', 'W', 'P', 'C', 'B', 'F', 'N'],
        ['P', 'R', 'M', 'W'],
        ['R', 'T', 'N', 'G', 'L', 'S', 'W'],
        ['Q', 'T', 'H', 'F', 'N', 'B', 'V'],
        ['L', 'M', 'H', 'Z', 'N', 'F']
    ]

    def rearrangement(self, puzzle, option, test):
        instructions = puzzle.split("\n")
        stacks = self.test_stacks if test == True else self.puzzle_stacks

        for instruction in instructions:
            temp = re.findall(r'\d+', instruction)
            inst_vals = list(map(int, temp))
            # inst_vals:
            # [0] how many stacks to be moved
            # [1] from [2] to
            how_many = inst_vals[0]
            from_stack = inst_vals[1] - 1
            to_stack = inst_vals[2] - 1

            if option == 1:
                for x in range(0, how_many):
                    val = stacks[from_stack].pop()
                    print('Moving',val,'from stack',from_stack+1,'to',to_stack+1)
                    stacks[to_stack].append(val)
            else:
                temp_stack = [stacks[from_stack].pop() for _ in range(how_many)]
                stacks[to_stack].extend([temp_stack.pop() for _ in range(how_many)])

        self.print_tops(stacks)

    def print_tops(self, stacks):
        tops = ''
        for stack in stacks:
            if len(stack) > 0:
                tops += stack.pop()
        print(tops)
