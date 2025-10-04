"""
516 Hackers - Integration Tests
End-to-end testing of the toolkit
"""

import unittest
import os
import tempfile
from scripts.sherlock_wrapper import Sherlock516
from scripts.metadata_analyzer import MetadataAnalyzer516

class TestIntegration516(unittest.TestCase):
    
    def test_sherlock_integration(self):
        """Test Sherlock wrapper integration"""
        with tempfile.TemporaryDirectory() as temp_dir:
            investigator = Sherlock516('testuser', temp_dir)
            self.assertEqual(investigator.username, 'testuser')
            self.assertEqual(investigator.output_dir, temp_dir)
    
    def test_metadata_analyzer_integration(self):
        """Test metadata analyzer integration"""
        # Create a test image
        from PIL import Image
        with tempfile.TemporaryDirectory() as temp_dir:
            test_image_path = os.path.join(temp_dir, 'test.png')
            img = Image.new('RGB', (100, 100), color='red')
            img.save(test_image_path)
            
            analyzer = MetadataAnalyzer516(temp_dir)
            metadata = analyzer.extract_metadata(test_image_path)
            
            self.assertIn('filename', metadata)
            self.assertIn('image_size', metadata)

if __name__ == '__main__':
    unittest.main()
