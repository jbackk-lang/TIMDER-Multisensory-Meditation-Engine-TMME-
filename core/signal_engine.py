class SignalEngine:
    """
    Silnik sygnału TIMDER:
    - hz: częstotliwość impulsu (np. 1.0)
    Zwraca prosty model impulsów J-klucza.
    """

    def pulse(self, hz: float = 1.0) -> dict:
        return {
            "type": "signal",
            "hz": hz,
            "pattern": "pulse",
            "pulses": [
                {"t": 0.0, "value": 1.0},
                {"t": 1.0 / hz, "value": 1.0},
                {"t": 2.0 / hz, "value": 1.0},
            ],
        }
