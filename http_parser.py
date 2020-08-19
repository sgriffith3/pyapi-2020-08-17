#!/usr/bin/env python3
"""
RZFeeser || Alta3 Research
Using regular expression to parse HTTPS responses
"""

import requests
import re

def main():
    while True:
        # prompt user for "url" and "searchFor"
        print(f"Welcome to the simple HTTP response parser. Where should we search (ex: https://alta3.com)?")
        url = input()
        if url == "q" or url == "quit":
            break
        print(f"Great! So we'll try to open this url {url} to search for the phrase:")
        searchFor = input()
    
        # send an HTTP GET to the "url", then strip off the attached HTML data
        searchMe = requests.get(url).text
    
        if re.search(searchFor, searchMe):
            print("Found a match!")
        else:
            print("No match!")
    
        matches = re.findall(searchFor, searchMe)
        print(f"There were {len(matches)} matches for {searchFor} in {url}")

if __name__ == "__main__":
    main()

