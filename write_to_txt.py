from tkinter import *
from tkinter import ttk

def write_file_neutral():
  f = open("output.txt", "a")
  f.write("neutral")
  f.write("\n")
  f.close()

def write_file_blink():
  f = open("output.txt", "a")
  f.write("blink")
  f.write("\n")
  f.close()

def write_file_look_l():
  f = open("output.txt", "a")
  f.write("lookL")
  f.write("\n")
  f.close()

def write_file_look_r():
  f = open("output.txt", "a")
  f.write("lookR")
  f.write("\n")
  f.close()

def write_file_wink_l():
  f = open("output.txt", "a")
  f.write("winkL")
  f.write("\n")
  f.close()
def write_file_wink_r():
  f = open("output.txt", "a")
  f.write("winkR")
  f.write("\n")
  f.close()

def main():
	root = Tk()
	root.title('testing')
	frm = ttk.Frame(root, padding=10)
	frm.grid()
	translations = PhotoImage(file='translations.png')
	translations = translations.zoom(10) 
	translations = translations.subsample(30)
	ttk.Button(frm, text="winkL", width=10, command=write_file_wink_l).grid(column=0, row=0)
	ttk.Button(frm, text="winkR", width=10, command=write_file_wink_r).grid(column=0, row=1)
	ttk.Button(frm, text="lookL", width=10, command=write_file_look_l).grid(column=1, row=0)
	ttk.Button(frm, text="neutral", width=10, command=write_file_neutral).grid(column=2, row=0)
	ttk.Button(frm, text="lookR", width=10, command=write_file_look_r).grid(column=1, row=1)
	ttk.Button(frm, text="quit", width=10, command=root.destroy).grid(column=2, row=1)
	ttk.Label(frm, text="Wink Left = dot (.) \nWink Right = dash (-) \nLook Left = new letter \nLook Right = new word").grid(column=0, row=3)

	ttk.Label(frm, image=translations).grid(column=3, row=0)
	root.mainloop()
if __name__ == '__main__': main()
