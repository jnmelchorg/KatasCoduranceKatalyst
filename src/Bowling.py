def score(game: str) -> int:
    total_score = 0
    for string in  game.split("|")[0]:
        if string != "-":
            total_score += int(string)
    return total_score

