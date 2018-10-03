# SSLD-videos
Downloads videos from the Swedish Sign Language dictionary (http://teckensprakslexikon.su.se).

Requires Python3 with package `bs4`, and that Wget is installed.

Run the script from the command line with
```
python3 get_ssld_videos.py {signID}
```
or use the flag `--short` to rename to downloaded file to only ID number plus file extension (e.g., `00001.mp4`).
```
python3 get_ssld_videos.py {signID} --short
```
NB: `-s` works as a shorthand for `--short`.

SignIDs can be given in the full five-digit format (e.g., `00001`) or without zero-fillers (e.g., `1`).
Multiple signIDs can be entered at once, by separating them with a comma "," – for example:
```
python3 get_ssld_videos.py 00001,00002,00003
```
or
```
python3 get_ssld_videos.py 1,2,3
```
