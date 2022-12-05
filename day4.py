class Day4:

    def overlap(self, raw_input, option):
        input_collected = raw_input.split("\n")
        total = 0

        for teams in input_collected:
            team = teams.split(",")
            elf1 = team[0].split("-")
            elf2 = team[1].split("-")

            elf1_start = int(elf1[0])
            elf1_end = int(elf1[1])
            elf2_start = int(elf2[0])
            elf2_end = int(elf2[1])

            if option == 1:
                if elf1_start >= elf2_start and elf1_end <= elf2_end:
                    print(team[0],'is contain in',team[1])
                    total += 1
                elif elf2_start >= elf1_start and elf2_end <= elf1_end:
                    print(team[1],'is contain in',team[0])
                    total += 1
            else:
                p1 = list(range(elf1_start,elf1_end+1))
                p2 = list(range(elf2_start,elf2_end+1))
                commons1 = set(p1) & set(p2)
                commons2 = set(p2) & set(p1)

                if len(commons1) > 0 or len(commons2) > 0:
                    print(team[0],'overlapping',team[1])
                    total += 1

        return total
