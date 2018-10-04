#!/usr/bin/env python3
import sys
import argparse
import urllib
from urllib import request
from bs4 import BeautifulSoup

"""
This script collects videos of signs in the Swedish Sign Language Dictionary
(teckensprakslexikon.su.se).
"""

def fetch_sign_video(id, long_name=True):
    """Fetches and saves the video for the sign with the provided id"""

    base = "https://teckensprakslexikon.su.se"
    infopage = base + '/ord/' + id
    try:
        page = urllib.request.urlopen(infopage)
        soup = BeautifulSoup(page, 'html.parser')
        videlem = soup.find(id='ts-headvideo')
        source = videlem.find('source')
        vidfile = source['src']

        if long_name:
            dst = vidfile.split('/')[-1]
        else:
            dst = "{}.mp4".format(id)

        urllib.request.urlretrieve(base + vidfile, dst)
        print("Wrote {}".format(dst))
    except Exception as e:
        sys.exit(e)

def get_videos(ids, long_name):
    """Iterates through list ids and fetches each element after padding if necessary."""
    for id in ids:
        if len(id) < 5:
            id = id.zfill(5)
        fetch_sign_video(id, long_name)

def main():
	try:
		nums = sys.argv[1].split(",")
		get_videos(nums)
	except:
		print('Error! The correct input is "python3 get_ssld_videos.py {signIDs,separated,by,commas}"')

if __name__=="__main__":
	main()
