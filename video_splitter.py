from moviepy.editor import VideoFileClip
import os
from tkinter import filedialog
import tkinter as tk

def seleccionar_video():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path

def recortar_pelicula(video_path, output_dir):
    video = VideoFileClip(video_path)
    clip_duration = 30
    total_clips = int(video.duration / clip_duration)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    for i in range(total_clips):
        start_time = i * clip_duration
        end_time = min((i + 1) * clip_duration, video.duration)
        clip = video.subclip(start_time, end_time)
        clip_path = os.path.join(output_dir, f"clip_{i+1}.mp4")
        clip.write_videofile(clip_path)
    video.close()

if __name__ == "__main__":
    video_path = seleccionar_video()
    if video_path:
        output_dir = "D:\\Desktop\\clips"
        recortar_pelicula(video_path, output_dir)
    else:
        print("No se seleccionó ningún video.")
