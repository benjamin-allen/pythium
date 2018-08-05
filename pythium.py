from tkinter import *

#CRITICAL VARS
readfile = "default.elements"
size = 4

def read_elements():
    elements = []
    with open(readfile, "r") as f:
        for line in f.readlines():
            e = Element()
            e.read(line)
            if e.verify_completeness():
                elements.append(e)
    return elements


class Element:
    def __init__(self):
        self.mass = 0
        self.number = 0
        self.long_name = ""
        self.symbol = ""
        self.xpos = -1
        self.ypos = -1

    def set_mass(self, v):
        self.mass = float(v)

    def set_number(self, v):
        self.number = int(v)

    def set_long_name(self, v):
        self.long_name = v

    def set_symbol(self, v):
        self.symbol = v

    def set_xpos(self, v):
        self.xpos = int(v)

    def set_ypos(self, v):
        self.ypos = int(v)

    def __str__(self):
        return "Name: " + self.long_name + "\n" +\
            "Number: " + str(self.number) + "\n" +\
            "Mass: " + str(self.mass) + "\n" +\
            "XPos: " + str(self.xpos) + "\n" +\
            "YPos: " + str(self.ypos)

    def __repr__(self):
        return self.__str__().replace("\n", ", ")

    dispatcher = {
        'mass': set_mass,
        'm': set_mass,
        'number': set_number,
        'n': set_number,
        'name': set_long_name,
        'symbol': set_symbol,
        's': set_symbol,
        'xpos': set_xpos,
        'x': set_xpos,
        'ypos': set_ypos,
        'y': set_ypos
    }

    def verify_completeness(self, check_pos=True):
        complete = True
        for v in [self.mass, self.number]:
            if v < 1:
                print("ERROR: Bad mass or number value for " + self.long_name + ".")
                complete = False
        for v in [self.long_name, self.symbol]:
            if v=="":
                print("ERROR: Missing symbol or long name value for element with number " + self.number + ".")
                complete = False
        if check_pos:
            for v in [self.xpos, self.ypos]:
                if v < 0:
                    print("ERROR: Bad position for " + self.long_name + ".")
                    complete = False
        return complete

    def read(self, inputstr):
        data = [i.split(":") for i in inputstr.lower().split(",")]
        for k,v in data:
            if k not in Element.dispatcher:
                print("ERROR: Unsupported name field \'" + k + "\'.")
            else:
                self.dispatcher[k](self, v)


class App:
    def __init__(self, master):
        elementslist = read_elements()
        self.elements = {}

        for i in range(len(elementslist)):
            self.elements[elementslist[i].symbol] = elementslist[i]

        frame = Frame(master)
        frame.grid_rowconfigure(7, minsize=size//2*10)
        frame.pack()

        for e in self.elements:
            button = Button(frame, height=size//2, width=size, text=e.capitalize(),
                            command=lambda arg=e: self.call(arg))
            button.config(relief=SOLID, overrelief=FLAT, bd=2)
            button.grid(row=self.elements[e].ypos, column=self.elements[e].xpos, padx=1, pady=1)

    def call(self, element):
        # TODO: Stuff with the called element
        print(element)

root = Tk()
root.wm_title("Pythium")
pp = App(root)
root.mainloop()
