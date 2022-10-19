# ToTemp
<div style="display: inline-block">
  <img src="https://shields.io/pypi/v/totemp"  alt="package version"/>
  <img src="https://img.shields.io/pypi/l/totemp.svg"  alt="license"/>
</div>

**ToTemp** is a temperature conversion package between Celcius, Delisle, Fahrenheit, Kelvin, Rankine, Reaumur, Newton and Romer

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

> In these two examples, we want to know the equivalent in Fahrenheit
> of 35º Celsius and 18.746º Celsius to Newton.

```python
from totemp import Celsius

temperature = Celsius.to_fahrenheit(35)  # Return: 95.0
```
```python
from totemp import Celsius

temperature = Celsius.to_newton(18.746)  # Return: 6.186179999999999
```

Note that **all returns are *float values***, and that **applies to all methods**.

## Versions

- 0.1.0:
  - Yanked, not functional
- 0.2.0:
  - Functional;
  - Can convert Celsius to Delisle, Fahrenheit, Kelvin, Newton, Rankine, Réaumur and Rømer.

## License

For more information, check LICENSE file.
