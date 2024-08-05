import tkinter as tk
from tkinter import messagebox
from decisionwheel import SpinningWheelApp
from randompicker import randomChoicerReturnsAngle
root = tk.Tk()
root.title("Decision Form")
root.geometry("500x500")

#frames
frame1 = tk.Frame(root)
frame1.pack(pady=20)
frame2 = tk.Frame(root)
frame2.pack(pady=20)
frame3 = tk.Frame(root)
frame3.pack(pady=30)

labelChoice = tk.Label(frame1,text="Choice : ")
labelChoice.pack(side="left")

entryChoice = tk.Entry(frame1)
entryChoice.pack(side="left")

btnChoice = tk.Button(frame1,text="Add",command=lambda:add_to_listbox())
btnChoice.pack(side="left",padx=10)

listBoxChoice = tk.Listbox(frame2,selectmode=tk.SINGLE)
listBoxChoice.pack(side="left")

btnDeleteFromListBox = tk.Button(frame2,text="Delete",command=lambda:delete_from_listbox())
btnDeleteFromListBox.pack(side="top",padx=10)

btnTen = tk.Button(frame2,text="Add10",command=lambda:add_0_to_10())
btnTen.pack(side="top",padx=10)

btnSpinTheWheel = tk.Button(frame3,text="SPIN THE WHEEL",command=lambda:spin_the_wheel())
btnSpinTheWheel.pack(side="bottom")

def add_0_to_10():
    for i in range(10):
        listBoxChoice.insert(i,i)
    

def delete_from_listbox():
    selected_indis = listBoxChoice.curselection()
    if(selected_indis):
        selected_index = selected_indis[0]
        listBoxChoice.delete(selected_index)
        

def add_to_listbox():
    newChoice = entryChoice.get()
    if newChoice:
        listBoxChoice.insert(tk.END,newChoice)
        entryChoice.delete(0,tk.END)



def spin_the_wheel():
    if listBoxChoice.size() < 2:
        messagebox.showerror("Insufficient Data","Please add at least 2 options to spin the decision wheel")
    else:
        listBoxItems = listBoxChoice.get(0,tk.END)
        item_list = list(listBoxItems)
        stop_angle = randomChoicerReturnsAngle(len(item_list))
        root2 = tk.Tk()
        app2 = SpinningWheelApp(root2,item_list)
        app2.start_spinning(stop_angle)
        root2.mainloop()
        

def main():
    root.mainloop()



if __name__ == "__main__":
    main()
