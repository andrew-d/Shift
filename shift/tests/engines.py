from . import BaseTestCase, parameters, parametrize
import os
from glob import glob
import unittest

file_path = os.path.dirname(os.path.abspath(__file__))
search_path = os.path.abspath(os.path.join(file_path, 'templates', '*.test.*'))
test_file_names = glob(search_path)

# print 'search_path:', repr(search_path)
# print 'test_file_names:', repr(test_file_names)

def generate_name(idx, param):
    file_type = os.path.basename(param).split('.')[0]
    return 'test_with_' + file_type

@parametrize
class TestTemplates(BaseTestCase):
    @parameters(test_file_names, name_func=generate_name)
    def test_with(self, name):
        # print 'testing with:', name
        pass


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestTemplates))

    return suite


def main():
    """
    This runs the our tests, suitable for a command-line application
    """
    try:
        unittest.main(defaultTest='suite')
    except Exception as e:
        print "Exception: {0!s}".format(e)

if __name__ == "__main__":
    main()

