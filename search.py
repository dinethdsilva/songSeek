from config import SLSKD_URL, HEADERS
import requests
import time


def getSearchResults(searchText):
    # Starting search
    payload = {"searchText": searchText}
    startSearch = requests.post(
        f"{SLSKD_URL}/api/v0/searches", headers=HEADERS, json=payload
    )
    if startSearch.status_code not in (200, 201):
        print(f"Failed to initiate search request. Status: {startSearch.status_code}")
        print(startSearch.text)
        return []
    print("Search request was successfull and searching started!")

    # Checking search status
    searchId = startSearch.json()["id"]
    t = 0
    time.sleep(1)
    t += 1
    print(f"Waiting for search results... {t}s", end="\r", flush=True)
    searchStatus = requests.get(
        f"{SLSKD_URL}/api/v0/searches/{searchId}/", headers=HEADERS
    )
    if searchStatus.status_code not in (200, 201):
        print(f"Failed to get search status. Status: {searchStatus.status_code}")
        print(searchStatus.text)
        return []
    while searchStatus.json()["isComplete"] == False:
        time.sleep(1)
        t += 1
        print(f"Waiting for search results... {t}s", end="\r", flush=True)
        searchStatus = requests.get(
            f"{SLSKD_URL}/api/v0/searches/{searchId}/", headers=HEADERS
        )
        if searchStatus.status_code not in (200, 201):
            print(f"Failed to get search status. Status: {searchStatus.status_code}")
            print(searchStatus.text)
            return []
    print("\n", end="")

    # Obtaining results
    time.sleep(1)
    searchResults = requests.get(
        f"{SLSKD_URL}/api/v0/searches/{searchId}/responses/", headers=HEADERS
    )
    if searchResults.status_code not in (200, 201):
        print(f"Failed to get search results. Status: {searchResults.status_code}")
        print(searchResults.text)
        return []
    results = searchResults.json()
    print(f"{len(results)} search results found!")
    return results
