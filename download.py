import sys
import time
from utils.conversions import *
from config import SLSKD_URL, HEADERS
import requests


def desplayDownload(downloadStatus):
    state = downloadStatus["state"]
    size = sizeMB(downloadStatus["size"])
    downloaded = sizeMB(downloadStatus["bytesTransferred"])
    percent = round(downloadStatus["percentComplete"])
    speed = sizeMB(downloadStatus["averageSpeed"])

    print(f"Download {state}")
    noBlocks = round(percent / 2)
    print("[\033[32m", end="")
    print("#" * noBlocks, end="")
    print(" " * (50 - noBlocks), end="")
    print(f"\033[0m] \033[34m{percent}%\033[0m")
    print(f"\033[33m{downloaded}\033[0m/{size} MB   \033[31m{speed} MBps\033[0m")


def downloadFile(file):
    payload = [
        {
            "filename": file["filename"],
            "size": file["size"],
        }
    ]
    startDownload = requests.post(
        f"{SLSKD_URL}/api/v1/transfers/downloads/{file["username"]}/",
        json=payload,
        headers=HEADERS,
    )
    if startDownload.status_code not in (200, 201):
        print(
            f"Failed to initiate download request. Status: {startDownload.status_code}"
        )
        print(startDownload.text)
        return ""

    id = startDownload.json()["enqueued"][0]["id"]

    downloadState = requests.get(
        f"{SLSKD_URL}/api/v1/transfers/downloads/Blinkacre/{id}/",
        headers=HEADERS,
    )
    if downloadState.status_code not in (200, 201):
        print(f"Failed to obtain download status. Status: {downloadState.status_code}")
        print(downloadState.text)
        return ""

    desplayDownload(downloadState.json())
    time.sleep(1)

    while True:
        sys.stdout.write("\033[F\033[K" * 3)
        sys.stdout.flush()

        downloadState = requests.get(
            f"{SLSKD_URL}/api/v1/transfers/downloads/Blinkacre/{id}/",
            headers=HEADERS,
        )
        if downloadState.status_code not in (200, 201):
            print(
                f"Failed to obtain download status. Status: {downloadState.status_code}"
            )
            print(downloadState.text)
            return ""

        desplayDownload(downloadState.json())

        if "Completed" in downloadState.json()["state"]:
            break

        time.sleep(1)

    return downloadState.json()["state"]
