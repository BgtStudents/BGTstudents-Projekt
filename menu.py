import tkinter as tk
from PIL import Image, ImageTk
import os
import mediapipe as mp
import cv2
import numpy as np
from mediapipe.framework.formats import landmark_pb2
import time
import random
import argparse



def makinaV2():
    #XML (ALGORITHMA)
    kerretxml = cv2.CascadeClassifier("XMLFiles/module_per_makina.xml")


    #DETEKTIMI 
    def detect(frame):
        kerri = kerretxml.detectMultiScale(frame, 1.15, 4)

        for (x, y, w, h) in kerri:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), thickness = 2)
            cv2.putText(frame, "Makine e Detektuar!", (x+w, y+h), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), thickness = 1)

        return frame

    #KAMERA DHE DISPLAY
    def kamera():
        video_kamera = cv2.VideoCapture(0)

        while video_kamera.isOpened():
            ret, frame = video_kamera.read()
            butoni = cv2.waitKey(1)

            if ret :
                makina_xy = detect(frame)
                cv2.imshow("Detektion per Makina", makina_xy)

            else :
                break

            if butoni == ord('q'):
                break
            
        video_kamera.release()
        cv2.destroyAllWindows()

    kamera()



def MakinaV1():

    kerret_detection = cv2.CascadeClassifier("XMLFiles/module_per_makina.xml")

    video = cv2.VideoCapture("kerret.mp4")

    while video.isOpened():
        ret, img = video.read()
        e_hint = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        kerret = kerret_detection.detectMultiScale(e_hint, 1.3, 2)

        for (x,y,w,h) in kerret:
            cv2.rectangle(img,(x, y), (x+w+5, y+h+5), (0, 255, 0),3) 

        cv2.imshow("Detector per Makina", img)   
        
        if cv2.waitKey(10) & 0xFF == ord('q'):
                break
        
    video.release()
    cv2.destroyAllWindows()

def StopSign_Detection():

    # Stop Sign Cascade Classifier xml
    stop_sign = cv2.CascadeClassifier('XMLFiles/cascade_stop_sign.xml')
    speed_sign = cv2.CascadeClassifier('XMLFiles/speed_limit_sign_haar.xml')

    capture_video = cv2.VideoCapture(0)

    while capture_video.isOpened():
        _, img = capture_video.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        stop_sign_scaled = stop_sign.detectMultiScale(gray, 1.3, 5)
        speed_sign_scaled = speed_sign.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in stop_sign_scaled:
        
            stop_sign_rectangle = cv2.rectangle(img, (x,y),
                                                (x+w, y+h),
                                                (0, 255, 0), 3)

            stop_sign_text = cv2.putText(img=stop_sign_rectangle,
                                         text="Stop Sign",
                                         org=(x, y+h+30),
                                         fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                         fontScale=1, color=(0, 0, 255),
                                         thickness=2, lineType=cv2.LINE_4)

        for (x, y, w, h) in speed_sign_scaled:

            speed_sign_rectangle = cv2.rectangle(img, (x,y),
                                                 (x+w, y+h),
                                                 (0,255,0), 3)

            speed_sign_text = cv2.putText(img=speed_sign_rectangle,
                                          text='Speed Sign',
                                          org=(x, y+h+30),
                                          fontFace = cv2.FONT_HERSHEY_SIMPLEX,
                                          fontScale = 1, color=(0,0,255),
                                          thickness=2, lineType=cv2.LINE_4)

        cv2.imshow("img", img)
        key = cv2.waitKey(30)
        if key == ord('q'):
            capture_video.release()
            cv2.destroyAllWindows()
            break


def Bodyscanner():
        
    os.system('py openpose.py')


def run_script1():
    MakinaV1()

def run_script1_5():
    makinaV2()

def run_script2():
    os.system("py hand_detection.py")

def run_script3():
    StopSign_Detection()

def quit_program(event=None):
    root.quit()
    

root = tk.Tk()
root.geometry("1366x768")
root.title("BGT PROJECT")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()



bg_image = Image.open("Images/background2.png")
bg_image = bg_image.resize((screen_width - 20, screen_height - 20), Image.ANTIALIAS)
bg_image = ImageTk.PhotoImage(bg_image)

#bg_image = ImageTk.PhotoImage(Image.open())

bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

title_font = ("Helvetica", 21, "bold")
button_font = ("Helvetica", 14, "bold")

title_frame = tk.Frame(root)
title_frame.pack(pady=30)


title_label = tk.Label(title_frame, text="Mire se erdhet ne projektin e shkolles BGT!", font=title_font, bg='#14bbeb', fg='white')
title_label.pack()


description_label = tk.Label(root, text="Ne kete projekt ne kemi paraqitur se si teknologjia mund te na ndikoj dhe ndihmoj neve ne jeten tone te perditshme\nKeto programe qe ne kemi bere do te kene impakt te madh ne jeten tone te perditshme.\nTe gjitha keto programe dhe kodi jane te punuara nga 3 nxenes ne shkollen BGT.\nErdajt Sopjani, Idriz Mirena, Lum Vokshi.\nPer te provuar keto programe fillimisht shtypni butonet me poshte:", font=("Times New Roman", 13, "bold"), justify='center', bg='#14bbeb', fg='white')
description_label.pack(pady=20)


script1_button = tk.Button(root, text="Detektimi i Makinave", command=run_script1, font=button_font, width=30, height=2, bd=3, bg="#2196F3", fg="white")
script1_button.pack(side="top", padx=10, pady=10)

script1_button = tk.Button(root, text="Detektimi i Makinave(Kamere)", command=run_script1_5, font=button_font, width=30, height=2, bd=3, bg="#2196F3", fg="white")
script1_button.pack(side="top", padx=10, pady=10)

script2_button = tk.Button(root, text="Detektimi i Duarve(Loja)", command=run_script2, font=button_font, width=30, height=2, bd=3, bg="#4CAF50", fg="white")
script2_button.pack(side="top", padx=10, pady=10)


script3_button = tk.Button(root, text="Detektimi i shenjave rrugore", command=run_script3, font=button_font, width=30, height=2, bd=3, bg="#FF5722", fg="white")
script3_button.pack(side="top", padx=10, pady=10)

script4_button = tk.Button(root, text = 'Detektimi i Trupit', command = Bodyscanner, font= button_font, width=30, height=2, bd=3, bg='red', fg='white')
script4_button.pack(side='top', padx=10, pady=10)

root.bind("q", quit_program)
root.mainloop()
