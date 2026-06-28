class Integrator:
    """
    Integrator TIMDER-FLOW:
    Łączy:
    - rhythm (dict)
    - color (dict)
    - light (dict)
    - image (dict)
    - signal (dict)
    Zwraca jeden model strumienia.
    """

    def flow(self, rhythm: dict, color: dict,
             light: dict, image: dict, signal: dict) -> dict:
        return {
            "type": "TIMDER-FLOW",
            "rhythm": rhythm,
            "color": color,
            "light": light,
            "image": image,
            "signal": signal,
        }
