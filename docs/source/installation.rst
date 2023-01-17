Installation and Usage
======================

Installation
************

Install the package (or add it to your ``requirements.txt`` file):

.. code:: console

    $ pip install totemp

Or, in poetry environments:

.. code:: console

    $ poetry add totemp

Basic Usage and Representation
******************************

When working with temperature scales representations and
convertions, we often see a lack of "straight to the point"
solutions beside of searching online for every single
mathematical formula.

In that sense, everytime `I <https://github.com/eddyyxxyy>`_ tried
to represent those temperatures (using packages or implementing my
own code) to automate any calculation/operation/representation, I
was often stuck with little to none precise and simple way of doing
it.

This package aims to bring the simple and straight to the point,
but precise, Object Oriented experience of working with temperature
data types.

**For example, this**:

    .. code-block:: Python
        :linenos:
        :emphasize-lines: 5,6,10,11,15,16,17,18,22,23,27,28

        from totemp import Celsius, Fahrenheit, Kelvin, Delisle

        if __name__ == '__main__':
            temps: list = [Celsius(12), Celsius(25), Celsius(50)]
            print(temps[0])
            print(temps)

            # Converts all Celsius objects using to_fahrenheit() method
            temps = list(map(Celsius.to_fahrenheit, temps))
            print(temps[0])
            print(temps)

            # Unpacks the temperature objects list
            temp0, temp1, temp2 = temps
            print(temp0.__repr__())
            print(temp0.__str__())
            print(temp0.value)
            print(temp0.symbol)

            # Converts to Kelvin and then rounds the value
            temp1 = temp1.to_kelvin()
            print(temp1)
            print(temp1.rounded())

            # Converts to Delisle
            temp2 = temp2.to_delisle().rounded()
            print(type(temp2))
            print(type(temp2.value), f'-> {temp2.value}')

**Outputs**:

    From line 5 and 10::

        >>> '12 ºC'
        >>> '53.6 ºF'

        Calls to the __str__ method of the temperature object returns
        "`value`º `symbol`". That means that every call that need string
        representations of the temperature (such as print(), str() or
        `object`.__str__()) returns the value and its official symbol.

    From line 6 and 11::

        >>> [Celsius(12), Celsius(25), Celsius(50)]
        >>> [Fahrenheit(53.6), Fahrenheit(77.0), Fahrenheit(122.0)]

        And here we can see the "real representation" of the objects,
        shown by **__repr__** special method, that specifies its nature
        (like which scale it is and it's value, and we can create a "new"
        object with those representations).

    From line 15, 16, 17 and 18::

        >>> 'Fahrenheit(53.6)'  # __repr__()
        >>> '53.6 ºF'  # __str__()
        >>> 53.6  # `value` property
        >>> 'ºF'  # Official `symbol` property

        Both special methods and the symbol property returns
        strings, but value is numeric, a float.

    From line 22 and 23::

        >>> 298.15000000000003 K
        >>> 298 K

        Here we can see the calculation precision and the
        simplicity to make the result to be rounded, to
        become an aproximate int value.

    From line 27 and 28::

        >>> <class 'totemp.temperature_types.Delisle'>
        >>> <class 'int'> -> 75

        And now we have two type outputs, the first one is
        the type of the temp2 object and the type of its value.
