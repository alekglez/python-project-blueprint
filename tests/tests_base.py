# -*- coding: utf-8 -*-

import unittest
from unittest import TestCase

from project import main


class BaseTestCases(TestCase):
    def test_execution(self):
        self.assertEqual(main.execute(), None)


if __name__ == "main":
    unittest.main()
