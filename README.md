# SSLD-videos
Downloads videos from the [Swedish Sign Language dictionary](http://teckensprakslexikon.su.se).

Requires Python3 with package `bs4`.

Run the script from the command line with
```
./get_ssld_videos.py {signID}
```
or use the flag `--short-names` (`-S`) to rename to downloaded file to only ID number plus file extension (e.g., `00001.mp4`).
```
./get_ssld_videos.py {signID} --short
```
NB: `-S` works as a shorthand for `--short`.

SignIDs can be given in the full five-digit format (e.g., `00001`) or without zero-fillers (e.g., `1`).
Multiple signIDs can be entered at once, and both input formats can be mixed:
```
./get_ssld_videos.py 00001 2 00003
```

## TODO
- [ ] Implement searching for names of signs instead of having to provide ID
