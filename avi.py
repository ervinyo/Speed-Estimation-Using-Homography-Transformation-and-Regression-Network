import math
import numpy as np
import cv2
from termcolor import colored
import os
import time
# System call
os.system("")


CAMERA = [
    {
        'ID' : 1,           # First camera ID for RGB camera
        'WIDTH' : 640,
        'HEIGHT' : 480,
        'FPS' : 30
    },
    {
        'ID' : 0,
        'WIDTH' : 640,
        'HEIGHT' : 480,
        'FPS' : 30,
        'DEPTH' : True      # Depth camera should be True
    }
]

IMG_SHOW_MAX_WIDTH = 800

DATA_BASE_DIRECTORY = "data"
DATA_NEW_VIDEO_DIRECTORY = "new_video"

class colors:
    reset='\033[0m'
    bold='\033[01m'
    disable='\033[02m'
    underline='\033[04m'
    reverse='\033[07m'
    strikethrough='\033[09m'
    invisible='\033[08m'
    class fg:
        black='\033[30m'
        yellow ='\033[31m'
        green='\033[32m'
        orange='\033[33m'
        blue='\033[34m'
        purple='\033[35m'
        cyan='\033[36m'
        lightgrey='\033[37m'
        darkgrey='\033[90m'
        lightred='\033[91m'
        lightgreen='\033[92m'
        yellow='\033[93m'
        lightblue='\033[94m'
        pink='\033[95m'
        lightcyan='\033[96m'
    class bg:
        black='\033[40m'
        red='\033[41m'
        green='\033[42m'
        orange='\033[43m'
        blue='\033[44m'
        purple='\033[45m'
        cyan='\033[46m'
        lightgrey='\033[47m'

def getVideoProperties(video) :
    properties = {}
    properties['FPS'] = round(video.get(cv2.CAP_PROP_FPS))
    properties['Height'] = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    properties['Width'] = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    properties['Count'] = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

    return properties

def hhmmss(ms) :
    s = round(ms / 1000)
    m, s = divmod(s, 60)
    h, m = divmod(m, 60)
    return ("%d:%02d:%02d" % (h,m,s)) if h else ("%02d:%02d" % (m,s))

def distance2D(p1, p2) :
    distance = math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))
    return distance

def fixPoint(approx, flip = False) :
    if flip :
        approx = np.flip(approx, 0)
    tmp = approx.copy()

    tmp[0] = approx[3]
    tmp[1] = approx[0]
    tmp[2] = approx[1]
    tmp[3] = approx[2]

    return tmp

def isRectangle(approx, range = 20) :
    d_1 = math.sqrt(((approx[0][0][0] - approx[1][0][0]) ** 2) + ((approx[0][0][1] - approx[1][0][1]) ** 2))
    if d_1 < range :
        return False

    d_2 = math.sqrt(((approx[2][0][0] - approx[3][0][0]) ** 2) + ((approx[2][0][1] - approx[3][0][1]) ** 2))
    if d_2 < range :
        return False

    return True

def default(obj) :
    if type(obj).__module__ == np.__name__:
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return obj.item()
    raise TypeError('Unknown type:', type(obj))

percentTime = time.time()
def PrintPercent(c, t, descr = "", progressLength = 30, doRemainTime = True) :
    global percentTime
    progressText = ""
    percent = math.floor(c / t * 100)

    if c == 1 :
        percentTime = time.time()

    for i in range(progressLength) :
        progressText += colors.bg.green if i / progressLength < c / t else colors.bg.lightgrey
        progressText += " "

    progressText += "{} {}% ({:.0f}/{:.0f})".format(colors.reset, percent, c, t)
    progressText = descr + progressText

    if doRemainTime > 0 :
        progressText += " " + hhmmss((time.time() - percentTime) / c * (t - c) * 1000)

    print(progressText, end="\r" if  c < t else "\n")
