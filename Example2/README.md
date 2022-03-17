Example with automatic package find and modules organised in directories.
This is the structure of the directory:

  find_test.py
  foo.py
  README.md
  setup.py
  mkpkg
    __init__.py
    bar.py
    sub1
      __init__.py
      sub1one.py
      sub1two.py
      sub1sub1
        __init__.py
        sub1sub1one.py
      sub1sub2
        sub1sub2one.py      
    sub2
      sub2one.py
      sub2sub1
        __init__.py
        sub2sub1one.py
        
If we run
  pip install .
from the directory which contains the setup.py script, setuptools.find_packages() will recursively find all the modules and nested modules.
The packages are organised following the structure of the modules in the filesystem.
A (sub)package must contain a __init__.py file, otherwise it is discarded.
Let's which modules are effectively installed:
  pip show -f mypackage
    
    mypkg\__init__.py
    mypkg\bar.py
      mypkg contains a __init__.py file, so all the .py files in this directory (including __init__.py) are part of the package
    mypkg\sub1\__init__.py
    mypkg\sub1\sub1one.py
    mypkg\sub1\sub1two.py
      mypkg\sub1 contains a __init__.py file: all the .py files are included
    mypkg\sub1\sub1sub1\__init__.py      
    mypkg\sub1\sub1sub1\sub1sub1one.py
      the search for packages continues recursively

Observe that some modules are ignored. This is because the recursive search for __init__.py fails at some point.
For example mkpkg\sub2 does not have a __init__.py. This directory is entirely excluded, even if a subdirectory (sub2sub1one) has a __init__.py.

Once the package is installed, we can run the example from any directory

python path/to/.../tests/example2.py

    