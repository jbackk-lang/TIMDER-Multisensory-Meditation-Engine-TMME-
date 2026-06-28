class RhythmEngine:
    """
    Silnik rytmu TIMDER:
    - bpm: tempo (np. 60)
    - pattern: nazwa wzorca (np. 'skręt', 'relax', 'pulse')
    Zwraca prostą strukturę rytmiczną do dalszego modelowania.
    """

    def generate(self, bpm: int = 60, pattern: str = "skręt") -> dict:
        return {
            "type": "rhythm",
            "bpm": bpm,
            "pattern": pattern,
            "steps": [
                {"time": 0.0, "intensity": 0.3},
                {"time": 0.5, "intensity": 0.5},
                {"time": 1.0, "intensity": 0.7},
            ],
        }
