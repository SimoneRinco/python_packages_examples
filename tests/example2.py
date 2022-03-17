import mypkg

print("== mypkg is here:")
print(mypkg.__file__)

print("== Importing mypkg.bar")
import mypkg.bar
mypkg.bar.print_me()

print("== Importing mypkg.sub1.sub1one")
from mypkg.sub1 import sub1one
sub1one.print_me()

print("== Importing mypkg.sub1.sub1sub1.sub1sub1one")
from mypkg.sub1.sub1sub1 import sub1sub1one
sub1sub1one.print_me()

try:
    from mypkg.sub1.sub1sub2 import sub1sub2one
except ImportError:
    # This is because directory sub1/sub1sub2 doesn't have a __init__.py file,
    # even if sub1 does.
    print("== Cannot import mypkg.sub1.sub1sub2.sub1sub2one")
    
try:
    from mypkg.sub2 import sub2one
except ImportError:
    # This is because directory sub2 doesn't have a __init__.py file
    print("== Cannot import mypkg.sub2.sub2one")  

try:
    from mypkg.sub2.sub2sub1 import sub2sub1one
except ImportError:
    # This is because directory sub2 doesn't have a __init__.py file,
    # even if sub2/sub2sub1 does.
    print("== Cannot import mypkg.sub2.sub2sub1.sub2sub1one")    