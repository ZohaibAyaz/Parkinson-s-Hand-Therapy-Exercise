import cv2
from tkinter import*
from tkinter import messagebox
from PIL import Image, ImageTk
from HandTrackingModule1 import HandDetector
import math
from tkinter import filedialog
import numpy as np

Draw=False
def cal_angle(a,b,c):
    'This function is for calculating angle b/w two lines where a, b and c are points on lines and b is common point b/w two lines'
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)

    radians = np.arctan2(c[1]-b[1],c[0]-b[0]) - np.arctan2(a[1]-b[1],a[0]-b[0])
    ang = np.abs(radians*180.0/np.pi)

    if (ang > 180.0):
        return 360-ang
    else:
        return ang

win = Tk()
win.title("Parkinson's Hand Therapy Exercise")
wid=win.winfo_screenwidth()
hei=win.winfo_screenheight()
win.geometry("%dx%d" % (wid, hei))
frame_1 = Frame(win, width=wid, height=hei, bg="#B0C4DE").place(x=0, y=0)
cap = cv2.VideoCapture(0)

w = 500
h = 400
label1 = Label(frame_1, width=w, height=h)
label1.place(x=420, y=100)

def Live():
    global cap, detector
    cap = cv2.VideoCapture(0)
    detector = HandDetector(detectionCon=0.5, maxHands=2)

def RecordedVideo():
    global win, label1,cam, cap, wid, heit
    cap.release()
    win.filename = filedialog.askopenfilename(initialdir = "Users\HP\OneDrive\Desktop",  \
    title = "SelectRecordedVideos")
    if win.filename:
        cap = cv2.VideoCapture(win.filename)
        label1.place(x=420, y=100)
        wid = 236
        heit = 400
        print(",,,",win.filename)
    else:
        cap = cv2.VideoCapture(0)
        label1.configure(width = 210, height= 100)
        label1.place(x=420, y=100)
        wid = 140
        heit = 80
    global cam,_
    _, img = cam.read()
    img = cv2.resize(img, (wid, heit))
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    rgb =cv2.flip(rgb, 1)
    image =Image.fromarray(rgb)
    finalImage = ImageTk.PhotoImage(image)
    label1.configure(image=finalImage)
    label1.image = finalImage
    select_img()

def Ex1():
    messagebox.showinfo('Hands Up Down Exercise',f'Stretch your hands such that your palms and fingers facing away from you and\
then release them such that your fingers and palms facing towards you(Hands Up down).\
Make sure both hands keep the same timing and size of movement.')

def Ex2():
    messagebox.showinfo('Hand Flapping Exercise',f'Create a tight fist then stretch your fingers and palms out(Hand Flapping).\
Make sure both hands keep the same timing and size of movement.')
def Ex3():
   messagebox.showinfo('Tip to Tip Exercise',f'On both hands, touch the tip of each finger to the tip of the thumb(Tip_to_Tip).\
Repeat this movement and slowly get faster.Make sure both hands keep the same timing and size of movement.')
def Ex4():
    messagebox.showinfo('Rotate Hands Exercise',f'Stretch your hands such that your palm and fingers of right hand facing\
towards palm and fingers of left hand and then rotate them about arm axis such that back side\
of palm and fingers of one hand face the back side of other(Rotate Hands).\
Make sure both hands keep the same timing and size of movement. ')
def Ex5():
    messagebox.showinfo('Snake Gesture Exercise',f'Make all the fingers of one hand perpendicular to its palm, do the same for second hand.\
This position will look like two snakes facing each other. Once you this positon is achieved,\
release your fingers such that both hands nice and straight facing each other(Snake Gesture).\
Make sure both hands keep the same timing and size of movement.')

def select_img():
    global cap, detector
    success, img = cap.read()
    if(success==False):
        cap = cv2.VideoCapture(0)
        select_img()
    img=cv2.flip(img, 1)
    # imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    hands, img = detector.findHands(img,flipType=False) 
    
    img = cv2.resize(img, (w, h))
    if hands:
        hand1 = hands[0]
        lmList1 = hand1["lmList"]  # List of 21 Landmark points
        x00,y00 = lmList1[0][1], lmList1[0][2]
        x11, y11 = lmList1[4][1], lmList1[4][2]
        x12, y12 = lmList1[3][1], lmList1[3][2]
        x13, y13 = lmList1[2][1], lmList1[2][2]
        x14, y14 = lmList1[1][1], lmList1[1][2]

        x21, y21 = lmList1[8][1], lmList1[8][2]
        x22, y22 = lmList1[7][1], lmList1[7][2]
        x23, y23 = lmList1[6][1], lmList1[6][2]
        x24, y24 = lmList1[5][1], lmList1[5][2]

        x31, y31 = lmList1[12][1], lmList1[12][2]
        x32, y32 = lmList1[11][1], lmList1[11][2]
        x33, y33 = lmList1[10][1], lmList1[10][2]
        x34, y34 = lmList1[9][1], lmList1[9][2]

        x41, y41 = lmList1[16][1], lmList1[16][2]
        x42, y42 = lmList1[15][1], lmList1[15][2]
        x43, y43 = lmList1[14][1], lmList1[14][2]
        x44, y44 = lmList1[13][1], lmList1[13][2]

        x51, y51 = lmList1[20][1], lmList1[20][2]
        x52, y52 = lmList1[19][1], lmList1[19][2]
        x53, y53 = lmList1[18][1], lmList1[18][2]
        x54, y54 = lmList1[17][1], lmList1[17][2]

        length11 = math.hypot(x21-x11, y21-y11) # calculating the length of the line which joins landmark 4 and landmark 8:
        length21 = math.hypot(x31-x11, y31-y11) # calculating the length of the line which joins landmark 4 and landmark 12:
        length31 = math.hypot(x41-x11, y41-y11) # calculating the length of the line which joins landmark 4 and landmark 16:
        length41= math.hypot(x51-x11, y51-y11) # calculating the length of the line which joins landmark 4 and landmark 20:

            #Exercise # 1 Tip to Tip
        if ((length11< 50) and ((y31 and y41 and y51) < (y11 and y21)) and ((cal_angle((x32,y32),(x33,y33),(x34,y34)) and cal_angle((x42,y42),(x43,y43),(x44,y44)) and cal_angle((x52,y52),(x53,y53),(x54,y54))) >170.0) and (cal_angle((x22,y22),(x23,y23),(x24,y24)) < 140.0)):
            cv2.putText(img, "Tip to Tip", (65, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        elif ((length21< 50) and ((y21 and y41 and y51) < (y11 and y31)) and ((cal_angle((x22,y22),(x23,y23),(x24,y24)) and cal_angle((x42,y42),(x43,y43),(x44,y44)) and cal_angle((x52,y52),(x53,y53),(x54,y54))) >170.0) and (cal_angle((x32,y32),(x33,y33),(x34,y34)) < 140.0)):
            cv2.putText(img, "Tip to Tip", (65, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        elif((length31< 50)and ((y21 and y31 and y51) < (y11 and y41)) and ((cal_angle((x32,y32),(x33,y33),(x34,y34)) and cal_angle((x22,y22),(x23,y23),(x24,y24)) and cal_angle((x52,y52),(x53,y53),(x54,y54))) >170.0) and (cal_angle((x42,y42),(x43,y43),(x44,y44)) < 140.0)):
            cv2.putText(img, "Tip to Tip", (65, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        elif ((length41< 50)and ((y21 and y31 and y41) < (y11 and y51)) and ((cal_angle((x32,y32),(x33,y33),(x34,y34)) and cal_angle((x22,y22),(x23,y23),(x24,y24)) and cal_angle((x42,y42),(x43,y43),(x44,y44))) >170.0) and (cal_angle((x52,y52),(x53,y53),(x54,y54)) < 140.0)):
            cv2.putText(img, "Tip to Tip", (65, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)         

            # Exercise # 2 Hands Flapping
        elif(cal_angle((x21,y21),(x22,y22),(x23,y23))<150):
            if (y21 > y24) and (y21 < y00):       #Index finger
                if (y31 > y34)and (y31 < y00):     #Middle finger
                    if (y41 > y44)and (y41 < y00):     #Ring finger                  
                        if (y51 > y54)and (y51 < y00):     #Little finger
                            # Exercise['Hands Flipping'] = True
                            cv2.putText(img, "Hand Flapping", (270, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            #Exercise # 3 Hands Down
        elif (y21 > y00):       #Index finger
            if(y31 > y00):     #Middle finger
                if (y41 > y00):     #Ring finger                  
                    if (y51 > y00):     #Little finger
                        # Exercise['Hands Up Down'] = True
                        cv2.putText(img, "Hands Up Down", (65, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            #Execise # 4 Rotate Hands about Arm Axis
        elif (y11 > y21):       #Index finger
            if(y21 > y31):     #Middle finger
                if (y31 > y41):     #Ring finger                  
                    if (y41 > y51):     #Little finger
                        # Exercise['Hands about arm axis'] = True
                        cv2.putText(img, "Rotate Hands", (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            #Exercise # 5 Snake Gesture        
        elif ((abs(y21 - y22) and abs(y23 - y24) and abs(y22 - y23)) < 10):       #Index finger
            if ((abs(y31 - y32) and abs(y33 - y34) and abs(y32 - y33)) < 10):     #Middle finger
                if ((abs(y41 - y42) and abs(y43 - y44) and abs(y42 - y43)) < 10):     #Ring finger                  
                    if ((abs(y51 - y52) and abs(y53 - y54) and abs(y52 - y54)) < 10):     #Little finger
                        cv2.putText(img, "Snake Gesture", (65, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
               
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(imgRGB)
    finalImage = ImageTk.PhotoImage(image)
    label1.configure(image=finalImage)
    label1.image = finalImage
    win.after(1, select_img)

detector = HandDetector(detectionCon=0.5, maxHands=2)
label2= Label(frame_1, text="Welcome to Parkinson's Hand Therapy Exercise", bg="#2C2F33",fg="white" ,font=('Times', '20', 'bold') ).place(x=390,y=40)
label7=Button(frame_1, text="1.Hands Up Down Exercise",borderwidth=10,fg="white",bg='#2C2F33', height=1, width=20, relief=RAISED, cursor="hand2", command=Ex1 ,font=('Times', '14', 'bold') ).place(x=60,y=160)
label8=Button(frame_1, text="2.Hands Flapping Exercise",borderwidth=10,fg="white", bg='#2C2F33', height=1, width=20, relief=RAISED, cursor="hand2", command=Ex2,font=('Times', '14', 'bold') ).place(x=60,y=220)
label9=Button(frame_1, text="3.Tip To Tip Exercise",borderwidth=10,fg="white",bg='#2C2F33', height=1, width=20, relief=RAISED, cursor="hand2", command=Ex3,font=('Times', '14', 'bold') ).place(x=60,y=280)
label10=Button(frame_1, text="4.Rotate Hands Exercise",borderwidth=10,fg="white", bg='#2C2F33', height=1, width=20, relief=RAISED, cursor="hand2", command=Ex4,font=('Times', '14', 'bold') ).place(x=60,y=340)
label11=Button(frame_1, text="5.Snake Gesture Exercise",borderwidth=10,fg="white",bg='#2C2F33',height=1, width=20, relief=RAISED, cursor="hand2", command=Ex5,font=('Times', '14', 'bold') ).place(x=60,y=400)
label4= Button(frame_1, text="Developed By :                      Hurraira Addrees (2021-MC-01)\
                                    Zohaib Ayaz (2021-MC-02)", fg="white",bg="#2C2F33", font=('Times', '15', 'bold')).place(x=252,y=615)
label12 = Message(win, justify = CENTER, font = ("Times", '17', 'bold' ), fg='white',bg = "#2C2F33", 
        text= "Department of Mechatronics & Control Engineering, University of Engineering and Technology, Lahore",\
        width = 1200,relief = RAISED)
label12.place(x = 200, y = 658)
b1 = Button(frame_1,text='Recorded Videos',borderwidth=10, height=1, width=20, relief=RAISED,fg="white",bg='#2C2F33', cursor="hand2", command=RecordedVideo)
b1.place(x=420, y=520)
b2 = Button(frame_1,text='Live Video',borderwidth=10, height=1, width=20, relief=RAISED,fg="white",bg='#2C2F33', cursor="hand2", command=Live)
b2.place(x=780, y=520)
b3 = Button(frame_1,text='Exit Program',borderwidth=10, height=1, width=20, relief=RAISED,fg="white",bg='#2C2F33', cursor="hand2", command=win.destroy)
b3.place(x=600, y=(560))

select_img()
win.mainloop()