# Table of Contents
1. [inTegrity](#integrity)
2. [Features](#features)
3. [Usage](#usage)
4. [Available Algorithms](#available-algorithms)

# inTegrity

`inTegrity` is a Python class for hashing files and comparing hashes. It uses the `hashlib` module to provide a variety of hashing algorithms.
This class can imported into any existing Python code.

## Features

- Hash files using any algorithm provided by the `hashlib` module.
- Save a hash value to a file.
- Load a hash value from a file.
- Compare two hash values.
- Compare two files based on their hash values.

## Usage

```python
from integrity import inTegrity

# Create an instance of the inTegrity class
hasher = inTegrity('sha256')

# Hash a file
hash_value = hasher.hash_file('path_to_your_file')

# Save the hash to a file
hasher.save_hash('path_to_save_hash', hash_value)

# Load a hash from a file
loaded_hash = hasher.load_hash('path_to_saved_hash')

# Compare two hashes
are_same = hasher.compare_hashes(hash_value, loaded_hash)

# Compare two files
are_same = hasher.compare_files('path_to_file1', 'path_to_file2')
```

## Available Algorithms

The available algorithms are those provided by the hashlib module and guaranteed to be available on all platforms. The default algorithm is 'sha256'.
Available algorithms can be listed by inspecting the available_algorithm attribute.