'''OpenGL extension ANGLE.window_fixed_size

This module customises the behaviour of the 
OpenGL.raw.EGL.ANGLE.window_fixed_size to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ANGLE/window_fixed_size.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.EGL import _types, _glgets
from OpenGL.raw.EGL.ANGLE.window_fixed_size import *
from OpenGL.raw.EGL.ANGLE.window_fixed_size import _EXTENSION_NAME

def glInitWindowFixedSizeANGLE():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION