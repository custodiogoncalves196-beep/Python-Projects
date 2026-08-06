try:
    import winsound
except ImportError:
    winsound = None
from pathlib import Path

ALARM_PATH = Path(__file__).parent / "alarm.wav"


class ClockController:
    """Connects View events to Timer rules and Session data."""

    def __init__(self, root, timer, view, session):
        self.root = root
        self.timer = timer
        self.view = view
        self.session = session
        self.after_id = None
        view.bind_commands(self.start, self.pause, self.reset)
        self._refresh()

    def start(self):
        if self.timer.running:
            return
        self.timer.start()
        self.view.set_status("Em andamento")
        self.view.set_start_text("Em curso")
        self._schedule_tick()

    def pause(self):
        if not self.timer.running:
            return
        self.timer.pause()
        if self.after_id:
            self.root.after_cancel(self.after_id)
            self.after_id = None
        self.view.set_status("Em pausa", self.view.ORANGE)
        self.view.set_start_text("Continuar")

    def reset(self):
        self.pause()
        self.timer.reset()
        self.view.set_status("Pronto para estudar")
        self.view.set_start_text("Iniciar")
        self._refresh()

    def _schedule_tick(self):
        finished = self.timer.tick()
        self._refresh()
        if finished:
            self._finish_phase()
        elif self.timer.running:
            self.after_id = self.root.after(1000, self._schedule_tick)

    def _finish_phase(self):
        self.after_id = None

        objective, notes = self.view.get_session_data()
        self.session.objective = objective
        self.session.notes = notes

        if self.timer.phase == self.timer.WORK:
            self.session.complete()

        self.timer.advance_phase(self.session.completed)

        self._alarm()

        self.view.update_session(
            self.session,
            self.timer.durations[self.timer.WORK] // 60
        )
        self.view.set_status("Próxima fase pronta")
        self.view.set_start_text("Iniciar")
        self._refresh()

    def _refresh(self):
        self.view.update_timer(
            self.timer.remaining_seconds,
            self.timer.progress,
            self.timer.phase,
        )

    def _alarm(self):
        print(f"Alarme: {ALARM_PATH}")
        print(f"Existe: {ALARM_PATH.exists()}")

        try:
            winsound.PlaySound(
                str(ALARM_PATH.resolve()),
                winsound.SND_FILENAME
            )
        except RuntimeError as error:
            print(f"Erro ao tocar o alarme: {error}")
            self.root.bell()

