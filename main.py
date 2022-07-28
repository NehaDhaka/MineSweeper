from tkinter import *
from cell import Cell
import settings
import utilties

root = Tk()
# Override the settings of the window
root.configure(bg="black")
root.geometry(f"{settings.WIDTH}x{settings.HEIGHT}")
root.title("Minesweeper Game")
root.resizable(False, False)

top_frame = Frame(
    root,
    bg="black",
    width=1440,
    height=utilties.height_prct(25)
)
top_frame.place(x=0, y=0)
game_title = Label(
    top_frame,
    bg="black",
    fg="white",
    text="Minesweeper Game",
    font=('', 48)
)
game_title.place(
    x=utilties.width_prct(25),
    y=0

)
left_frame = Frame(
    root,
    bg="black",
    width=utilties.width_prct(25),
    height=utilties.height_prct(75),
)
left_frame.place(x=0, y=utilties.height_prct(25))

center_frame = Frame(
    root,
    bg="black",
    width=utilties.width_prct(75),
    height=utilties.height_prct(75)
)
center_frame.place(
    x=utilties.width_prct(25),
    y=utilties.height_prct(25)
)

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=x, row=y
        )

# Call the label from Cell class
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(x=0, y=0)
Cell.randomize_mines()

# Run the window
root.mainloop()
