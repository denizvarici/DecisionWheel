import tkinter as tk
import math
import time
#my libs
import  randompicker

class SpinningWheelApp:
    def __init__(self, root,item_list,picked_index):
        self.root = root
        self.root.title("Spinning Wheel")

        self.main_frame = tk.Frame(root)
        self.main_frame.pack(fill=tk.BOTH,expand=True)

        self.canvas = tk.Canvas(self.main_frame, width=400, height=400, bg="white")
        self.canvas.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        self.arrowLabel = tk.Label(self.main_frame,text="<" + 10*"-")
        self.arrowLabel.pack(side=tk.RIGHT,padx=10,pady=0)
        self.item_list = item_list

        print(self.item_list)

        self.freespin_count = 4
        self.angle = 0
        self.num_segments = len(self.item_list)
        self.picked_index = picked_index
        self.speed = 20
        self.is_spinning = False
        self.stop_angle = None
        self.create_wheel()
        self.freespin_countdown()

    
    def freespin_countdown(self):
        if self.freespin_count > 0:
            self.freespin_count -= 1
            self.root.after(1000,self.freespin_countdown)

        

    def create_wheel(self):
        self.canvas.delete("wheel")
        self.center_x = 200
        self.center_y = 200
        self.radius = 150
        self.segment_angle = 360 / self.num_segments #4
        for i in range(self.num_segments):
            start_angle = i * self.segment_angle + self.angle    
            end_angle = (i + 1) * self.segment_angle + self.angle 
            text = self.item_list[i]
            self.draw_segment(start_angle, end_angle,text)

    def draw_segment(self, start_angle, end_angle, text):
        # draw sphere
        self.canvas.create_arc
        self.canvas.create_arc(
            self.center_x - self.radius, self.center_y - self.radius,
            self.center_x + self.radius, self.center_y + self.radius,
            start=start_angle,
            extent=end_angle - start_angle,
            fill="lightblue", outline="black", tags="wheel"
        )
        # insert text to slices
        mid_angle = (start_angle + end_angle) / 2
        rad = math.radians(mid_angle)
        text_x = self.center_x + (self.radius / 2) * math.cos(rad)
        text_y = self.center_y - (self.radius / 2) * math.sin(rad)
        self.canvas.create_text(text_x, text_y, text=text, tags="wheel")

    def update_wheel(self):
        if self.is_spinning:
            self.angle -= self.speed
            #extra if
            if self.freespin_count <= 0:
                if self.stop_angle is not None:
                    angle_diff = (self.stop_angle - self.angle) % 360
                    if angle_diff < self.speed:
                        self.angle = self.stop_angle
                        self.is_spinning = False
                        self.speed = 0
                        self.arrowLabel.config(text="<"+10*"-"+" : " + str(self.item_list[self.picked_index]))
                    else:
                        self.speed = max(1,self.speed - 0.1)
        self.create_wheel()
        self.root.after(50, self.update_wheel)

    def start_spinning(self,stop_angle):
        self.stop_angle = stop_angle
        self.is_spinning = True
        self.update_wheel()

if __name__ == "__main__":
    root = tk.Tk()
    app = SpinningWheelApp(root)
    root.mainloop()
