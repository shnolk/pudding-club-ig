# pudding-club-ig
The source code for pudding club's instabot: @pudding_club_

Notable libraries used:  
instabot [https://pypi.org/project/instabot/]  
bing image downloader [https://pypi.org/project/bing-image-downloader/]  
Pillow [https://pypi.org/project/Pillow/]  

Needs per Machine:  
-updated hardware.dat file with hardware name  
-filled out PostOnIg_TEMPLATE.py, then rename as PostOnIg.py  
-crontab configuration (pull upstream master, post, file management[deletion])


Log:  
<i>
23-7-20: Set banana to post 20 minutes past every 4 hours and delete all local files at 20:00 (8:00 PM EST) on sundays.   
23-7-20: Ported to banana.  
22-7-20: Added dithering & other image processing tweaks.  
21-7-20: Added submittable objects with generative captions.
  </i>
