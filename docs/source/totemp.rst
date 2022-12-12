ToTemp Module
=============

Classes to represent temperature scale objects, providing
arithmetic and comparison operations between them.

Base class
**********

**All classes inherit from this one.**

.. autoclass:: totemp.temperature_types.AbstractTemperature
   :special-members: __init_subclass__,__add__
   :show-inheritance:
   :member-order: bysource

Temperature Classes
*******************

All **temperature objects inherit a convertion to itself** that
**when called it will always return the same object** (and that's
why those methods aren't included here in each class doc).

The **symbol property is read-only** and different for each
class.

.. autoclass:: totemp.Celsius
   :members: symbol,value,rounded,to_delisle,to_fahrenheit,to_kelvin,to_newton,to_rankine,to_reaumur,to_romer,convert_to
   :undoc-members:
   :show-inheritance:
   :member-order: bysource

.. autoclass:: totemp.Fahrenheit
   :members: symbol,value,rounded,to_celsius,to_delisle,to_kelvin,to_newton,to_rankine,to_reaumur,to_romer,convert_to
   :undoc-members:
   :show-inheritance:
   :member-order: bysource

.. autoclass:: totemp.Delisle
   :members: symbol,value,rounded,to_celsius,to_fahrenheit,to_kelvin,to_newton,to_rankine,to_reaumur,to_romer,convert_to
   :undoc-members:
   :show-inheritance:
   :member-order: bysource

.. autoclass:: totemp.Kelvin
   :members: symbol,value,rounded,to_celsius,to_fahrenheit,to_delisle,to_newton,to_rankine,to_reaumur,to_romer,convert_to
   :undoc-members:
   :show-inheritance:
   :member-order: bysource

.. autoclass:: totemp.Newton
   :members: symbol,value,rounded,to_celsius,to_fahrenheit,to_delisle,to_kelvin,to_rankine,to_reaumur,to_romer,convert_to
   :undoc-members:
   :show-inheritance:
   :member-order: bysource

.. autoclass:: totemp.Rankine
   :members: symbol,value,rounded,to_celsius,to_fahrenheit,to_delisle,to_kelvin,to_newton,to_reaumur,to_romer,convert_to
   :undoc-members:
   :show-inheritance:
   :member-order: bysource

.. autoclass:: totemp.Reaumur
   :members: symbol,value,rounded,to_celsius,to_fahrenheit,to_delisle,to_kelvin,to_newton,to_rankine,to_romer,convert_to
   :undoc-members:
   :show-inheritance:
   :member-order: bysource

.. autoclass:: totemp.Romer
   :members: symbol,value,rounded,to_celsius,to_fahrenheit,to_delisle,to_kelvin,to_newton,to_rankine,to_reaumur,convert_to
   :undoc-members:
   :show-inheritance:
   :member-order: bysource
