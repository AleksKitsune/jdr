import tkinter as tk
import player
from PIL import Image, ImageTk
import time
import threading

class App(threading.Thread):

    def __init__(self, app, sec=None):
        threading.Thread.__init__(self)
        self.app=app
        self.sec = sec
        self.start()
        
    def callback(self):
        self.root.quit()

    def run(self):
        if self.sec == None:

            self.root=self.app()
        
        else:
            self.root = self.app(self.sec)
        self.root.protocol("WM_DELETE_WINDOW", self.callback)

        self.root.mainloop()

class Timer(tk.Tk):
    def __init__(self, sec):
        tk.Tk.__init__(self)
        self.title("Chronomètre")
        self.wm_attributes("-topmost", 1)
        self.min = int(sec/60)
        self.sec = sec - self.min*60
        self.label = tk.Label(self, text="", font=('Times New Roman', 40))
        self.label.pack()
        self.alive = True
        self.updateClock()

    def updateClock(self):
        zeroMin = ""
        zeroSec = ""
        if self.sec < 0:
            self.sec += 60
            self.min -= 1
        if self.min < 0:
            self.alive = False
            time.sleep(0.1)
            self.quit()
        if self.min < 10:
            zeroMin = 0
        if self.sec < 10:
            zeroSec = 0
        timer = f"{zeroMin}{self.min}:{zeroSec}{self.sec}"
        self.label.configure(text=timer)
        self.sec -= 1
        self.after(1000, self.updateClock)

class Map(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Carte gardes en chef")
        self.activateMove = False
        
    def create_image(self, image):
        self.wm_attributes("-topmost", 1)
        self.map = Image.open(image)
        self.photo = ImageTk.PhotoImage(self.map)

        self.can = tk.Canvas(self, width = self.map.size[0], height = self.map.size[1])
        self.img = self.can.create_image(0,0, anchor=tk.NW,image=self.photo)
        self.can.pack()

    def modify_image(self, image):
        self.map = Image.open(image)
        self.photo = ImageTk.PhotoImage(self.map)
        self.can.itemconfigure(self.img, image = self.photo)

    def create_players(self):
        self.aleks = player.Player(self, "Aleks", 345, 685)
        self.kitsune = player.Player(self, "Kitsune", 370, 685)
        self.aleks.draw()
        self.kitsune.draw()
        self.bind('<Left>', self.press_left)
        self.bind('<Right>', self.press_right)
        self.bind('<Down>', self.press_down)
        self.bind('<Up>', self.press_up)

    def press_left(self, event):
        if self.activateMove == True:
            self.kitsune.move_left()
            if self.aleks.y == self.kitsune.y:
                self.aleks.move_left()
            elif self.aleks.y < self.kitsune.y:
                self.aleks.move_down()
            elif self.aleks.y > self.kitsune.y:
                self.aleks.move_up()
            self.bathroom()

    def press_right(self, event):
        if self.activateMove == True:
            self.kitsune.move_right()
            if self.aleks.y == self.kitsune.y:
                self.aleks.move_right()
            elif self.aleks.y < self.kitsune.y:
                self.aleks.move_down()
            elif self.aleks.y > self.kitsune.y:
                self.aleks.move_up()
            self.bathroom()

    def press_down(self, event):
        if self.activateMove == True:
            self.kitsune.move_down()
            if self.aleks.x == self.kitsune.x:
                self.aleks.move_down()
            elif self.aleks.x < self.kitsune.x:
                self.aleks.move_right()
            elif self.aleks.x > self.kitsune.x:
                self.aleks.move_left()
            self.bathroom()

    def press_up(self, event):
        if self.activateMove == True:
            self.kitsune.move_up()
            if self.aleks.x == self.kitsune.x:
                self.aleks.move_up()
            elif self.aleks.x < self.kitsune.x:
                self.aleks.move_right()
            elif self.aleks.x > self.kitsune.x:
                self.aleks.move_left()
            self.bathroom()
    
    def bathroom(self):
        if self.kitsune.x >= 395 and self.kitsune.x <= 400:
            if self.kitsune.y >=476 and self.kitsune.y <=478:
                self.activateMove = False
                self.secret = "Vous avez résolu l'énigme au dos de la carte, devant vous se trouve un renfoncement aux dimensions de la carte. Vous mettez la carte à l'intérieur et quasi immédiatement un passage secret se révèle à vous\n"
                self.modify_image("images/MapBath.png")
