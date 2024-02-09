import unittest
import hashlib
import os
from integrity import inTegrity

class HashToolsTests(unittest.TestCase):
    def setUp(self):
        self.ht = inTegrity()
        self.directory = './tests/test_files/'

    def test_hash_file(self):
        filename = self.directory + 'test_file.txt'
        with open(filename, 'w') as file:
            file.write('This is a test file.')
        expected_hash = hashlib.sha256(b'This is a test file.').hexdigest()
        result = self.ht.hash_file(filename)
        self.assertEqual(result, expected_hash)
        os.remove(filename)
        self.assertFalse(os.path.exists(filename))

    def test_save_hash(self):
        filename = 'test_hash.txt'
        hash_value = 'abcdef1234567890'
        expected_path = filename + '.sha256'
        result = self.ht.save_hash(filename, hash_value)
        self.assertEqual(result, expected_path)
        with open(expected_path, 'r') as file:
            saved_hash = file.read()
        self.assertEqual(saved_hash, hash_value)
        os.remove(expected_path)
        self.assertFalse(os.path.exists(expected_path))


    def test_load_hash(self):
        filename = 'test_hash.txt.sha256'
        save_hash_filename = 'test_hash.txt'
        expected_hash = 'abcdef1234567890'
        self.ht.save_hash(save_hash_filename, expected_hash)
        result = self.ht.load_hash(filename)
        self.assertEqual(result, expected_hash)
        os.remove(filename)
        self.assertFalse(os.path.exists(filename))

    def test_compare_hashes(self):
        hash1 = 'abcdef1234567890'
        hash2 = 'abcdef1234567890'
        result = self.ht.compare_hashes(hash1, hash2)
        self.assertTrue(result)

    def test_compare_files(self):
        file1 = self.directory + 'test_file1.txt'
        file2 = self.directory + 'test_file2.txt'
        with open(file1, 'w') as f1, open(file2, 'w') as f2:
            f1.write('This is a test file.')
            f2.write('This is a test file.')
        result = self.ht.compare_files(file1, file2)
        self.assertTrue(result)
        os.remove(file1)
        os.remove(file2)
        self.assertFalse(os.path.exists(file1))
        self.assertFalse(os.path.exists(file2))
        
    def test_algorithm_types(self):
        self.ht.algorithm = 'sha256'
        self.assertEqual(self.ht.algorithm, 'sha256')
        self.ht.algorithm = 'md5'
        self.assertEqual(self.ht.algorithm, 'md5')
        self.ht.algorithm = 'sha1'
        self.assertEqual(self.ht.algorithm, 'sha1')
        self.ht.algorithm = 'sha512'
        self.assertEqual(self.ht.algorithm, 'sha512')
        self.ht.algorithm = 'sha224'
        self.assertEqual(self.ht.algorithm, 'sha224')
        self.ht.algorithm = 'sha384'
        self.assertEqual(self.ht.algorithm, 'sha384')

if __name__ == '__main__':
    unittest.main()