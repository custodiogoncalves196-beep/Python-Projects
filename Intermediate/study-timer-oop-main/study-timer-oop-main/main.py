import tkinter as tk

from clock_controller import ClockController
from clock_timer import ClockTimer
from clock_view import ClockView
from session import Session


def main():
    root = tk.Tk()

    timer = ClockTimer()
    session = Session()
    view = ClockView(root)

    controller = ClockController(
        root=root,
        timer=timer,
        view=view,
        session=session
    )

    root.mainloop()


if __name__ == "__main__":
    main()