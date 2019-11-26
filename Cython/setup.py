from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

cexample_extension = Extension(
    name="wrapcexample",            
    sources=["wrapcexample.pyx"],
    libraries=["cexample"],
    library_dirs=["lib"],
    include_dirs=["lib"]
)

setup(
    name="wrapcexample",
    ext_modules=cythonize([cexample_extension])
)