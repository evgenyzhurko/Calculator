# Calculator
Homework for LDC.

## Installation
### PREREQUISITES
* Python 2.7
* For building: [setuptools](https://github.com/pypa/setuptools)

#### From Git
Use the command:
```
git clone https://github.com/evgenyzhurko/Calculator.git

cd Calculator
python setup.py install
```
#### From ZIP
Unpack ```Calculator-*.zip```, chanhe to the ```Calculator-*/``` directory, and run:

```python setup.py install```
#### Testing
Use the command:

```python setup.py test```
## Using Calculator
#### Python interpreter
```
>>> from calculator import evaluate
>>> evaluate('1+1-sin(pi/2)')
1.0
```
#### Bash shell
```
$ calc '1+1-sin(pi/2)'
1.0
```
## Features
#### Support logic and comparison operators
Example:
```
>>> evaluate('1 & 2 <= 1')
True
>>> evaluate('1 & 2 > 1')
False
```
#### Mathematical functions and constants
Calculator import ```math``` package by default. You can use all functions and constants that defined in ```math``` package.
Example:
```
>>> evaluate("sin(pi/2) - cos(pi)  + log(e**4)")
6.0
```
#### Support binary, octal, decimal, hexadecimal number systems
Use prefix ```0b``` for binary, ```0o``` for octal and ```0x``` for hexadecimal numbers.

Example:
```
>>> evaluate('0b10 + 0o10 + 10 + 0xF')
35.0
```
#### Dynamically expandable system for importing modules

Calculator could import additional modules if you say it to him.
##### Example for python interpreter:
```
>>> evaluate('isinf(beta(1,2) - 0.5)','scipy.special','numpy')
False
```
Second and the following parameters in ```evaluate``` mean name of package to import.
##### Example for bash shell:
```
$ calc "beta(1,2)" "scipy.special"
0.5
```
Second and the following parameters in ```calc``` mean name of package to import.
