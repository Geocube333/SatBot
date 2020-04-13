# SatBot
An automatic instagram downloader.

SatBot is a bot that currently goes around instagram stealing content from specified accounts.

This repo isn't fully finished. Future additions include:

Auto Following
Auto Liking
Auto Posting
And more!

How to use:

1. Fill Sources.txt with a list of instagram accounts to take content from
2. Run UpdateSources.py
3. Run CleanSources.py
4. Run DownloadContent.py //DownloadContent.py can be run with a start from post argument. If the script happens to fail midway
                          through a download, you can run DownloadContent.py {Number of next post that should've been 
                          downloaded} to continue where you left off. (i.e)
                          
                          Page Downloaded 5
                          Page Downloaded 6
                          Error: DownloadContent Has Failed For Reason x (This is just sample output by the way)
                          //To finish the download proceed with
                          ./DownloadContent.py 7
                          //This must be done in a cmd/terminal
                          
5. Run DeleteDuplicates.py **NOTE: DeleteDuplicates is now functional.

Optional 6. Run Clean.py  //Clean.py will delete all extra files in the SatBot Directory. Clean.py can be run with argument -k
                          this will remove only the /tmp/ and /links/ directory.
                          
SatBot (v1.1)
