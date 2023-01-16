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

Usage
*****

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
        :emphasize-lines: 5,6,10,11

        from totemp import Celsius, Fahrenheit

        if __name__ == '__main__':
            temps: list = [Celsius(12), Celsius(25), Celsius(50)]
            print(temps[0])
            print(temps)

            # Converts all Celsius objects using to_fahrenheit() method
            temps = list(map(Celsius.to_fahrenheit, temps))
            print(temps[0])
            print(temps)

**Outputs**:

    From line 5 and 10::

        >>> 12º C
        >>> 53.6 ºF

        Every print() or str() calls to the __str__ method of the temperature object.
        That means that every call that need string representations of the temperature
        returns the value and its official symbol (e.g. `value`º `symbol`).

    From line 6 and 11::

        >>> [Celsius(12), Celsius(25), Celsius(50)]
        >>> [Fahrenheit(53.6), Fahrenheit(77.0), Fahrenheit(122.0)]

        Introduce explanation here.
