import sys

from .deprecation import WarnOnDeprecatedModuleAttributes
from .enums import Align
from .enums import TextMode
from .enums import XPos
from .enums import YPos
from .fpdf import FPDF
from .fpdf import FPDF_FONT_DIR as _FPDF_FONT_DIR
from .fpdf import FPDF_VERSION as _FPDF_VERSION
from .fpdf import FPDFException
from .fpdf import TitleStyle
from .html import HTML2FPDF
from .html import HTMLMixin
from .prefs import ViewerPreferences
from .template import FlexTemplate
from .template import Template

FPDF_VERSION = _FPDF_VERSION
"Current FPDF Version, also available via `__version__`"

FPDF_FONT_DIR = _FPDF_FONT_DIR
"""This is the location of where to look for fonts."""

# Pattern from sir Guido Von Rossum: https://stackoverflow.com/a/72911884/636849
# > a module can define a class with the desired functionality, and then at
# > the end, replace itself in sys.modules with an instance of that class
sys.modules[__name__].__class__ = WarnOnDeprecatedModuleAttributes

__license__ = "LGPL 3.0"

__version__ = FPDF_VERSION


__all__ = [
    # metadata
    "__version__",
    "__license__",
    # Classes
    "FPDF",
    "FPDFException",
    "Align",
    "XPos",
    "YPos",
    "Template",
    "FlexTemplate",
    "TitleStyle",
    "ViewerPreferences",
    "HTMLMixin",
    "HTML2FPDF",
    # FPDF Constants
    "FPDF_VERSION",
    "FPDF_FONT_DIR",
]
