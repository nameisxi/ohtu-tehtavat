class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def same_score(self):
        scenarios = {
                0: 'Love-All',
                1: 'Fifteen-All',
                2: 'Thirty-All',
                3: 'Forty-All'
        }

        score = 'Deuce'

        if self.m_score1 in scenarios.keys():
            score = scenarios[self.m_score1]
        
        return score

    def over_four(self):
        minus_result = self.m_score1 - self. m_score2
        if minus_result >= 2: 
            minus_result = 2

        scenarios = {
            1: 'Advantage player1',
            -1: 'Advantage player2',
            2: 'Win for player1'
        }

        score = 'Win for player2'

        if minus_result in scenarios.keys():
            score = scenarios[minus_result]

        return score

    def other_scenarios(self):
        score = ""
        temp_score = 0

        scenarios = {
            0: 'Love',
            1: 'Fifteen',
            2: 'Thirty',
            3: 'Forty'
        }

        for i in range(1, 3):
            if i == 1:
                temp_score = self.m_score1
            else:
                score = score + "-"
                temp_score = self.m_score2

            score += scenarios[temp_score]
        
        return score

    def get_score(self):
        score = ""
        
        if self.m_score1 == self.m_score2:
            score = self.same_score()
        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            score = self.over_four()
        else:
            score = self.other_scenarios()

        return score
