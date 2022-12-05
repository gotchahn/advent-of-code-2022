class Day3:
    lower_priority = 96
    upper_priority = 27

    def priority(self, common):
        ordinal = ord(common)
        if ordinal >= ord('a'):
            # lowecase
            point = ordinal - self.lower_priority
        else:
            # upper case
            point = ordinal - ord('A') + self.upper_priority

        return point

    def sum_priority(self, raw_input, option):
        input_collected = raw_input.split("\n")
        total = 0

        if option == 1:
            for items in input_collected:
                item_len = len(items)
                half_index = int(item_len/2)

                first_compartment = items[0:half_index]
                second_compartment =  items[half_index:item_len]

                common = ''.join(set(first_compartment).intersection(second_compartment))
                print('Common :',common)
                point = self.priority(common)

                print("Adding", point, 'to', total)
                total = total + point
        else:
            start = 0
            end = 3
            len_collected = len(input_collected)

            while start < len_collected:
                team = input_collected[start:end]
                common_set = set(team[0]) & set(team[1]) & set(team[2])
                common = list(common_set)[0]

                print('Common :',common)
                point = self.priority(common)

                print("Adding", point, 'to', total)
                total = total + point

                start += 3
                end += 3


        return total
