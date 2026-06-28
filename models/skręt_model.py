class SkretModel:
    """
    Model skrętu TIMDER:
    Prosty opis skrętu jako parametry do dalszego modelowania.
    """

    def __init__(self, intensity: float = 1.0, smoothness: float = 0.5):
        self.intensity = intensity
        self.smoothness = smoothness

    def as_dict(self) -> dict:
        return {
            "intensity": self.intensity,
            "smoothness": self.smoothness,
        }
