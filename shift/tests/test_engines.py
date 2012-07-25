from . import BaseTestCase, parameters, parametrize, shift
import os
import sys
from glob import glob
import unittest
import yaml

def is_pypy():
    return hasattr(sys, 'pypy_version_info')

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")
test_spec = os.path.join(file_path, "spec.yaml")
with open(test_spec, 'rb') as f:
    test_details = list(yaml.load_all(f.read()))

def generate_name(idx, param):
    return 'test_with_' + param['test_name']

@parametrize
class TestTemplates(BaseTestCase):
    def setup(self):
        self.shift = shift.Shift(template_root=file_path)

    @parameters(test_details, name_func=generate_name)
    def test_with(self, details):
        # print "Template file: {0}".format(details['template_file'])
        # print "Output file  : {0}".format(details['output_file'])
        # print "Engine name  : {0}".format(details['engine_name'])

        # We special-case skip Cheetah on PyPy since it doesn't handle
        # the template engine properly.
        if is_pypy() and details['engine_name'] == 'cheetah':
            return


        template = self.shift.new(details['template_file'])
        self.assert_true(template is not None)

        rendered = template.render(details['params'])

        expected_path = os.path.join(file_path, details['output_file'])
        with open(expected_path, 'rb') as f:
            expected = f.read()

        self.assert_equal(rendered, expected)


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

