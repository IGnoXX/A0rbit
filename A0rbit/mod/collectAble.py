class BonusBox:

    def __init__(self, data, gui):
        
        self.boxID = int(data["boxID"])
        self.x = float(data["x"])
        self.y = float(data["y"])

        self.size = 2
        self.color = "yellow"

        
        self.gui = gui

        self.guiObj = self.gui.canvas.create_rectangle(
            (self.x/100 * self.gui.scale)-self.size, 
            (self.y/100 * self.gui.scale)-self.size, 
            (self.x/100 * self.gui.scale)+self.size, 
            (self.y/100 * self.gui.scale)+self.size, 
            fill=self.color
        )

        self.gui.bonusBoxes.append(self)

    def hide(self):
        self.gui.setColor(self.guiObj, "black")
    
    def show(self):
        self.gui.setColor(self.guiObj, self.color)
    
    def remove(self):
        self.gui.bonusBoxes.remove(self)
        self.hide()
    
