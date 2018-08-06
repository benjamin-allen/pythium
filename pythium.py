from tkinter import *
import re

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
        self.mass_str = ""

        for i in range(len(elementslist)):
            self.elements[elementslist[i].symbol] = elementslist[i]

        frame = Frame(master)
        frame.grid_rowconfigure(7, minsize=size//2*10)
        frame.grid_rowconfigure(10, minsize=size//2*10)
        frame.pack()

        for e in self.elements:
            button = Button(frame, height=size//2, width=size, text=e.capitalize(),
                            command=lambda arg=e: self.emplace(arg))
            button.config(relief=SOLID, overrelief=FLAT, bd=2)
            button.grid(row=self.elements[e].ypos, column=self.elements[e].xpos, padx=1, pady=1)

        frame2 = Frame(master)
        frame2.columnconfigure(0, weight=4)
        frame2.columnconfigure(1, weight=1)
        frame2.grid_rowconfigure(2, minsize=size//2*10)
        frame2.pack()
        self.entry = Entry(frame2, width=80)
        self.entry.grid(row=1, column=0, sticky=W+E)
        b = Button(frame2, text="Calculate mass!", command=self.read)
        b.grid(row=1, column=1)

    def emplace(self, element):
        if self.entry.get() == "" or (self.entry.get()[-1].isdigit() and self.entry.get()[-2] is " ") or self.entry.get()[-1] == " ":
            self.entry.insert(END, self.elements[element].symbol.capitalize())
        else:
            self.entry.insert(END, " " + self.elements[element].symbol.capitalize())

    def read(self):
        self.mass_str = self.entry.get().lower()
        molecule_list = []
        r = re.compile("\s*\+\s*")
        self.mass_str = re.sub(r, "+", self.mass_str)
        r = re.compile("\(.+\)\.[0-9]+")
        parenthesized_molecules = re.findall(r, self.mass_str)
        for p in parenthesized_molecules:
            p, mult = p.split(").")
            p = mult + p[1:]
            self.mass_str = re.sub(r, " + " + p, self.mass_str)
        for molecule in self.mass_str.split("+"):
            molecule_list.append(molecule)
        total_mass = 0.0
        for molecule in molecule_list:
            if molecule is "":
                continue
            m = {}
            molecule = molecule.strip()
            if molecule[0].isdigit():
                m["front_multiplier"] = int(molecule[0])
                while not molecule[0].isalpha():
                    molecule = molecule[1:]
            else:
                m["front_multiplier"] = 1
            molecule = molecule.split(" ")
            m["molecule_mass"] = 0
            for atom in molecule:
                a = ""
                mult = 1
                try:
                    a, mult = atom.strip().split(".")
                except ValueError:
                    a = atom.strip()
                finally:
                    mult = int(mult)
                if a.strip() is not "":
                    m["molecule_mass"] += (self.elements[a].mass * mult)
            total_mass += m["molecule_mass"] * m["front_multiplier"]
        print(total_mass)

root = Tk()
root.wm_title("Pythium")
pp = App(root)
root.mainloop()
