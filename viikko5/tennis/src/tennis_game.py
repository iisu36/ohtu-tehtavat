class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_points = 0
        self.player2_points = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_points = self.player1_points + 1
        else:
            self.player2_points = self.player2_points + 1

    def get_score(self):
        score_text = ""

        if self.player1_points >= 4 or self.player2_points >= 4: 
            score_text =  self.score_for_four_points_and_higher()
        else:
            score_text = self.score_up_to_forty()

        return score_text

    def score_for_four_points_and_higher(self):
        difference_in_points = self.player1_points - self.player2_points

        if difference_in_points < -2: difference_in_points = -2
        elif difference_in_points > 2: difference_in_points = 2

        score_text_options = [f'Win for {self.player2_name}', 
                                f'Advantage {self.player2_name}', 
                                'Deuce', 
                                f'Advantage {self.player1_name}', 
                                f'Win for {self.player1_name}']

        return score_text_options[difference_in_points + 2]

    def score_up_to_forty(self):
        score_text_options = ['Love', 'Fifteen', 'Thirty', 'Forty']

        score_text = score_text_options[self.player1_points] + '-'

        if self.player1_points == self.player2_points:
            score_text += 'All'
        else:
            score_text += score_text_options[self.player2_points]

        return score_text