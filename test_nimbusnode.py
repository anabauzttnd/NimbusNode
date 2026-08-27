# test_nimbusnode.py
"""
Tests for NimbusNode module.
"""

import unittest
from nimbusnode import NimbusNode

class TestNimbusNode(unittest.TestCase):
    """Test cases for NimbusNode class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NimbusNode()
        self.assertIsInstance(instance, NimbusNode)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NimbusNode()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
