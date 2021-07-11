import os.path

SCORES_FILE_NAME = "score/Scores.txt"
BAD_RETURN_CODE = -1


def Screen_cleaner():
    os.system('cls' if os.name == 'nt' else 'clear')


def read_score_file(filename):
    if not os.path.isfile(filename):
        current_point_of_score = 0
        f = open(filename, 'w')
        f.write(str(current_point_of_score))
        f.close()
    else:
        f = open(filename, 'r')
        current_point_of_score = f.readline()

    return current_point_of_score

def write_score_file(old_point_of_winning, new_point_of_winning,filename):
    f = open(filename, 'w')
    current_point_of_winning = old_point_of_winning+new_point_of_winning
    f.write(str(current_point_of_winning))
    return True

