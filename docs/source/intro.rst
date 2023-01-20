Introduction
============

``ToTemp`` as an high-level OO Python package, aims to provide an easy and intuitive way to represent temperature
scales and convert/operate over them with precise/aproximated values.

In essence, this package is made for research and academic porpuses, since I
(`Edson <https://github.com/eddyyxxyy>`_) haven't found any "good, interesting and functional" enough package
to work with temperature scales.

.. note:: For usage information and example code, go to :doc:`Installation and Usage <installation_usage>`.

The goal here was to define dynamic objects which would allow users/developers to perform the operations with ease and
precision, without worrying about the calculations needed to convert temperature scales, providing them the option to
get precise and rounded values to their operations.

The current implementation has been developed for Python ^3.10 (since it uses new syntax and features from available
in those releases).

Limitations
***********

As my main use-case scenario was to operate over diverse temperature scales, the current version of
:doc:`ToTemp<totemp>` has been designed to support operations between these Classes:

- :meth:`Celsius<totemp.Celsius>`
- :meth:`Fahrenheit<totemp.Fahrenheit>`
- :meth:`Delisle<totemp.Delisle>`
- :meth:`Kelvin<totemp.Kelvin>`
- :meth:`Newton<totemp.Newton>`
- :meth:`Rankine<totemp.Rankine>`
- :meth:`Réaumur<totemp.Reaumur>`
- :meth:`Rømer<totemp.Romer>`

And all those classes inherits from the :meth:`Base Class<totemp.temperature_types.AbstractTemperature>`.
