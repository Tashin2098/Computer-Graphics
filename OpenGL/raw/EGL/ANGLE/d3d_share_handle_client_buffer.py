'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.EGL import _types as _cs
# End users want this...
from OpenGL.raw.EGL._types import *
from OpenGL.raw.EGL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'EGL_ANGLE_d3d_share_handle_client_buffer'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.EGL,'EGL_ANGLE_d3d_share_handle_client_buffer',error_checker=_errors._error_checker)
EGL_D3D_TEXTURE_2D_SHARE_HANDLE_ANGLE=_C('EGL_D3D_TEXTURE_2D_SHARE_HANDLE_ANGLE',0x3200)

