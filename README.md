![To Temp logo](https://raw.githubusercontent.com/eddyyxxyy/ToTemp/Develop-0.5.0/logo.png)

# ToTemp
<div style="display: inline-block">
  <img src="https://shields.io/pypi/v/totemp"  alt="package version"/>
  <img src="https://img.shields.io/pypi/l/totemp.svg"  alt="license"/>
  <img src="https://results.pre-commit.ci/badge/github/eddyyxxyy/ToTemp/main.svg" alt="pre-commit.ci"/>
</div>

**ToTemp** is a temperature conversion package with Celsius, Delisle, Fahrenheit, Kelvin, Rankine, Réaumur, Newton and Rømer scales.

> This package aims to bring the simple and straight to the point,
but precise, Object Oriented experience of working with temperature
scale data types.

---

## Usage

First of all, install the package:

````shell
pip install totemp
````

or, to have an example in poetry environments:

````shell
poetry add totemp
````

> For more information, read the docs: [ToTemp Docs]('insert link here')

### The instances:

````python
from totemp import Celsius, Fahrenheit

if __name__ == '__main__':
    temps: list = [Celsius(12), Celsius(25), Celsius(50)]
    print(temps[0])  # '12 ºC'
    print(temps)  # [Celsius(12), Celsius(25), Celsius(50)]

    temps = list(map(Celsius.to_fahrenheit, temps))
    print(temps[0])  # '53.6 ºF'
    print(temps)  # [Fahrenheit(53.6), Fahrenheit(77.0), Fahrenheit(122.0)]
````

### It's representations and properties:

> Property *`symbol`* is **read-only**.

````python
from totemp import Fahrenheit

if __name__ == '__main__':
    temp0 = Fahrenheit(53.6)
    print(temp0.__repr__())  # 'Fahrenheit(53.6)'
    print(temp0.__str__())  # '53.6 ºF'
    print(temp0.symbol)  # 'ºF'
    print(temp0.value)  # 53.6
````

### Comparision operations ('==', '!=', '>', '>=', '<',...):

> The comparision/arithmetic implementation attempts to convert the value of `other` (if it is a temperature instance) and then evaluate the expression.

````python
import totemp as tp

if __name__ == '__main__':
    temp0, temp1 = tp.Celsius(0), tp.Fahrenheit(32)

    print(f'temp0: {repr(temp0)}')  # Celsius(0)
    print(f'temp1: {repr(temp1.to_celsius())}')  # Celsius(0.0)

    print(temp0 != temp1)  # False

    print(temp0 > temp1)  # False

    print(temp0 < temp1)  # False

    print(temp0 >= temp1)  # True

    print(temp0 <= temp1)  # True

    print(temp0 == temp1)  # True
````

### Arithmetic operations ('+', '-', '*', '**', '/', '//', '%', ...):

````python
from totemp import Newton, Rankine

if __name__ == '__main__':
    temp0 = Newton(33)
    temp1 = Rankine(671.67)

    temp2 = temp0 + temp1

    print('temp2:', temp2)  # temp2: 65.99999999999999 ºN
    print('temp2:', repr(temp2))  # temp2: Newton(65.99999999999999)
    print('temp2:', temp2.value, temp2.symbol)  # temp2: 65.99999999999999 ºN

    print((temp0 + temp1).rounded())  # 66 ºN
    print(repr((temp0 + temp1).rounded()))  # Newton(66)

    print(temp2 + 12.55)  # 78.54999999999998 ºN
    print((12 + temp2.rounded()))  # 78 ºN
````

### ToTemp classes can work with many built-in Python functions:

````python
from math import floor, ceil, trunc

from totemp import Reaumur

if __name__ == '__main__':
    temp = Reaumur(100.4)

    float(temp)  # 100.4
    int(temp)  # 100
    round(temp)  # Reaumur(100)
    abs(temp)  # Reaumur(100)
    floor(temp)  # Reaumur(100)
    ceil(temp)  # Reaumur(101)
    trunc(temp)  # Reaumur(100)
    divmod(temp, temp0 := Reaumur(25.1))  # (Reaumur(4.0), Reaumur(0.0))

````



### Temperature Instance Conversions:

````python
import totemp

if __name__ == '__main__':
    temp = totemp.Fahrenheit(32)

    print(temp.to_celsius())  # 0.0 ºC
    print(temp.to_fahrenheit())  # 32 ºF
    print(temp.to_delisle())  # 150.0 ºDe
    print(temp.to_kelvin())  # 273.15 K
    print(temp.to_newton())  # 0.0 ºN
    print(temp.to_rankine())  # 491.67 ºR
    print(temp.to_reaumur())  # 0.0 ºRé
    print(temp.to_romer())  # 7.5 ºRø
````

## Changelog

---

- _0.1.0_:
  - Yanked, not functional;
- _0.2.0_:
  - Functional;
  - Can convert Celsius to Delisle, Fahrenheit, Kelvin, Newton, Rankine, Réaumur and Rømer.
- _0.3.0_:
  - Changed methods implementations and adds Fahrenheit conversions;
      - <scale_value> parameter is now positional-only;
      - Adds new parameter -> float_ret -> Float Return (True by default, keyword-only);
      - Celsius class methods were updated and enhanced;
      - Can now convert Fahrenheit to Celsius, Delisle, Kelvin, Newton, Rankine, Réaumur and Rømer.
- _0.4.0_:
  - There are two new Classes, Kelvin and Delisle, functional and ready-to-use.

- **0.5.0**:
  - The implementation has been **completely refactored**:

    1 - ***All classes inhehits from `AbstractTemperature`** (our new abstract  Base Class)*;

    2 - ***All classes now available***:
      - *`Celsius`;*
      - *`Fahrenheit`;*
      - *`Delisle`;*
      - *`Kelvin`;*
      - ***(\*New)** `Newton`;*
      - ***(\*New)** `Rankine`;*
      - ***(\*New)** `Réaumur`;*
      - ***(\*New)** `Rømer`.*

    3 - ***New features***:
      - *The majority of Python's built-in functions works with the instances*;
      - *More pythonic properties and methods implementations*;
      - *Arithmetic operations;*
      - *Comparision operations;*
      - *`convert_to()` method;*

    4 - ***Removals***:
      - *`precise()` method;*
      - *`float_ret()` param;*
      - *differentiating int/float;*

    5 - ***Known problemns***:
      - *`pow()` doesn't work as intended;*

---

## License

For more information, check LICENSE file.
