class Team(object):
    def __init__(self, team_data, season):
        self.id = team_data['id']
        self.name = team_data['abbreviation']
        self.season = season

        roster_list = team_data['roster']['roster']

        self.players = [
            Player(player, self)._to_dict() for player in roster_list
        ]


class Player(object):
    def __init__(self, player: dict, team: Team):
        self.id = player['person']['id']
        self.fullName = player['person']['fullName']
        self.position = player['position']['abbreviation']
        self.team_id = team.id
        self.team_name = team.name
        self.season = team.season

    def _to_dict(self):
        return {
            "id": self.id,
            "fullName": self.fullName,
            "position": self.position,
            "team_id": self.team_id,
            "team_name": self.team_name,
            "season": self.season
        }