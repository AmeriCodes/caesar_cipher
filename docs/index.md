# Caesar Cipher

The idea of this project is to represent a library capable of performing the Caesar cipher (ROT13).

## Usage Examples

### Encryption

```python
from caesar import encripta

encripta('Eduardo')  # rqhneqb
```

### Decryption
```python
from caesar import decripta

decripta('rqhneqb')  # eduardo
```

### Rotations other than 13
```python
from caesar import decripta, encripta

encripta('Eduardo')  # sriofrc
decripta('sriofrc', 14)  # eduardo
```