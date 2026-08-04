# seconds -> minutes,seconds
def timemin(sec):
    min = sec // 60
    sec = sec % 60
    return (min, sec)


# B -> MB
def sizeMB(B):
    return round(B / 1_048_576, 1)


# Hz -> kHz
def ratekHz(Hz):
    return round(Hz / 1000, 2)
