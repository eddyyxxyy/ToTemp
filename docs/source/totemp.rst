ToTemp Module
=============

Classes to represent temperature scale objects, providing
arithmetic and comparison operations between them.

Base Class
**********

**All classes inherit from this one.** Here are all of the special and common methods docs.

.. autoclass:: totemp.temperature_types.AbstractTemperature
   :special-members: rounded,convert_to,__add__,__sub__,__mul__,__pow__,__truediv__,__floordiv__,__mod__,__pos__,__neg__,__invert__,__eq__,__lt__,__le__,__ne__,__gt__,__ge__,__divmod__,__radd__,__rsub__,__rmul__,__rpow__,__rtruediv__,__rfloordiv__,__rmod__,__rdivmod__,__abs__,__float__,__int__,__round__,__floor__,__ceil__,__trunc__,__str__,__repr__
   :show-inheritance:
   :member-order: bysource

Temperature Classes
*******************

All **temperature objects inherit a conversion to itself** that
**when called it will always return the same object** (and that's
why those methods aren't included here in each class doc).

.. note::
   The **symbol property is read-only** and different for each class.

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
