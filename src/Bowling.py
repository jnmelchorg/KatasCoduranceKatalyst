def __calculate_score(game: str) -> int:
    if game[0] == "|":
        return 0
    if "/" in game.split("|")[0]:
        if game.split("|")[1] != "":
            return __calculate_score_from_spare(game)
        else:
            return __calculate_score_from_additional_roll_for_spare(game)
    elif "X" in game.split("|")[0]:
        if game.split("|")[1] != "":
            return __calculate_score_from_strike(game)
        else:
            return __calculate_score_from_additional_rolls_for_strike(game)
    else:
        partial_score = __calculate_score_from_frame(game.split("|")[0])
        return partial_score + __calculate_score(game[3:])


def __calculate_score_from_strike(game: str) -> int:
    if "/" in game.split("|")[1]:
        partial_score = 20
    elif "X" in game.split("|")[1]:
        if game.split("|")[2] != "":
            partial_score = __calculate_score_from_second_strike(game.split("|")[2])
        else:
            partial_score = __calculate_score_from_second_strike(game.split("|")[3])
    else:
        partial_score = 10 + __calculate_score_from_frame(game.split("|")[1])
    return partial_score + __calculate_score(game[2:])


def __calculate_score_from_additional_rolls_for_strike(game: str) -> int:
    if game.split("|")[2] == "XX":
        return 30
    if game.split("|")[2][0] == "X":
        return 20 + int(game.split("|")[2][1]) if game.split("|")[2][1] != "-" else 20
    elif game.split("|")[2][1] == "X":
        return 20 + int(game.split("|")[2][0]) if game.split("|")[2][0] != "-" else 20
    return 10 + __calculate_score_from_frame(game.split("|")[2])


def __calculate_score_from_second_strike(frame: str) -> int:
    if (len(frame) == 1 and "X" in frame) or (len(frame) == 2 and "X" in frame[0]):
        return 30
    else:
        return 20 + int(frame[0]) if frame[0] != "-" else 20


def __calculate_score_from_spare(game: str) -> int:
    partial_score = 10 + int(game.split("|")[1][0]) if game.split("|")[1][0] != "-" else 10
    return partial_score + __calculate_score(game[3:])


def __calculate_score_from_additional_roll_for_spare(game: str) -> int:
    if game.split("|")[2][0] == "X":
        partial_score = 20
    elif game.split("|")[2][0] != "-":
        partial_score = 10 + int(game.split("|")[2][0])
    else:
        partial_score = 10
    return partial_score


def __calculate_score_from_frame(frame: str) -> int:
    partial_score = 0
    for string in frame:
        if string != "-":
            partial_score += int(string)
    return partial_score


def score(game: str) -> int:
    __check_input_for_errors(game)
    return __calculate_score(game)


def __check_input_for_errors(game: str) -> None:
    if len(game.split("|")) > 12:
        raise ValueError(f"A bowling game must have 10 frames and an additional frame in case of a strike or spare in "
                         f"the 10th frame, which should result on a maximum of 11 frames. However the provided input "
                         f"has {len(game.split('|')) - 1} frames.")
    frames = game.split("|")
    for counter in range(10):
        if len(frames[counter]) > 2 or len(frames[counter]) == 0:
            raise ValueError(f"A frame should have 1 or 2 rolls. However the frame {counter} has "
                             f"{len(frames[counter])} rolls.")
    for counter in range(10):
        if len(frames[counter]) == 1 and frames[counter] != "X":
            raise ValueError(f"A frame should have only 1 roll when the roll is a strike. However, frame {counter} is"
                             f"not a strike but have one roll.")
    if "||" not in game:
        raise ValueError("No separator || to indicate additional games was found in the input.")
