First example of creating a python package composed of two files (foo.py and bar.py).
The setup.py file is in the same directory as foo.py and bar.py.

Steps to install and use:
1. cd into this directory (the directory of setup.py)
2. run
     python -m pip install .
3. To check that the package is installed run (from any directory)
     python -m pip list
   We can see that the package mypackage is installed
4. To test the package, cd into any directory and run the interpreter
     import foo
     help(foo)
     foo.print_me()
     
     import bar
     bar.print_me()
     
5. To uninstall the package run
     python -m pip uninstall mypackage
   from any directory

Note: python -m pip is safer than simply pip, but in most (almost all) circumnstances they are the same thing.
If running pip only, it's useful to check that this is consistent with python (in cases we use a virtual environment).
   
Another useful pip command is:
  - pip show -f mypackage
which displays the modules in the package

Observe that if the package is installed with
  python setup.py install
it cannot be later uninstalled!
     

     