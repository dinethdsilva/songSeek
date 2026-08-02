# seconds -> minutes
def timemin(sec):
    min = sec // 60
    sec = sec % 60
    if sec < 10:
        sec = f"0{sec}"
    return f"{min}.{sec}"


# bytes -> Megabytes
def sizeMb(b):
    return f"{round(b / 1_048_576, 2)} MB"


# hz -> khz
def ratekhz(hz):
    return f"{round(hz / 1000, 2)} kHz"


# bits
def depthbit(bits):
    return f"{bits} bits"
