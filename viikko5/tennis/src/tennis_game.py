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
        temp_score = 0

        if self.player1_points >= 4 or self.player2_points >= 4: 
            score_text =  self.score_for_four_and_higher()

        elif self.player1_points == self.player2_points:
            if self.player1_points == 0:
                score_text = "Love-All"
            elif self.player1_points == 1:
                score_text = "Fifteen-All"
            elif self.player1_points == 2:
                score_text = "Thirty-All"
            elif self.player1_points == 3:
                score_text = "Forty-All"
            else:
                score_text = "Deuce"

        else:
            for i in range(1, 3):
                if i == 1:
                    temp_score = self.player1_points
                else:
                    score_text = score_text + "-"
                    temp_score = self.player2_points

                if temp_score == 0:
                    score_text = score_text + "Love"
                elif temp_score == 1:
                    score_text = score_text + "Fifteen"
                elif temp_score == 2:
                    score_text = score_text + "Thirty"
                elif temp_score == 3:
                    score_text = score_text + "Forty"

        return score_text

    def score_for_four_and_higher(self):
        difference_in_points = self.player1_points - self.player2_points

        if difference_in_points < -2: difference_in_points = -2
        if difference_in_points > 2: difference_in_points = 2

        score_text_options = [f'Win for {self.player2_name}', 
                                f'Advantage {self.player2_name}', 
                                'Deuce', 
                                f'Advantage {self.player1_name}', 
                                f'Win for {self.player1_name}']

        return score_text_options[difference_in_points + 2]