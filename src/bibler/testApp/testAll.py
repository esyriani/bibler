'''
BiBler - A software to manage references of scientific articles using BibTeX.
Copyright (C) 2018  Eugene Syriani

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

'''
Created on Jan 13, 2014
.. moduleauthor:: Eugene Syriani

.. versionadded:: 1.0

This package contains the modules to unit test the L{app.UserInterface.UserInterface} class.
'''
import unittest
from .testAdd import TestAdd
from .testDelete import TestDelete
from .testUpdate import TestUpdate
from .testDuplicate import TestDuplicate
from .testPreview import TestPreview
from .testSearch import TestSearch
from .testSort import TestSort

def testApp():
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestAdd))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestDelete))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestUpdate))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestDuplicate))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestPreview))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestSearch))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestSort))
    return suite  


if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(testApp())