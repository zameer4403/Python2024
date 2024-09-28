class Match:
    def __init__(self, match_id, team1, team2, score1, score2):
        self.match_id = match_id
        self.team1 = team1
        self.team2 = team2
        self.score1 = score1
        self.score2 = score2

class MatchResultManager:
    def __init__(self):
        self.matches = {}

    def record_game_outcomes(self, match_id, team1, team2, score1, score2):
        if score1 < 0 or score2 < 0:
            raise ValueError("Scores must be non-negative.")
        if not team1 or not team2:
            raise ValueError("Team names must not be empty.")
        self.matches[match_id] = Match(match_id, team1, team2, score1, score2)

    def delete_game_result(self, match_id):
        if match_id in self.matches:
            del self.matches[match_id]
        else:
            raise KeyError(f"No match found with ID: {match_id}")

    def retrieve_game_result(self, match_id):
        match = self.matches.get(match_id)
        if match is None:
            raise KeyError(f"No match found with ID: {match_id}")
        return vars(match)

    def analyze_team_performance(self, team_id):
        performance = {'games_played': 0, 'wins': 0, 'draws': 0, 'losses': 0}
        for match in self.matches.values():
            if team_id in (match.team1, match.team2):
                performance['games_played'] += 1
                if (team_id == match.team1 and match.score1 > match.score2) or \
                   (team_id == match.team2 and match.score2 > match.score1):
                    performance['wins'] += 1
                elif match.score1 == match.score2:
                    performance['draws'] += 1
                else:
                    performance['losses'] += 1
        return performance

    def display_match_results(self):
        for match in self.matches.values():
            print(f"Match ID: {match.match_id} | {match.team1} {match.score1} - {match.score2} {match.team2}")

# Example Usage
manager = MatchResultManager()
manager.record_game_outcomes("001", "Team A", "Team B", 3, 1)
manager.record_game_outcomes("002", "Team A", "Team B", 0, 0)
manager.display_match_results()
print(manager.analyze_team_performance("Team B"))
