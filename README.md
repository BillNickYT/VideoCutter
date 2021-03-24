# VideoCutter
This is little program that I made that cuts videos together.

Installation
-------
Just put the videos in a folder called "input" folder and songs in a folder called "audio" folder. The folders need to be in the same folder as the program. You will also need to add a file called "transition.mp4". This just plays everytime it cuts to the next video (no greenscreen function).

Config
-------
You can configure a few things in the lines 9-16 in "main.py".

 - **x**, **y** are the video sizes. Down below are different qualities.
 - **musicMultiplier** is the volume multiplier of the music.
 - **normalSoundMultiplier** is the volume multiplier of the videos.
 - **transitionSoundMultiplier** is the volume multiplier of the transitions.
 - **shuffleMusic**. If this is set to true, it chooses a random song to play and not the next song in the list.
 - **outputName** is the name for the output of the program.
 - **fps** is the amount of fps (frames per second) that the video will have.

Config
-------
Here are some qualities for the config file. The higher the quality, the higher the wait time for the program. I will list it like this: **width(x)** X **height(y)**.

 - **240p**: **352**x**240**
 - **360p**: **480**x**360**
 - **480p**: **858**x**480** - SD
 - **720p**: **1280**x**720** - HD
 - **1080p**: **1920**x**1080** - FullHD
 - **2160p**: **3860**x**2160** - UltraHD (4K)

Requirements
-------
All requirements are listed down below and in "requirements.txt". **Only ImageMagick is not listed because you need to download it from this [website](https://www.imagemagick.org/script/download.php)**. 

 - Moviepy (1.0.3)
 - Numpy (1.18.2)
