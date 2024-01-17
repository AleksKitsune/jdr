class Player():
    def __init__(self, root, name, x, y):
        self.name = name
        self.speed = 1
        self.x = x
        self.y = y
        self.root = root

    def draw(self):
        self.circle = self.root.can.create_oval(self.x, self.y, self.x+20, self.y+20, fill = "green")
        self.text = self.root.can.create_text(self.x +10, self.y +10, text = self.name[0])

    def move_right(self, event=None):

        self.root.can.move(self.circle, 1, 0)
        self.root.can.move(self.text, 1, 0)
        self.x += 1
    
    def move_left(self, event=None):

        self.root.can.move(self.circle, -1, 0)
        self.root.can.move(self.text, -1, 0)
        self.x -= 1

    def move_up(self, event=None):

        self.root.can.move(self.circle, 0, -1)
        self.root.can.move(self.text, 0, -1)
        self.y -= 1

    def move_down(self, event=None):

        self.root.can.move(self.circle, 0, 1)
        self.root.can.move(self.text, 0, 1)
        self.y += 1

