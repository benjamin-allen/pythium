# Pythium

Pythium is a small utility for a university chemistry class.
It calculates masses for inputted chemical formulas.

# Usage

Run `pythium.py` to pull up the main window. There is a 
periodic table of the elements, a text entry box, a calculate
button, and a result field.

Pythium can be used with both mouse and keyboard.

### Keyboard
The mass of a element is accessed by typing its symbol.
Capitalization doesn't matter, but spacing does. After each
symbol, type a space. For example, sodium chloride's mass can
be obtained by typing `Na Cl` in the text entry field, then
pressing enter. Additionally, `na cl` will also suffice.
Pressing `Enter` calculates the mass of the compound.

To enter subscripts, immediately after the symbol place a dot
and then enter the desired number for the subscript. For 
example, the formula for water is `H.2 O` or `h.2 o`.

Subscripts can be used for parenthesized areas as well. For
example, the formula for aluminum sulfate is `Al.2 (SO.4).3`.
Note that parenthesized areas must be followed by a `.` subscript

Leading coefficients can be specified by making the first value
of the an entry a number. Multiple entries can be summed by using
a `+` between them. For example, `2Fe.2 O.3 + 3C`.

###Mouse
Masses of elements can be added by clicking on the respective
cell. If the element clicked is the same as the previous, it will
be subscripted instead of appended. Pressing the hydrogen cell
twice will give `H.2`.


# Screenshot

![Pythium screenshot](./Screenshot.png?raw=true)