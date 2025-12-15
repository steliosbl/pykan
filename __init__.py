from .kan.MultKAN import MultKAN, KAN
from .kan.utils import *

# Expose nested kan modules as top-level kan.* modules
from .kan import utils, LBFGS, KANLayer, Symbolic_KANLayer, spline, MLP, compiler
import sys
sys.modules['kan.utils'] = utils
sys.modules['kan.LBFGS'] = LBFGS
sys.modules['kan.KANLayer'] = KANLayer
sys.modules['kan.Symbolic_KANLayer'] = Symbolic_KANLayer
sys.modules['kan.spline'] = spline
sys.modules['kan.MLP'] = MLP
sys.modules['kan.compiler'] = compiler

__all__ = ['MultKAN', 'KAN', 'utils', 'LBFGS', 'KANLayer', 'Symbolic_KANLayer', 'spline', 'MLP', 'compiler']
