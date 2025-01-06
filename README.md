## Obfuscator Python Code
## Features:
- Renaming Function, Classes, Identifiers and Variables names.
- Minifier, Remove Annotations.
- String Encode (zlib+base64).
### Sample:
```python
def hello_world(name):
    print("Hello", name, "!")
hello_world("Alice")
```
### Sample Obf:
```python
import zlib as A,base64 as B
def C(O0O0O0O00O0O00O0O00O00O00O00O00O00O0O00O0O00O0O00O0O0O00O00O00O0O0O0O00O00O00O00O0O0O0O0O00O0O00O00O00O00O00O0O0O0O00O0O0O00O0O00O0O0O00O00O0O00O0O00O0O0O00O0O00O00O0O0O00O00O0O00O00O00O00O00O00O00O00O0O0O00O00O00O0O00O00O0O0O0O00O0O00O0O0O00O00O0O0O00O0O0O0):print((lambda s:A.decompress(B.b64decode(s)).decode())('eJzzSM3JyQcABYwB9Q=='),O0O0O0O00O0O00O0O00O00O00O00O00O00O0O00O0O00O0O00O0O0O00O00O00O0O0O0O00O00O00O00O0O0O0O0O00O0O00O00O00O00O00O0O0O0O00O0O0O00O0O00O0O0O00O00O0O00O0O00O0O0O00O0O00O00O0O0O00O00O0O00O00O00O00O00O00O00O00O0O0O00O00O00O0O00O00O0O0O0O00O0O00O0O0O00O00O0O0O00O0O0O0,(lambda s:A.decompress(B.b64decode(s)).decode())('eJxTBAAAIgAi'))
C((lambda s:A.decompress(B.b64decode(s)).decode())('eJxzzMlMTgUABWAB3w=='))
```
## Demo
(https://i.imgur.com/HpvEXuN.png)
