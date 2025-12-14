# test_usterra.py
"""
Tests for USTerra module.
"""

import unittest
from usterra import USTerra

class TestUSTerra(unittest.TestCase):
    """Test cases for USTerra class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = USTerra()
        self.assertIsInstance(instance, USTerra)
        
    def test_run_method(self):
        """Test the run method."""
        instance = USTerra()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
