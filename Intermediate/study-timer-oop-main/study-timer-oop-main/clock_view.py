import tkinter as tk


class ClockView:
    """Creates the interface and exposes only the visual update methods."""

    BG = "#080d19"
    CARD = "#101726"
    INPUT = "#151d2d"
    TEXT = "#f4f6ff"
    MUTED = "#778199"
    BLUE = "#5974ff"
    GREEN = "#2ed6a1"
    ORANGE = "#ffb55e"

    def __init__(self, root):
        self.root = root
        root.title("Clock — Tempo de Estudo[Autor Custódio Gonçalves]")
        root.geometry("1050x650")
        root.configure(bg=self.BG)
        root.resizable(False, False)
        self._build()

    def _build(self):
        header = tk.Frame(self.root, bg=self.BG, height=55)
        header.pack(fill="x", padx=38, pady=(25, 8))
        header.pack_propagate(False)

        tk.Label(header, text="◷  Clock", bg=self.BG, fg=self.BLUE,
                 font=("Segoe UI", 10, "bold")).pack(side="left")

        title_frame = tk.Frame(header, bg=self.BG)
        title_frame.place(relx=0.5, y=0, anchor="n")

        tk.Label(title_frame, text="Tempo de Estudo", bg=self.BG, fg=self.TEXT,
                 font=("Segoe UI", 18, "bold")).pack()
        tk.Label(title_frame, text="Mantém o foco e alcança os teus objetivos! 💪",
                 bg=self.BG, fg=self.MUTED, font=("Segoe UI", 9)).pack()

        body = tk.Frame(self.root, bg=self.BG)
        body.pack(fill="both", expand=True, padx=38, pady=20)

        self._left_card(body)
        self._timer(body)
        self._right_card(body)
        self._notes_card(body)

    def _left_card(self, parent):
        card = self._card(parent, 0, 55, 215, 205)
        tk.Label(card, text="●  SESSÃO ATUAL", bg=self.CARD, fg=self.BLUE,
                 font=("Segoe UI", 9, "bold")).pack(anchor="w", padx=18, pady=(16, 12))
        self.session_label = tk.Label(card, text="Sessão 1 de 4", bg=self.CARD,
                                      fg=self.TEXT, font=("Segoe UI", 12, "bold"))
        self.session_label.pack(anchor="w", padx=18)
        self.objective_entry = tk.Entry(card, bg=self.INPUT, fg=self.TEXT,
                                        insertbackground=self.TEXT, relief="flat",
                                        font=("Segoe UI", 10))
        self.objective_entry.insert(0, "Objetivo desta sessão")
        self.objective_entry.pack(fill="x", padx=18, pady=14, ipady=7)
        self.studied_label = tk.Label(card, text="◉  Estudado hoje: 0 min",
                                      bg=self.CARD, fg=self.GREEN,
                                      font=("Segoe UI", 9, "bold"))
        self.studied_label.pack(anchor="w", padx=18)

    def _timer(self, parent):
        center = tk.Frame(parent, bg=self.BG, width=490, height=430)
        center.place(x=230, y=0)
        center.pack_propagate(False)
        self.canvas = tk.Canvas(center, width=330, height=330, bg=self.BG,
                                highlightthickness=0)
        self.canvas.pack()
        self.canvas.create_oval(35, 35, 295, 295, outline="#202a40", width=8)
        self.progress_arc = self.canvas.create_arc(
            35, 35, 295, 295, start=90, extent=-360,
            outline=self.BLUE, width=8, style="arc")
        self.canvas.create_text(165, 92, text="⏱", fill=self.BLUE,
                                font=("Segoe UI Symbol", 22))
        self.time_text = self.canvas.create_text(
            165, 155, text="25:00", fill=self.TEXT,
            font=("Consolas", 36, "bold"))
        self.phase_text = self.canvas.create_text(
            165, 196, text="ESTUDO", fill=self.MUTED,
            font=("Segoe UI", 10, "bold"))
        self.canvas.create_text(165, 220, text="Minutos  •  Segundos",
                                fill=self.MUTED, font=("Segoe UI", 8))

        controls = tk.Frame(center, bg=self.BG)
        controls.pack()
        self.reset_button = self._button(controls, "↻\nReiniciar", self.INPUT)
        self.start_button = self._button(controls, "▶\nIniciar", self.BLUE)
        self.pause_button = self._button(controls, "■\nPausar", self.INPUT)
        for button in (self.reset_button, self.start_button, self.pause_button):
            button.pack(side="left", padx=12)

    def _right_card(self, parent):
        card = self._card(parent, 730, 55, 245, 205)
        tk.Label(card, text="ESTADO", bg=self.CARD, fg=self.MUTED,
                 font=("Segoe UI", 9, "bold")).pack(anchor="w", padx=18, pady=(16, 10))
        self.status_label = tk.Label(card, text="●  Pronto para estudar",
                                     bg=self.CARD, fg=self.GREEN,
                                     font=("Segoe UI", 11, "bold"))
        self.status_label.pack(anchor="w", padx=18)
        self.completed_label = tk.Label(card, text="Sessões concluídas: 0",
                                        bg=self.CARD, fg=self.TEXT,
                                        font=("Segoe UI", 10))
        self.completed_label.pack(anchor="w", padx=18, pady=(18, 5))
        tk.Label(card, text="A cada 4 sessões: pausa longa", bg=self.CARD,
                 fg=self.MUTED, font=("Segoe UI", 9)).pack(anchor="w", padx=18)

    def _notes_card(self, parent):
        card = self._card(parent, 730, 280, 245, 175)
        tk.Label(card, text="NOTAS DA SESSÃO", bg=self.CARD, fg=self.BLUE,
                 font=("Segoe UI", 9, "bold")).pack(anchor="w", padx=18, pady=(14, 8))
        self.notes_text = tk.Text(card, height=5, bg=self.INPUT, fg=self.TEXT,
                                  insertbackground=self.TEXT, relief="flat",
                                  wrap="word", font=("Segoe UI", 9))
        self.notes_text.pack(fill="both", expand=True, padx=18, pady=(0, 16))

    def bind_commands(self, start, pause, reset):
        self.start_button.config(command=start)
        self.pause_button.config(command=pause)
        self.reset_button.config(command=reset)

    def update_timer(self, remaining, progress, phase):
        minutes, seconds = divmod(remaining, 60)
        self.canvas.itemconfig(self.time_text, text=f"{minutes:02d}:{seconds:02d}")
        self.canvas.itemconfig(self.phase_text, text=phase)
        self.canvas.itemconfig(self.progress_arc, extent=-360 * progress)

    def update_session(self, session, work_minutes):
        self.session_label.config(text=f"Sessão {session.current_number} de 4")
        self.completed_label.config(text=f"Sessões concluídas: {session.completed}")
        self.studied_label.config(text=f"◉  Estudado hoje: {session.completed * work_minutes} min")

    def set_status(self, text, color=None):
        self.status_label.config(text=f"●  {text}", fg=color or self.GREEN)

    def set_start_text(self, text):
        self.start_button.config(text=f"▶\n{text}")

    def get_session_data(self):
        return self.objective_entry.get().strip(), self.notes_text.get("1.0", "end-1c").strip()

    def _card(self, parent, x, y, width, height):
        card = tk.Frame(parent, bg=self.CARD, width=width, height=height)
        card.place(x=x, y=y)
        card.pack_propagate(False)
        return card

    def _button(self, parent, text, color):
        return tk.Button(parent, text=text, bg=color, fg=self.TEXT,
                         activebackground=self.BLUE, activeforeground=self.TEXT,
                         relief="flat", borderwidth=0, width=9, height=2,
                         cursor="hand2", font=("Segoe UI", 9, "bold"))

