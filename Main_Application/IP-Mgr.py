
print("Loading app...")

from pathlib import Path
import sys

#print('__file__ = %s' % (__file__))
cwd = Path(__file__).parent.parent.resolve()
#print('%s\stubs' % cwd)
#print('%s\descriptors' % cwd)
#print(sys.path)
#sys.path.append(cwd)
sys.path.append('%s\stubs' % cwd)
sys.path.append('%s\descriptors' % cwd)
#sys.path.append('%s\implementations' % cwd)
#print(sys.path)

import app


