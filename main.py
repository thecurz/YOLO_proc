import os 
import sys
import subprocess

if sys.version_info.major != 3 or sys.version_info.minor != 10:
    sys.exit("Este script necesita Python 3.10 para funcionar.")

print(sys.version_info)
if not os.path.isdir('yolov5'):
    subprocess.run(['git', 'clone', 'https://github.com/ultralytics/yolov5'], check=True)
subprocess.run(['pip', 'install', '-r', './yolov5/requirements.txt'], check=True)
subprocess.run(['pip', 'install', 'moviepy'], check=True)

from moviepy.editor import VideoFileClip

if not os.path.isfile('OUTPUT.mp4'):
    clip = VideoFileClip("INPUT.mp4")
    clip = clip.subclip(0, 120)
    clip = clip.set_duration(120).set_fps(24)
    clip.write_videofile("OUTPUT.mp4")

subprocess.run(['python3.10', './yolov5/detect.py', '--weights', 'yolov5s.pt', '--source', 'OUTPUT.mp4', '--view-img', '--classes', '0', '--save-txt'], check=True)