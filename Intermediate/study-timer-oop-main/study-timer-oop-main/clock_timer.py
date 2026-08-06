class ClockTimer:

    WORK_MIN = 25
    SHORT_BREAK_MIN = 5
    LONG_BREAK_MIN = 20

    WORK = "ESTUDO"
    SHORT_BREAK = "PAUSA"
    LONG_BREAK = "PAUSA LONGA"

    def __init__(self):
        self.durations = {
            self.WORK: max(1, int(self.WORK_MIN * 60)),
            self.SHORT_BREAK: max(1, int(self.SHORT_BREAK_MIN * 60)),
            self.LONG_BREAK: max(1, int(self.LONG_BREAK_MIN * 60)),
        }

        self.phase = self.WORK
        self.total_seconds = self.durations[self.phase]
        self.remaining_seconds = self.total_seconds
        self.running = False

    @property
    def progress(self):
        if not self.total_seconds:
            return 0
        return self.remaining_seconds / self.total_seconds

    def start(self):
        self.running = True

    def pause(self):
        self.running = False

    def reset(self):
        self.running = False
        self.phase = self.WORK
        self._load_phase()

    def tick(self):
        """Subtracts one second. Returns True when the phase ends."""
        if not self.running:
            return False
        if self.remaining_seconds > 0:
            self.remaining_seconds -= 1
        return self.remaining_seconds == 0

    def advance_phase(self, completed_sessions):
        self.running = False
        if self.phase == self.WORK:
            self.phase = (
                self.LONG_BREAK if completed_sessions % 4 == 0
                else self.SHORT_BREAK
            )
        else:
            self.phase = self.WORK
        self._load_phase()

    def _load_phase(self):
        self.total_seconds = self.durations[self.phase]
        self.remaining_seconds = self.total_seconds

