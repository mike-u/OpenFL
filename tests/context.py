# -*- coding: utf-8 -*-

import sys
import os
import inspect
from os.path import dirname

# Add parent directory to sys.path so we find OpenFL.
sys.path.insert(0, dirname(dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))))


from OpenFL import FLP
from OpenFL import Printer
