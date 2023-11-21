import os 
import sys
import subprocess
from pathlib import Path

if sys.version_info.major != 3 or sys.version_info.minor != 10:
    sys.exit("Este script necesita Python 3.10 para funcionar.")

print(sys.version_info)

# Si el directorio 'yolov5' no existe, clona el repositorio de GitHub
if not os.path.isdir('yolov5'):
    subprocess.run(['git', 'clone', 'https://github.com/ultralytics/yolov5'], check=True)
subprocess.run(['pip', 'install', '-r', './yolov5/requirements.txt'], check=True)
subprocess.run(['pip', 'install', 'moviepy'], check=True)

from moviepy.editor import VideoFileClip
import shutil

sys.path.append(str(Path('./yolov5').resolve()))
shutil.copy('./detect.py', './yolov5/detect.py')
from detect import run

if not os.path.isfile('OUTPUT.mp4'):
    clip = VideoFileClip("INPUT.mp4")
    clip = clip.subclip(0, 120)
    clip = clip.set_duration(120).set_fps(24)
    clip.write_videofile("OUTPUT.mp4")

weights = 'yolov5s.pt'
source = 'OUTPUT.mp4'
view_img = True
classes = [0]

run(weights=weights, source=source, view_img=view_img, classes=classes)