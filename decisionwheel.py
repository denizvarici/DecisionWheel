import tkinter as tk
import math

#my libs
import  randompicker

class SpinningWheelApp:
    def __init__(self, root,item_list):
        self.root = root
        self.root.title("Dönen Çark")
        self.canvas = tk.Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack()
        self.item_list = item_list

        print(self.item_list)

        self.angle = 0
        self.num_segments = len(self.item_list)
        self.create_wheel()
        self.update_wheel()


        

    def create_wheel(self):
        self.canvas.delete("wheel")
        self.center_x = 200
        self.center_y = 200
        self.radius = 150
        self.segment_angle = 360 / self.num_segments

        for i in range(self.num_segments):
            start_angle = i * self.segment_angle + self.angle
            end_angle = (i + 1) * self.segment_angle + self.angle
            self.draw_segment(start_angle, end_angle)

    def draw_segment(self, start_angle, end_angle):
        # Segmenti daire olarak çiz
        self.canvas.create_arc(
            self.center_x - self.radius, self.center_y - self.radius,
            self.center_x + self.radius, self.center_y + self.radius,
            start=start_angle,
            extent=end_angle - start_angle,
            fill="lightblue", outline="black", tags="wheel"
        )

    def update_wheel(self):
        self.angle -= 5  # Çarkı döndürme miktarı
        self.create_wheel()
        self.root.after(50, self.update_wheel)

if __name__ == "__main__":
    root = tk.Tk()
    app = SpinningWheelApp(root)
    root.mainloop()
