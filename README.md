# ToTemp
<div style="display: inline-block">
  <img src="https://shields.io/pypi/v/totemp"  alt="package version"/>
  <img src="https://img.shields.io/pypi/l/totemp.svg"  alt="license"/>
</div>

**ToTemp** is a temperature conversion package between Celsius, Delisle, Fahrenheit, Kelvin, Rankine, Reaumur, Newton and Romer

## Usage

First of all, install the package:

```
pip install totemp
```

or, to have an example in poetry environments:

```
poetry add --group dev totemp
```

Then, just use it:

> In these examples, you can observe the methods working with all
available Classes in this package

````python
# Import Celsius class
from totemp import Celsius

temperature = Celsius.to_fahrenheit(35)
print(temperature)  # 95.0 -> float

temperature = Celsius.to_fahrenheit(35, float_ret=False)
print(temperature)  # 95 -> int
````
````python
# Import Fahrenheit class
from totemp import Fahrenheit

temperature = Fahrenheit.to_newton(18.746)
print(temperature)  # -2.4299000000000004 -> float

temperature = Fahrenheit.to_newton(18.746, float_ret=False)
print(temperature)  # -2 -> int
````
````python
# Import Delisle class
from totemp import Delisle

temperature = Delisle.to_romer(37263.271)
print(temperature)  # -12982.14485 -> float

temperature = Delisle.to_romer(37263.271, float_ret=False)
print(temperature)  # -12982 -> int
````
````python
# Import Kelvin class
from totemp import Kelvin

temperature = Kelvin.to_reaumur(44.28137746)
print(temperature)  # -183.094898032 -> float

temperature = Kelvin.to_reaumur(44.28137746, float_ret=False)
print(temperature)  # -183 -> int
````
````python
# Import all classes
import totemp as tp

temperature = tp.Celsius.to_delisle(345.797)
print(temperature)  # -368.69550000000004 -> float

temperature = tp.Celsius.to_delisle(345.797, float_ret=False)
print(temperature)  # -368 -> int

temperature = tp.Fahrenheit.to_rankine(500)
print(temperature)  # 959.6700000000001 -> float

temperature = tp.Fahrenheit.to_rankine(500, float_ret=False)
print(temperature)  # 959 -> int

temperature = tp.Delisle.to_kelvin(12.5887)
print(temperature)  # 364.7575333333333 -> float

temperature = tp.Delisle.to_kelvin(12.5887, float_ret=False)
print(temperature)  # 364 -> int

temperature = tp.Kelvin.to_romer(44.28137746)
print(temperature)  # -112.6560268335 -> float

temperature = tp.Kelvin.to_reaumur(44.28137746, float_ret=False)
print(temperature)  # -112 -> int
````

Note that **all returns are *float values*** if you don't specify "float_ret"
parameter as False, which is True by default and that **applies to all methods**.

All methods have two parameters, the **value** (which is positional-only)
and the **return type** (which is <float_ret>, that is by default True to return float
values and keyword-only)

## Package Versions

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


- **0.4.0**:
  - There are **two new Classes**, **Kelvin** and **Delisle**, functional and ready-to-use.
---

## License

For more information, check LICENSE file.
