# This is a sample Python script.
import tkinter as tk
import subprocess
import os

from pytube import YouTube

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# https://youtu.be/mllJ49QIIVs
# https://youtu.be/zSRTjT7I0BA


def download():
    global E1
    s = E1.get()
    print('Link : ', s, str(s))
    if s != '':
        yt = YouTube(s)

        print('=' * 70)
        print('| Title    : ', yt.title)
        print('| Duration : ', yt.length)
        print('| Views    : ', yt.views)
        print('| Rating   : ', yt.rating)
        print('| Link     : ', str(s))
        print('=' * 70)

        videos = yt.streams

        i = 1
        button.pack_forget()
        for v in videos:
            try:
                fs = v.filesize
                re = v.resolution
                if fs and re:
                    print(str(i), '.', re, round(fs / (1024 * 1024), 2), 'MB')
                    if i < 6:
                        d_btn = tk.Button(text=str(i)+'.'+str(re) + str(round(fs / (1024 * 1024), 2)) + 'MB', fg="#000",
                                          bg="#0f0", bd="0", width=15, height=2,
                                          command=(lambda: save_video(videos, len(videos) - videos.index(v))))
                        d_btn.pack(side=tk.RIGHT)

                else:
                    print('Link not available')
            except Exception:
                print(str(i), '.', 'Link Unavailable')
            i += 1
        print('=' * 70)


def save_video(videos, number):
    for widget in root.winfo_children():
        widget.destroy()
    wait_msg = tk.Label(root, text='Please Wait', background="white", foreground="red", width=100, height=2)
    wait_msg.pack()
    print('Index', number)
    vid = videos[number-1]
    # dest = str(r'C:\Users\haPPy\Videos')
    dest = os.getcwd()
    vid.download(dest)
    # subprocess.Popen(dest)
    msg = tk.Label(root, text='The Video has been successfully downloaded', background="white",
                   foreground="green", width=100, height=2)
    # wait_msg.pack_forget()
    msg.pack()
    # quit()


if __name__ == '__main__':
    root = tk.Tk()

    w = tk.Label(root, text='Enter Video Link in Below Text Box', background="white", foreground="black", width=80,
                 height=1)
    w.pack()

    E1 = tk.Entry(root, bd=3, width=50)
    E1.pack(side=tk.LEFT)
    button = tk.Button(root, text="Download", fg="#000", command=(lambda: download()), bg="#3385ff", font="Arial",
                       bd="0", height=1)
    button.pack(side=tk.BOTTOM)
    root.mainloop()
