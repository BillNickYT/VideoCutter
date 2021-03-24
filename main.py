import numpy as np
from moviepy.editor import *
from moviepy.audio.fx.all import *
from moviepy.video.tools.segmenting import findObjects
from os import walk
import random


x = 1920
y = 1080
musicMultiplier = 0.05
normalSoundMultiplier = 1.5
transitionSoundMultiplier = 2
shuffleMusic = False
outputName = "output.mp4"
fps = 60

_, _, filenames = next(walk("./input"))
filenamesWithFolder = []
for fN in filenames:
    filenamesWithFolder.append("input/" + fN)
print("Videos: " + str(filenamesWithFolder))
screenSize = (int(x), int(y))
clips = [VideoFileClip(n, audio=True) for n in filenamesWithFolder]
transition = VideoFileClip("transition.mp4", audio=True)

_, _, audioFilenames = next(walk("./audio"))
if shuffleMusic == True:
    random.shuffle(audioFilenames)
audioPaths = []
for fN in audioFilenames:
    audioPaths.append("audio/" + fN)
print("Audio: " + str(audioPaths))

audioClips = [AudioFileClip(n) for n in audioPaths]



txt_clips = []
current = 0
time = 0
timeList = []
for audio in audioFilenames:
    txt_clip = TextClip("Now Playing:  \n" + audio.replace(".mp3", "") + "  ", fontsize=45, color="white", method="pango", font="arial", size=screenSize)
    txt_clip = txt_clip.set_start(time)
    txt_clip = txt_clip.set_duration(5)
    txt_clip = txt_clip.set_pos(("right", "top"))
    txt_clips.append(txt_clip)
    print("Playing " + audio.replace(".mp3", "") + " at " + str(time))
    audioClips[current] = audioClips[current].set_start(time).fx(volumex, musicMultiplier)
    time = time + audioClips[current].duration
    timeList.append(time)
    current = current + 1
    
orderedVideoClips = []
m = len(clips)
c = 1
allLength = 0
for clip in clips:
    
    allLength = allLength + clip.duration
    print("Starting next clip in " + str(allLength - clip.duration) + ". It has " + str(clip.fps) + " FPS")
    if c == m:
        
        clip = clip.set_start(allLength - clip.duration)
        clip.audio = clip.audio.set_start(allLength - clip.duration).fx(volumex, normalSoundMultiplier)
        orderedVideoClips.append(clip)
    else:
        newTrans = VideoFileClip("transition.mp4", audio=True)
        clip = clip.set_start(allLength - clip.duration).fx(volumex, normalSoundMultiplier)
        clip.audio = clip.audio.set_start(allLength - clip.duration)
        newTrans = newTrans.set_start(allLength)
        newAudio = newTrans.audio
        newAudio = newAudio.set_start(allLength).fx(volumex, transitionSoundMultiplier)
        newTrans.audio = newAudio
        allLength = allLength + transition.duration
        orderedVideoClips.append(clip)
        orderedVideoClips.append(newTrans)
    c = c + 1

allAudio = []
for a in audioClips:
    allAudio.append(a)
for a in orderedVideoClips:
    allAudio.append(a.audio)
finalAudio = CompositeAudioClip(allAudio)

for a in txt_clips:
    orderedVideoClips.append(a)

allAudio = CompositeAudioClip(allAudio)
finalClip = CompositeVideoClip(orderedVideoClips)
finalClip = finalClip.set_audio(allAudio.set_duration(allLength))
finalClip = finalClip.set_duration(allLength)
finalClip = finalClip.resize(screenSize)
finalClip = finalClip.set_fps(fps)
finalClip.write_videofile(outputName)