class Day1:
    def __init__(self, raw_input):
        self.input_collected = raw_input.split("\n\n")

    def max_collected(self, option):
        sums = []

        # get the sums
        for row in self.input_collected:
            iterator = map(lambda convert: int(convert), row.split())
            sums.append(sum(list(iterator)))

        if option == 1:
            return max(sums)
        else:
            return sum(sorted(sums, reverse=True)[:3])
