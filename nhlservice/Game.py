class Game(object):
    """
    Collects a game log and converts it into a nicer object
    """
    def __init__(self, id, game_log):

        season = game_log['season']
        stats = game_log['stat']
        game_id = game_log['game']['gamePk']

        self.stats = {
            "season": season,
            "player_id": id,
            "game_id": game_id,
            "timeOnIce": stats["timeOnIce"],
            "assists": stats["assists"],
            "goals": stats['goals'],
            "pim": stats["pim"],
            "shots": stats["shots"],
            "hits": stats["hits"],
            "blocked": stats["blocked"],
            "plusMinus": stats["plusMinus"],
            "points": stats["points"],
            "shifts": stats["shifts"],
            "powerPlayGoals": stats["powerPlayGoals"],
            "powerPlayPoints": stats["powerPlayPoints"],
            "powerPlayTimeOnIce": stats["powerPlayTimeOnIce"],
            "evenTimeOnIce": stats["evenTimeOnIce"],
            "penaltyMinutes": stats["penaltyMinutes"],
            "gameWinningGoals": stats["gameWinningGoals"],
            "shortHandedGoals": stats["shortHandedGoals"],
            "shortHandedPoints": stats["shortHandedPoints"],
            "shortHandedTimeOnIce": stats["shortHandedTimeOnIce"],
            "team": game_log['team']['id'],
            "opponent": game_log['opponent']['id'],
            "isHome": game_log["isHome"],
            "isWin": game_log['isWin']
        }
