# -*- coding: utf-8 -*-
# BioSTEAM: The Biorefinery Simulation and Techno-Economic Analysis Modules
# Copyright (C) 2020, Yoel Cortes-Pena <yoelcortes@gmail.com>
# 
# This module is under the UIUC open-source license. See 
# github.com/BioSTEAMDevelopmentGroup/biosteam/blob/master/LICENSE.txt
# for license details.
"""
"""

__version__ = '2.22.5'

#: Chemical engineering plant cost index (defaults to 567.5 at 2017).
CE = 567.5 

#: Whether to add label the ID of streams with sources and sinks in process 
#: flow diagrams.
LABEL_PROCESS_STREAMS_IN_DIAGRAMS = True

#: Whether to automatically generate diagrams when displaying an object in the
#: IPython console.
ALWAYS_DISPLAY_DIAGRAMS = True

#: Whether to ignore unit graphics and display unit nodes as dots in process
#: flow diagrams.
MINIMAL_UNIT_DIAGRAMS = False

#: Whether to number unit operations in diagrams according to their order in the system path.
LABEL_PATH_NUMBER_IN_DIAGRAMS = False

# %% Initialize BioSTEAM 

from flexsolve import speed_up
from ._heat_utility import HeatUtility, UtilityAgent
from ._power_utility import PowerUtility
from ._unit import Unit
from ._system import System
from ._tea import CombinedTEA, TEA
from ._flowsheet import Flowsheet, main_flowsheet
from ._network import Network
from . import utils
from . import units
from . import evaluation
from . import exceptions
from . import process_tools
from . import examples
from . import report
from . import digraph

__all__ = ('Unit', 'PowerUtility', 'HeatUtility', 'UtilityAgent',
           'System', 'TEA', 'CombinedTEA', 'utils', 'units', 'evaluation', 
           'main_flowsheet', 'Flowsheet', 'CE', 'Chemical', 'Chemicals', 'Stream',
           'MultiStream', 'settings', 'Network', 'exceptions', 'speed_up', 'report',
           'digraph', 'process_tools', 'examples', *units.__all__, *evaluation.__all__
)

from thermosteam import Chemical, Chemicals, Thermo, Stream, MultiStream, settings
from .evaluation import *
from .units import *
