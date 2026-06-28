from core.rhythm_engine import RhythmEngine
from core.color_engine import ColorEngine
from core.light_engine import LightEngine
from core.image_engine import ImageEngine
from core.signal_engine import SignalEngine
from core.integrator import Integrator

def main():
    rhythm = RhythmEngine().generate(60, "skręt")
    color = ColorEngine().palette("Λ-relax")
    light = LightEngine().sequence("τ-soft")
    image = ImageEngine().fractal("ρ-smooth")
    signal = SignalEngine().pulse(1.0)

    flow = Integrator().flow(rhythm, color, light, image, signal)
    print(flow)

if __name__ == "__main__":
    main()
