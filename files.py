from utils.conversions import *


# Generator for desplaying files list on the screen
def desplayFiles(fileList, limit):
    no = len(fileList)
    for i in range(no):
        file = fileList[i]
        name = file["name"]
        bitDepth = file["bitDepth"] if "bitDepth" in file else ""
        sampleRate = ratekHz(file["sampleRate"]) if "sampleRate" in file else ""
        length = timemin(file["length"]) if "length" in file else ""
        size = sizeMB(file["size"]) if "size" in file else ""
        time = f"{length[0]}.{f"0{length[1]}" if length[1] < 10 else length[1]}"
        desplay = f"\n[{i}] {file["filename"]}\n\t{name} [ \033[33m{bitDepth} bit\033[0m/\033[31m{sampleRate} khz\033[0m | \033[32m{size} MB\033[0m | \033[34m{time}\033[0m ]"
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
            return cmd
    else:
        return cmd
