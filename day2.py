class Day2:
    move_points = dict(X=1, Y=2, Z=3)
    sames = dict(X='A', Y='B', Z='C')
    sames_reverted = dict(A='X', B='Y', C='Z')
    beats = dict(X='C', Y='A', Z='B')
    beats_reverted = dict(A='Y', B='Z', C='X')
    loses = dict(A='Z', B='X', C='Y')

    def challenge_total(self, raw_input, option):
        input_collected = raw_input.split("\n")
        total = 0
        for challenge in input_collected:
            moves = challenge.split()
            their_move = moves[0]
            my_move = moves[1]

            challenge_point = 0
            move_point = 0

            if option == 1:
                move_point = self.move_points[my_move]

                if self.sames[my_move] == their_move:
                    challenge_point = 3
                elif self.beats[my_move] == their_move:
                    challenge_point = 6

            else:
                if my_move == 'X':
                    # need to lose
                    move_point = self.move_points[self.loses[their_move]]
                elif my_move == 'Y':
                    # need to draw
                    challenge_point = 3
                    move_point = self.move_points[self.sames_reverted[their_move]]
                else:
                    # need to win
                    challenge_point = 6
                    move_point = self.move_points[self.beats_reverted[their_move]]

            print('Adding',(move_point + challenge_point), 'to', total)
            total = total + move_point + challenge_point

        return total
