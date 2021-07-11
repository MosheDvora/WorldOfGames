from Utils import SCORES_FILE_NAME, read_score_file, write_score_file
import os.path


def add_score(difficulty):
    old_point_of_winning = int(read_score_file(SCORES_FILE_NAME))
    new_point_of_winning = (difficulty * 3) + 5
    write_score_file(old_point_of_winning, new_point_of_winning, SCORES_FILE_NAME)
    return True
