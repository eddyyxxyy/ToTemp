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

.. code:: Python

    from totemp import Celsius, Fahrenheit

    if __name__ == '__main__':
        temps: list = [Celsius(12), Celsius(25), Celsius(50)]
        print(temps[0])
        print(temps)

        temps = list(map(Fahrenheit.to_fahrenheit, temps))
        print(temps[0])
        print(temps)
