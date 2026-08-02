from utils.conversions import *


# Generator for desplaying files list on the screen
def desplayFiles(fileList, limit):
    no = len(fileList)
    for i in range(no):
        file = fileList[i]
        name = file["name"]
        bitDepth = depthbit(file["bitDepth"]) if "bitDepth" in file else ""
        sampleRate = ratekhz(file["sampleRate"]) if "sampleRate" in file else ""
        length = timemin(file["length"]) if "length" in file else ""
        size = sizeMb(file["size"]) if "size" in file else ""
        desplay = f"\n[{i}] {file["filename"]}\n\t{name} [ \033[31m{sampleRate}\033[0m | \033[33m{bitDepth}\033[0m | \033[32m{size}\033[0m | \033[34m{length}\033[0m ]"
        print(desplay)
        if i % limit == limit - 1:
            yield


# Function to get user selection
def getSelection(desplay):
    cmd = input("\nEnter a number or press Enter to see more files:- ")
    if cmd == "":
        try:
            next(desplay)
            return getSelection(desplay)
        except:
            cmd = input("\nEnd of file list, Please enter a number:- ")
            return int(cmd)
    else:
        return int(cmd)
