import sys,os,re,urllib.request
from bs4 import BeautifulSoup

"""
This script collects videos of signs in the Swedish Sign Language Dictionary (teckensprakslexikon.su.se).
"""

def get_sign(num):
	# Collects the video of a sign based on the ID number from the dictionary as input
	top_url = "http://teckensprakslexikon.su.se"
	try:
		url = top_url+"/ord/"+num    #current
		html = urllib.request.urlopen(url)
		soup = BeautifulSoup(html,"html.parser")
		vid = re.findall(r'file: "(.*tecken.mp4)',soup.text)
		vid_url = top_url+vid[0]
		vidname = vid_url.split("/")[-1]
		wget1 = "wget -c -O "+vidname+" "+vid_url
		os.system(wget1)
	except:
		print("Error! Sign not found!")

def get_videos(all_nums):
	# Iterates over the inputted IDs and downloads the sign videos
	for num in all_nums:
		if len(num) < 5:
			num = num.zfill(5)
		get_sign(num)

def main():
	try:
		nums = sys.argv[1].split(",")
		get_videos(nums)
	except:
		print('Error! The correct input is "python3 get_ssld_videos.py {signIDs,separated,by,commas}"')

if __name__=="__main__":
	main()
