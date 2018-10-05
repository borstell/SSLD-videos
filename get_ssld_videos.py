#!/usr/bin/env python3
import sys
import argparse
import urllib
from urllib import request
from urllib import parse
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


def get_ids_from_name(name, maxfinds):
    """Returns a list of IDs that match the search term 'name'. """
    base = "https://teckensprakslexikon.su.se/sok?{}"
    q = {"q": name}
    try:
        query = base.format(urllib.parse.urlencode(q))
        page = urllib.request.urlopen(query)
        soup = BeautifulSoup(page, 'html.parser')
        tb = soup.find('tbody')
        ids = tb.find_all("td", class_='id')
        spantexts = [i.find('span').text for i in ids]
        if len(ids) > maxfinds:
            return spantexts[:maxfinds]
        return spantexts
    except Exception as e:
        sys.exit(e)

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
