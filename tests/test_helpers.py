"""
516 Hackers - Tests for Helper Functions
"""

import unittest
import os
import tempfile
from utils.helpers import *

class TestHelpers516(unittest.TestCase):
    
    def test_create_output_dir(self):
        """Test output directory creation"""
        with tempfile.TemporaryDirectory() as temp_dir:
            output_dir = create_output_dir(temp_dir)
            self.assertTrue(os.path.exists(output_dir))
            self.assertIn('scan_', output_dir)
    
    def test_save_json(self):
        """Test JSON saving functionality"""
        test_data = {'test': 'data', 'number': 123}
        
        with tempfile.TemporaryDirectory() as temp_dir:
            filename = os.path.join(temp_dir, 'test.json')
            save_json(test_data, filename)
            
            self.assertTrue(os.path.exists(filename))
            
            # Verify content
            with open(filename, 'r') as f:
                loaded_data = json.load(f)
            self.assertEqual(test_data, loaded_data)
    
    def test_calculate_file_hash(self):
        """Test file hash calculation"""
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            f.write('test content')
            temp_file = f.name
        
        try:
            file_hash = calculate_file_hash(temp_file)
            self.assertEqual(len(file_hash), 32)  # MD5 hash length
            self.assertEqual(file_hash, '9473fdd0d880a43c21b7778d34872157')
        finally:
            os.unlink(temp_file)
    
    def test_validate_email(self):
        """Test email validation"""
        valid_emails = [
            'test@example.com',
            'user.name@domain.co.uk',
            'user+tag@example.org'
        ]
        
        invalid_emails = [
            'invalid',
            'missing@domain',
            '@domain.com',
            'spaces in@email.com'
        ]
        
        for email in valid_emails:
            self.assertTrue(validate_email(email), f"Should be valid: {email}")
        
        for email in invalid_emails:
            self.assertFalse(validate_email(email), f"Should be invalid: {email}")

if __name__ == '__main__':
    unittest.main()
