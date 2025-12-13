"""
PhiANDO Genesis - Main Orchestrator
Scientific AI Architecture (φ=1.618)
"""
import sys
from pathlib import Path

# Add modules to path
sys.path.insert(0, str(Path(__file__).parent / "01_NOUS"))
sys.path.insert(0, str(Path(__file__).parent / "02_LOGOS"))
sys.path.insert(0, str(Path(__file__).parent / "03_PATHOS"))

from phiando_brain import PhiandoBrain
from frege_logic import FregeLogic
from angela_persona import AngelaPersona
from dolores_persona import DoloresPersona

class PhiandoGenesis:
    def __init__(self):
        self.brain = PhiandoBrain()
        self.logic = FregeLogic()
        self.angela = AngelaPersona()
        self.dolores = DoloresPersona()
        print("[GENESIS] PhiANDO Trinity Initialized")
    
    def pulse_check(self):
        return {
            "brain": self.brain.pulse(),
            "logic": self.logic.monad_calculation({}),
            "angela": self.angela.speak("System online"),
            "dolores": self.dolores.speak("All systems operational")
        }

if __name__ == "__main__":
    genesis = PhiandoGenesis()
    print("\n=== PULSE CHECK ===")
    import json
    print(json.dumps(genesis.pulse_check(), indent=2))
