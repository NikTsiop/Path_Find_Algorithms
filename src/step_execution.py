class StepTrack:
    def __init__(self, previous, current, next_step, track = 0) -> None:
        self.previous = previous
        self.current = current
        self.next = next_step
        self.track = track
        