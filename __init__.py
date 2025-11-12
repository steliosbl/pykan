# Inject submodule paths into sys.modules to allow imports like "from kan.LBFGS import X"
# This must be done before any other imports to avoid circular dependencies
import sys

# Import the submodules directly and register them
import kan.kan.LBFGS
import kan.kan.utils
sys.modules['kan.LBFGS'] = sys.modules['kan.kan.LBFGS']
sys.modules['kan.utils'] = sys.modules['kan.kan.utils']

# Now import everything from the inner kan.kan package
from kan.kan import *

# Explicitly expose key classes
from kan.kan.MultKAN import KAN, MultKAN
from kan.kan.KANLayer import KANLayer
from kan.kan.Symbolic_KANLayer import Symbolic_KANLayer
from kan.kan.MLP import MLP
from kan.kan.LBFGS import LBFGS

# Make utils available
from kan.kan import utils

__all__ = [
    'KAN',
    'MultKAN', 
    'LBFGS',
    'KANLayer',
    'Symbolic_KANLayer',
    'MLP',
    'utils',
]

#torch.use_deterministic_algorithms(True)