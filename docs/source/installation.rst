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

.. note::
    The `Base Class </ToTemp/docs/build/html/totemp.html#totemp.base-class>`_ is the center of
    attentions here, for all the detailed information go check every single method, property and
    other implementations there.

When working with temperature scales representations and
convertions, we often see a lack of "straight to the point"
solutions beside of searching online for every single
mathematical formula.

In that sense, everytime I (`Edson <https://github.com/eddyyxxyy>`_) tried
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


Arithmetic and comparison operations
************************************

Now we can look at the really interesting part of working
with ToTemp temperature objects: **perform operations between
temperature data types and its iterations with other numeric
data types**.

Let's go **straight to it**:

    .. code-block:: Python
        :linenos:
        :emphasize-lines: 1,4,6,12

        import totemp as tp

        if __name__ == '__main__':
            temp0, temp1 = tp.Celsius(0), tp.Fahrenheit(32)

            # Celsius(0) > Fahrenheit(32)
            if temp0 > temp1:
                print(f'`temp0`->{temp0} is greater than `temp1`->{temp1}')
            elif temp0 < temp1:
                print(f'`temp0`->{temp0} is not greater than `temp1`->{temp1}')
            else:
                print('What...is...happening...?')


**Outputs**:

    From line 12::

        >>> What...is...happening...?

As you are probably thinking:

    - *this doesn't make sense*... **or it does**?

When doing comparisons between temperature data types what are
we trying to achieve? To check if the objects "are the same" or to
check if the values equivalent? Or one is greater/lesser than another?

For example, *comparing int(1) == float(1)* would **return True**,
and that's exactly what's happening in our temperature comparision.

The *__gt__* special method (and most of the other comparision and arithmetic
special methods) checks if the object being compared to the calling class is an
Temperature Type or a float/integer, if `other` is a Temperature, it attempts to
convert the other object to the calling class and then return the result of the
evaluation (to be printed, in our case).

Another example, with the same objects:

    .. code-block:: Python
        :linenos:
        :emphasize-lines: 6,7,9,11,13,15,17,19

        import totemp as tp

        if __name__ == '__main__':
            temp0, temp1 = tp.Celsius(0), tp.Fahrenheit(32)

            print(f'temp0: {repr(temp0)}')
            print(f'temp1: {repr(temp1.to_celsius())}')

            print(temp0 > temp1)

            print(temp0 < temp1)

            print(temp0 == temp1)

            print(temp0 != temp1)

            print(temp0 >= temp1)

            print(temp0 <= temp1)

.. note::
    Using *repr()* just for better visualization

**Outputs**:

    From lines 6 and 7::

        >>> temp0: Celsius(0)
        >>> temp1: Celsius(0.0)

        The comparision/arithmetic implementation attempts to convert the value
        of other and then evaluate them.

        That meaning:
        `temp0` > `temp1.` is the same as `temp0` > `temp1.to_celsius()`

        The values being compared here are the equivalent values already converted!
        All that because of the calling class, `temp0` is an Celsius instance, so it
        will trigger a convertion of `other` to be compared with after.

    From lines 9 and 11::

        >>> False
        >>> False

        The value of `temp0` isn't greater or lesser than `other` value, it is equal.

    From lines 13 and 15::

        >>> True
        >>> False

        After the convertion of `temp1` (Celsius(0.0)) we could see that `temp1`
        has the same value, or better saying, has equivalent value to `temp0`.

    From lines 17 and 19::

        >>> True
        >>> True

        And, as we saw in the previous outputs (from lines 13 and 15), comparisions
        that declare ">=" or "<=" would return True in that case, even though they
        aren't greater or lesser than each other, they are indeed equivalents.


After understanding how comparisions are done, we can now see
how the arithmetic operations work.

**Look at this**:

    .. code-block:: Python
        :linenos:
        :emphasize-lines: 1,7,13,14

        from totemp import Newton, Rankine

        if __name__ == '__main__':
            temp0 = Newton(33)
            temp1 = Rankine(671.67)

            temp2 = temp0 + temp1

            print('`temp2`:', temp2)
            print('`temp2`:', repr(temp2))
            print('`temp2`:', temp2.value, temp2.symbol)

            print((temp0 + temp1).rounded())
            print(repr((temp0 + temp1).rounded()))

**Outputs**:

    From lines 9, 10 and 11::

        >>> `temp2`: 65.99999999999999 ºN
        >>> `temp2`: Newton(65.99999999999999)
        >>> `temp2`: 65.99999999999999 ºN

        Just as the comparisions, most of the arithmetic operations
        that can be performed by the objects attempts to convert `other`
        to the same type as the calling class (in this case, to Newton).

    From line 13 and 14::

        >>> 66 ºN
        >>> Newton(66)

        And, if needed, we can work with aproximate results too,
        we could aproximate just the values of `temp0` or `temp1`,
        none of them or even both before the operation actually
        happen.

        The thing is that every object can work as an aproximate or
        precise value of itself to perform more "embracing" operations,
        that the limits are mostly the way the developer/user is using
        it.

So, with that said, we can already assume that the
