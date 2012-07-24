from . import BaseTestCase
from .. import Shift, BaseTemplate
import os
import unittest

class TestSearchPaths(BaseTestCase):
    def setup(self):
        self.sh = Shift()

    def search(self, path):
        return list(self.sh._paths_iterator(path))

    def test_simple_search(self):
        self.assert_equal(self.search('foo.bar'), ['foo.bar', 'bar'])

    def test_mutiple_extensions(self):
        paths = self.search("foo.bar.baz.asdf")
        self.assert_equal(paths, ["foo.bar.baz.asdf", "bar.baz.asdf", "baz.asdf", "asdf"])

    def test_subdir_searching(self):
        subdir = os.path.join("subdir", "foo.bar")
        paths = self.search(subdir)
        self.assert_equal(paths, [subdir, "foo.bar", "bar"])


class TestEngineSearch(BaseTestCase):
    def setup(self):
        self.sh = Shift()

        class EngineOne(BaseTemplate):
            @classmethod
            def on_initialize(klass):
                return True

            def load_string(self, string):
                pass

            def render(self, context=None):
                return ''

        class EngineTwo(BaseTemplate):
            @classmethod
            def on_initialize(klass):
                return True

            def load_string(self, string):
                pass

            def render(self, context=None):
                return ''

        self.sh.register_on_instance(EngineOne, "one")
        self.sh.register_on_instance(EngineTwo, "baz.one")

    def search(self, path):
        return list(self.sh._engines_iterator(path))

    def test_search_returns_correct_engine(self):
        engines = self.search("foo.one")
        self.assert_equal(len(engines), 1)
        self.assert_equal(engines[0].__name__, "EngineOne")

    def test_search_returns_specific_first(self):
        engines = self.search("baz.one")
        self.assert_equal(len(engines), 2)
        self.assert_equal(engines[0].__name__, "EngineTwo")
        self.assert_equal(engines[1].__name__, "EngineOne")

    def test_search_returns_specific_first_subdir(self):
        class EngineThree(BaseTemplate):
            @classmethod
            def on_initialize(klass):
                return True

            def load_string(self, string):
                pass

            def render(self, context=None):
                return ''

        self.sh.register_on_instance(EngineThree, 'views/baz.one')

        engines = self.search("views/baz.one")
        self.assert_equal(len(engines), 3)
        self.assert_equal(engines[0].__name__, "EngineThree")
        self.assert_equal(engines[1].__name__, "EngineTwo")
        self.assert_equal(engines[2].__name__, "EngineOne")


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSearchPaths))
    suite.addTest(unittest.makeSuite(TestEngineSearch))

    return suite

