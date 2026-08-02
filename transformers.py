# Return True if any downloadable files exist
def accessible(response):
    if response["fileCount"] > 0:
        return True
    else:
        return False


# Return score for successful download probability
def smartScore(response):
    hasFreeUploadSlot = response["hasFreeUploadSlot"]
    queueLength = response["queueLength"]
    uploadSpeed = response["uploadSpeed"]

    speedScore = min((uploadSpeed / 10_485_760) * 40, 40)
    queueScore = max(30 - queueLength * 3, 0)
    freeSlotScore = 15 if hasFreeUploadSlot else 0

    finalScore = speedScore + queueScore + freeSlotScore

    return finalScore


# Filter and sort given responses
def fsRes(responses):
    filterRes = filter(accessible, responses)
    sortRes = sorted(filterRes, key=smartScore, reverse=True)
    return sortRes


# Return True if file name contain all search terms
def nameMatch(fileName, searchTerms):
    for searchTerm in searchTerms:
        if searchTerm.lower() not in fileName.lower():
            return False
    return True


# List out matching files from filtered and sorted responses list
def getFileList(responses, searchText):
    searchTerms = []
    term = ""
    for char in searchText:
        if char == " ":
            searchTerms.append(term)
            term = ""
        else:
            term += char
    searchTerms.append(term)
    flist = []

    for response in responses:
        userName = response["username"]
        files = response["files"]
        for file in files:
            fileName = ""
            for char in file["filename"][::-1]:
                if char == "\\":
                    break
                else:
                    fileName += char
            fileName = fileName[::-1]

            if nameMatch(fileName, searchTerms):
                fileData = file
                fileData["username"] = userName
                fileData["name"] = fileName
                flist.append(fileData)
                break
    return flist
