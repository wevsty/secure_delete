
# secure_delete

![](https://img.shields.io/badge/language-Python3-blue.svg)
![](https://img.shields.io/pypi/v/secure_delete.svg)

secure_delete is a tool for safely delete files.

Files deleted with secure_delete will be difficult to recover.

# Environment requirements

Python 3.X

Support for Windows and Linux

# Install
```bash
pip install secure_delete
```

# Usage

## Command

```bash
secdel --help
```

## Python lib

```python
from secure_delete import secure_delete

secure_delete.secure_random_seed_init()
secure_delete.secure_delete('Z:\\TEST.exe')
```

# License

MIT License