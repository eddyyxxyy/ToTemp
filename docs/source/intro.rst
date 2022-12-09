Introduction
============

``ToTemp`` API is a high-level OO Python package which aims to provide an easy and intuitive way to represent temperature
scales and convert/operate over them with precise/aproximated values.

In essence, this package is made for research and academic porpuses, since I
(`Edson <https://github.com/eddyyxxyy>`_) haven't found any "good, interesting and functional" enough package
to work with temperature scales.

The aim here was to define dynamic objects which would allow users/developers to perform the operations performed with
ease and precision, without worrying about the calculations needed to convert temperature scales, providing them the
option to get precise and rounded values to their operations.

The current implementation has been developed for Python 3.10/3.11 (since it uses new syntax and features from available
in those releases).

Limitations
***********

As my main use-case scenario was to operate over diverse temperature scales, the current version of
:doc:`ToTemp<totemp>` has been designed to support operations between these Classes:

- `Celsius </ToTemp/docs/build/html/totemp.html#totemp.Celsius>`_
- `Fahrenheit </ToTemp/docs/build/html/totemp.html#totemp.Fahrenheit>`_
- `Delisle </ToTemp/docs/build/html/totemp.html#totemp.Delisle>`_
- `Kelvin </ToTemp/docs/build/html/totemp.html#totemp.Kelvin>`_
- `Newton </ToTemp/docs/build/html/totemp.html#totemp.Newton>`_
- `Rankine </ToTemp/docs/build/html/totemp.html#totemp.Rankine>`_
- `Réaumur </ToTemp/docs/build/html/totemp.html#totemp.Reaumur>`_
- `Rømer </ToTemp/docs/build/html/totemp.html#totemp.Romer>`_

For usage information and example code, go to :doc:`Installation and Usage <installation>`.
