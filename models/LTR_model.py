class LTRModel:
    """
    Model warstw Λ–τ–ρ.
    """

    def __init__(self, lambda_state: str = "stable",
                 tau_state: str = "soft",
                 rho_state: str = "low-defect"):
        self.lambda_state = lambda_state
        self.tau_state = tau_state
        self.rho_state = rho_state

    def as_dict(self) -> dict:
        return {
            "Λ": self.lambda_state,
            "τ": self.tau_state,
            "ρ": self.rho_state,
        }
