# -*- coding: utf-8 -*-.

import unittest
import os

os.chdir("testing")

from testAccions                import *
from testActorsUserHistory      import *
from testArchivo                import *
from testBackLog                import *
from testCategory               import *
from testHistory                import *
from testLogin                  import *
from testObjective              import *
from testObjectivesUserHistory  import *
from testRole                   import *
from testSprint                 import *
from testTask                   import *
from testTeam                   import *
from testUser                   import *

if __name__ == '__main__':
    unittest.main()

