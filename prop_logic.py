def get_prop_picks(game_filter):
    picks = [
        {"player": "Aaron Judge", "prop_type": "Over 1.5 Total Bases", "confidence": 82, "reason": "Hot streak + favorable pitcher matchup"},
        {"player": "Shohei Ohtani", "prop_type": "Over 0.5 Home Runs", "confidence": 65, "reason": "Wind blowing out + good park factor"},
        {"player": "Freddie Freeman", "prop_type": "Over 1.5 Hits", "confidence": 78, "reason": "Great vs LHP + consistent contact"},
        {"player": "Gerrit Cole", "prop_type": "Over 6.5 Strikeouts", "confidence": 88, "reason": "High K/9 vs a strikeout-heavy team"},
    ]
    if game_filter != "All Games":
        picks = [p for p in picks if game_filter in p["player"]]
    return picks
