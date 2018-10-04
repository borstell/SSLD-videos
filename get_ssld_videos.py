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
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Download videos from SSLD.')
    # Take one or more ids to fetch.
    parser.add_argument('ids', nargs='+', help='ID(s) to download.')
    # Provides the option -S to save using short (ID only) names.
    parser.add_argument('-S', '--short-names', dest='long_name', action='store_false',
                        help='Store using id-only (00001.mp4) names?')
    # Parse arguments
    args = parser.parse_args()
    get_videos(args.ids, args.long_name)

if __name__ == "__main__":
    main()
