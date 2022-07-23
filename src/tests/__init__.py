import unittest

from .test_valorant import *


def my_module_suite():
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(test_valorant)
    return suite
