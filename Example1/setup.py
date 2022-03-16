from distutils.core import setup

setup(name='mypackage', # This is the name of the package, but "import mypackage" will NOT work
      version='1.0',
      py_modules=['foo', 'bar'], # These are the modules in the package. These are the names that can be imported
      )