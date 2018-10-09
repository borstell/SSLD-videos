# SSLD-videos
Downloads videos from the [Swedish Sign Language dictionary](http://teckensprakslexikon.su.se).

Requires Python3 with package `bs4`.

Run the script from the command line with
```
./get_ssld_videos.py {search word(s)}
```

to search for the word in the SSLD and download hits.

The amount of search hits to download can be configured with `-n` or `--num-hits`:
```
./get_ssld_videos.py -n 4 anka räv
```

Searching for terms with spaces in them can be done by escaping the term in the shell:
```
./get_ssld_videos.py "dålig andedräkt" 10\ öre
```

Downloading one or more IDs from the SSLD can be done with the `-i` or `--ids` flag:
```
./get_ssld_videos.py -i 548 9943
```

Using the flag `-S` or `--short-names` will save the files using only the ID and file extension (e.g., 00001.mp4).
```
./get_ssld_videos.py -S Australien
```

## TODO
- [x] Implement searching for names of signs instead of having to provide ID
