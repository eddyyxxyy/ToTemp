#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations

from abc import ABCMeta, abstractmethod
from typing import Any, ClassVar, TypeVar

T = TypeVar('T', bound='AbstractTemperature')


class AbstractTemperature(metaclass=ABCMeta):
    """
    Abstract base class for all temperature types.

    Attributes
    ----------

    _symbol : ClassVar[str]
        Official scale symbol.

    _value : float
        Temperature value (e.g. `36` or `-3.14`).

    Methods
    -------

    rounded()
        returns a new object of the same class with the value converted to int.

    to_celsius()
        returns a Celsius object which contains the converted value.

    to_fahrenheit()
        returns a Fahrenheit object which contains the converted value.

    to_delisle()
        returns a Delisle object which contains the converted value.

    to_kelvin()
        returns a Kelvin object which contains the converted value.

    to_newton()
        returns a Newton object which contains the converted value.

    to_rankine()
        returns a Rankine object which contains the converted value.

    to_reaumur()
        returns a Réaumur object which contains the converted value.

    to_romer()
        returns a Rømer object which contains the converted value.

    convert_to(temp_cls)
        returns an instance of `temp_cls` which contains the converted value.

    """

    _symbol: ClassVar[str]
    _value: float

    @classmethod
    def __init_subclass__(cls, **kwargs: object) -> None:
        """Ensures subclasses set the `_symbol` attribute."""
        super().__init_subclass__(**kwargs)
        try:
            _ = cls._symbol
        except AttributeError:
            raise AttributeError(
                'Temperature subclasses must set the `_symbol` class attribute'
            ) from None

    def __init__(self, value: float) -> None:
        self._value = value

    def __str__(self) -> str:
        return f'{self._value} {self._symbol}'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self._value})'

    def __add__(self: T, other: Any) -> T:
        """
        Returns a new instance of the same class with the sum of the values.

        If `other` is a temperature instance, it is first converted to the
        calling class, then the values are added.
        Otherwise, an attempt is made to add `other` to the value directly.
        """
        cls = self.__class__
        try:
            if isinstance(other, AbstractTemperature):
                return cls(self._value + other.convert_to(cls).value)
            return cls(self._value + other)
        except TypeError:
            return NotImplemented

    def __sub__(self: T, other: Any) -> T:
        """
        Returns a new instance of the same class with the subtraction of the values.

        If `other` is a temperature instance, it is first converted to the
        calling class, then the values are subtracted.
        Otherwise, an attempt is made to subtract `other` to the value directly.
        """
        cls = self.__class__
        try:
            if isinstance(other, AbstractTemperature):
                return cls(self._value - other.convert_to(cls).value)
            return cls(self._value - other)
        except TypeError:
            return NotImplemented

    def __mul__(self: T, other: Any) -> T:
        """
        Returns a new instance of the same class with the multiplication of the values.

        If `other` is a temperature instance, it is first converted to the
        calling class, then the values are multiplicated.
        Otherwise, an attempt is made to multiplicate `other` to the value directly.
        """
        cls = self.__class__
        try:
            if isinstance(other, AbstractTemperature):
                return cls(self._value * other.convert_to(cls).value)
            return cls(self._value * other)
        except TypeError:
            return NotImplemented

    def __pow__(self: T, other: Any) -> T:
        """
        Returns a new instance of the same class with the exponentiation of the values.

        If `other` is a temperature instance, it is first converted to the
        calling class, then the value is raised to the power of `other`.
        Otherwise, an attempt is made to raise the value field to the power of `other`.
        """
        cls = self.__class__
        try:
            if isinstance(other, AbstractTemperature):
                return cls(self._value ** other.convert_to(cls).value)
            return cls(self._value**other)
        except TypeError:
            return NotImplemented

    def __truediv__(self: T, other: Any) -> T:
        """
        Returns a new instance of the same class with the division of the values.

        If `other` is a temperature instance, it is first converted to the
        calling class, then the values are divided.
        Otherwise, an attempt is made to divide `other` to the value directly.
        """
        cls = self.__class__
        try:
            if isinstance(other, AbstractTemperature):
                return cls(self._value / other.convert_to(cls).value)
            return cls(self._value / other)
        except TypeError:
            return NotImplemented

    def __floordiv__(self: T, other: Any) -> T:
        """
        Returns a new instance of the same class with the floor division of the values.

        If `other` is a temperature instance, it is first converted to the
        calling class, then the values are divided and rounded.
        Otherwise, an attempt is made to floor divide `other` to the value directly.
        """
        cls = self.__class__
        try:
            if isinstance(other, AbstractTemperature):
                return cls(self._value // other.convert_to(cls).value)
            return cls(self._value // other)
        except TypeError:
            return NotImplemented

    def __mod__(self: T, other: Any) -> T:
        """
        Returns a new instance of the same class with the remainder from the division of the values.

        If `other` is a temperature instance, it is first converted to the
        calling class, then the values are divided.
        Otherwise, an attempt is made to use modulo operation on `other` to the value directly.
        """
        cls = self.__class__
        try:
            if isinstance(other, AbstractTemperature):
                return cls(self._value % other.convert_to(cls).value)
            return cls(self._value % other)
        except TypeError:
            return NotImplemented

    def __divmod__(self: T, other: Any) -> tuple[Any, Any]:
        """
        Returns a tuple of two new instances of the same class with the quotient and remainder.

        If `other` is a temperature instance, it is first converted to the
        calling class, then the values are divided.
        Otherwise, an attempt is made to use divmod operation between the
        calling class and `other` to the value directly.
        """
        cls = self.__class__
        try:
            if isinstance(other, AbstractTemperature):
                result = divmod(self._value, other.convert_to(cls).value)
                return cls(result[0]), cls(result[1])
            result = divmod(self._value, other)
            return cls(result[0]), cls(result[1])
        except TypeError:
            return NotImplemented

    def __radd__(self: T, other: Any) -> T:
        """
        Returns a new instance of the same class with the sum of the values.

        An attempt is made to add the value to the `other`.
        """
        cls = self.__class__
        try:
            return cls(other + self._value)
        except TypeError:
            return NotImplemented

    def __rsub__(self: T, other: Any) -> T:
        """
        Returns a new instance of the same class with the subtraction of the values.

        An attempt is made to subtract the value to the `other`.
        """
        cls = self.__class__
        try:
            return cls(other - self._value)
        except TypeError:
            return NotImplemented

    def __rmul__(self: T, other: Any) -> T:
        """
        Returns a new instance of the same class with the multiplication of the values.

        An attempt is made to multiply `other` by the value.
        """
        cls = self.__class__
        try:
            return cls(other * self._value)
        except TypeError:
            return NotImplemented

    def __rpow__(self: T, other: Any) -> T:
        """
        Returns a new instance of the same class with the exponentiation of the values.

        An attempt is made to raise `other` to the power of the value.
        """
        cls = self.__class__
        try:
            return cls(other**self._value)
        except TypeError:
            return NotImplemented

    def __rtruediv__(self: T, other: Any) -> T:
        """
        Returns a new instance of the same class with the division of the values.

        An attempt is made to divide the `other` by the value.
        """
        cls = self.__class__
        try:
            return cls(other / self._value)
        except TypeError:
            return NotImplemented

    def __rfloordiv__(self: T, other: Any) -> T:
        """
        Returns a new instance of the same class with the floor division of the values.

        An attempt is made to floor divide the value to `other`.
        """
        cls = self.__class__
        try:
            return cls(other // self._value)
        except TypeError:
            return NotImplemented

    def __rmod__(self: T, other: Any) -> T:
        """
        Returns a new instance of the same class with the remainder from the division of the values.

        An attempt is made to apply modulo between `other` and value.
        """
        cls = self.__class__
        try:
            return cls(other % self._value)
        except TypeError:
            return NotImplemented

    def __rdivmod__(self: T, other: Any) -> tuple[Any, Any]:
        """
        Returns a tuple of two new instances of the same class with the quotient and remainder.

        An attempt is made to apply divmod between the
        calling class and the value.
        """
        cls = self.__class__
        try:
            result = divmod(other, self._value)
            return cls(result[0]), cls(result[1])
        except TypeError:
            return NotImplemented

    def __abs__(self) -> AbstractTemperature:
        """Returns a new instance of the same class with the absolute of `value`"""
        cls = self.__class__
        return cls(abs(self._value))

    def __pos__(self) -> AbstractTemperature:
        """Returns a new instance of the same class with `+value`"""
        cls = self.__class__
        return cls(+self._value)

    def __neg__(self) -> AbstractTemperature:
        """Return a new instance of the same class with the negation of `value`"""
        cls = self.__class__
        return cls(-self._value)

    def __invert__(self) -> AbstractTemperature:
        """Return a new instance of the same class with bitwise NOT of `value`"""
        cls = self.__class__
        return cls(-self._value - 1)

    def __float__(self) -> float:
        """
        Returns a float of `value`.

        Returns
        -------
        _value : float
            float(self._value)

        """
        return float(self._value)

    def __int__(self) -> int:
        """
        Returns an int of `value`.

        Returns
        -------
        _value : float
            int(self._value)

        """
        return int(self._value)

    def __eq__(self, other) -> bool:
        """
        Checks if the values in the objects are equal and then returns a boolean.

        If `other` is a temperature instance, it is first converted to the
        calling class, then the objects are evaluated. That means: if `other`
        converted to the calling class has the same value, it returns True,
        otherwise it returns False.
        """
        cls = self.__class__
        try:
            if isinstance(other, AbstractTemperature):
                return self._value == other.convert_to(cls).value
            return self._value == other
        except TypeError:
            return NotImplemented

    def __lt__(self, other) -> bool:
        """
        Checks if the calling temperature object value is lesser than `other` and then returns a boolean.

        If `other` is a temperature instance, it is first converted to the
        calling class, then the objects are evaluated. That means: if `other`
        converted to the calling class has a greater value, it returns True,
        otherwise it returns False.
        """
        cls = self.__class__
        try:
            if isinstance(other, AbstractTemperature):
                return self._value < other.convert_to(cls).value
            return self._value < other
        except TypeError:
            return NotImplemented

    def __le__(self, other) -> bool:
        """
        Checks if the calling temperature object value is lesser or equal
        than `other` and then returns a boolean.

        If `other` is a temperature instance, it is first converted to the
        calling class, then the objects are evaluated. That means: if `other`
        converted to the calling class has a greater or equal value, it returns True,
        otherwise it returns False.
        """
        cls = self.__class__
        try:
            if isinstance(other, AbstractTemperature):
                return self._value <= other.convert_to(cls).value
            return self._value <= other
        except TypeError:
            return NotImplemented

    def __ne__(self, other) -> bool:
        """
        Checks if the calling temperature object value is different
        from `other` and then returns a boolean.

        If `other` is a temperature instance, it is first converted to the
        calling class, then the objects are evaluated. That means: if `other`
        converted to the calling class is different from `other`, it returns True,
        otherwise it returns False.
        """
        cls = self.__class__
        try:
            if isinstance(other, AbstractTemperature):
                return self._value != other.convert_to(cls).value
            return self._value != other
        except TypeError:
            return NotImplemented

    def __gt__(self, other) -> bool:
        """
        Checks if the calling temperature object value is greater
        than `other` and then returns a boolean.

        If `other` is a temperature instance, it is first converted to the
        calling class, then the objects are evaluated. That means: if `other`
        converted to the calling class is greater than `other`, it returns True,
        otherwise it returns False.
        """
        cls = self.__class__
        try:
            if isinstance(other, AbstractTemperature):
                return self._value > other.convert_to(cls).value
            return self._value > other
        except TypeError:
            return NotImplemented

    def __ge__(self, other) -> bool:
        """
        Checks if the calling temperature object value is greater
        or equal to `other` and then returns a boolean.

        If `other` is a temperature instance, it is first converted to the
        calling class, then the objects are evaluated. That means: if `other`
        converted to the calling class is greater or equal to `other`, it returns True,
        otherwise it returns False.
        """
        cls = self.__class__
        try:
            if isinstance(other, AbstractTemperature):
                return self._value >= other.convert_to(cls).value
            return self._value >= other
        except TypeError:
            return NotImplemented

    @property
    def value(self) -> float:
        """
        Returns temperature object value.

        Returns
        -------
        _value : float
            self._value
        """
        return self._value

    @value.setter
    def value(self, other: float) -> None:
        self._value = other

    @property
    def symbol(self) -> str:
        """
        Returns official scale symbol (read-only).

        Returns
        -------
        _symbol : str
            self._symbol
        """
        return self._symbol

    def rounded(self: T) -> T:
        """
        Returns the temperature object with converted value to int (rounded).

        Returns
        -------
        __class__(int(round(self._value))) : T
        """
        return self.__class__(int(round(self._value)))

    def to_celsius(self) -> Celsius:
        """
        Returns a Celsius object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        Returns
        -------
        convert_to(Celsius) : Celsius
        """
        return self.convert_to(Celsius)

    def to_fahrenheit(self) -> Fahrenheit:
        """
        Returns a Fahrenheit object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        Returns
        -------
        convert_to(Fahrenheit) : Fahrenheit
        """
        return self.convert_to(Fahrenheit)

    def to_delisle(self) -> Delisle:
        """
        Returns a Delisle object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        Returns
        -------
        convert_to(Delisle) : Delisle
        """
        return self.convert_to(Delisle)

    def to_kelvin(self) -> Kelvin:
        """
        Returns a Kelvin object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        Returns
        -------
        convert_to(Kelvin) : Kelvin
        """
        return self.convert_to(Kelvin)

    def to_newton(self) -> Newton:
        """
        Returns a Newton object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        Returns
        -------
        convert_to(Newton) : Newton
        """
        return self.convert_to(Newton)

    def to_rankine(self) -> Rankine:
        """
        Returns a Rankine object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        Returns
        -------
        convert_to(Rankine) : Rankine
        """
        return self.convert_to(Rankine)

    def to_reaumur(self) -> Reaumur:
        """
        Returns a Réaumur object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        Returns
        -------
        convert_to(Reaumur) : Reaumur
        """
        return self.convert_to(Reaumur)

    def to_romer(self) -> Romer:
        """
        Returns a Rømer object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        Returns
        -------
        convert_to(Rømer) : Rømer
        """
        return self.convert_to(Romer)

    @abstractmethod
    def convert_to(self, temp_cls: type[T]) -> T:
        """
        Returns an instance of `temp_cls` containing the converted value.

        If no conversion to `temp_cls` is possible, `TypeError` is raised.
        """
        ...


class Celsius(AbstractTemperature):
    """
    Class to represent Celsius temperature scale.

    Attributes
    ----------

    _symbol : str
        Celsius official scale symbol.

    _value : float
        Temperature value (e.g. `36` or `-3.14`).
    """

    _symbol = 'ºC'

    def convert_to(self, temp_cls: type[T]) -> T:
        if temp_cls is Celsius:
            return temp_cls(self._value)
        if temp_cls is Fahrenheit:
            return temp_cls(self._value * 9 / 5 + 32)
        if temp_cls is Delisle:
            return temp_cls((100 - self._value) * 3 / 2)
        if temp_cls is Kelvin:
            return temp_cls(self._value + 273.15)
        if temp_cls is Newton:
            return temp_cls(self._value * 33 / 100)
        if temp_cls is Rankine:
            return temp_cls((self._value + 273.15) * 9 / 5)
        if temp_cls is Reaumur:
            return temp_cls(self._value * 4 / 5)
        if temp_cls is Romer:
            return temp_cls(self._value * 21 / 40 + 7.5)
        raise TypeError


class Fahrenheit(AbstractTemperature):
    """
    Class to represent Fahrenheit temperature scale.

    Attributes
    ----------

    _symbol : str
        Fahrenheit official scale symbol.

    _value : float
        Temperature value (e.g. `36` or `-3.14`).
    """

    _symbol = 'ºF'

    def convert_to(self, temp_cls: type[T]) -> T:
        if temp_cls is Celsius:
            return temp_cls((self._value - 32) * 5 / 9)
        if temp_cls is Fahrenheit:
            return temp_cls(self._value)
        if temp_cls is Delisle:
            return temp_cls((212 - self._value) * 5 / 6)
        if temp_cls is Kelvin:
            return temp_cls((self._value + 459.67) * 5 / 9)
        if temp_cls is Newton:
            return temp_cls((self._value - 32) * 11 / 60)
        if temp_cls is Rankine:
            return temp_cls(self._value + 459.67)
        if temp_cls is Reaumur:
            return temp_cls((self._value - 32) * 4 / 9)
        if temp_cls is Romer:
            return temp_cls((self._value - 32) * (7 / 24) + 7.5)
        raise TypeError


class Delisle(AbstractTemperature):
    """
    Class to represent Delisle temperature scale.

    Attributes
    ----------

    _symbol : str
        Delisle official scale symbol.

    _value : float
        Temperature value (e.g. `36` or `-3.14`).
    """

    _symbol = 'ºDe'

    def convert_to(self, temp_cls: type[T]) -> T:
        if temp_cls is Celsius:
            return temp_cls(100 - self._value * 2 / 3)
        if temp_cls is Fahrenheit:
            return temp_cls(212 - self._value * 6 / 5)
        if temp_cls is Delisle:
            return temp_cls(self._value)
        if temp_cls is Kelvin:
            return temp_cls(373.15 - self._value * 2 / 3)
        if temp_cls is Newton:
            return temp_cls(33 - self._value * 11 / 50)
        if temp_cls is Rankine:
            return temp_cls(671.67 - self._value * 6 / 5)
        if temp_cls is Reaumur:
            return temp_cls(80 - self._value * 8 / 15)
        if temp_cls is Romer:
            return temp_cls(60 - self._value * 7 / 20)
        raise TypeError


class Kelvin(AbstractTemperature):
    """
    Class to represent Kelvin temperature scale.

    Attributes
    ----------

    _symbol : str
        Kelvin official scale symbol.

    _value : float
        Temperature value (e.g. `36` or `-3.14`).
    """

    _symbol = 'K'

    def convert_to(self, temp_cls: type[T]) -> T:
        if temp_cls is Celsius:
            return temp_cls(self._value - 273.15)
        if temp_cls is Fahrenheit:
            return temp_cls(self._value * 9 / 5 - 459.67)
        if temp_cls is Delisle:
            return temp_cls((373.15 - self._value) * 3 / 2)
        if temp_cls is Kelvin:
            return temp_cls(self._value)
        if temp_cls is Newton:
            return temp_cls((self._value - 273.15) * 33 / 100)
        if temp_cls is Rankine:
            return temp_cls(self._value * 1.8)
        if temp_cls is Reaumur:
            return temp_cls((self._value - 273.15) * 4 / 5)
        if temp_cls is Romer:
            return temp_cls((self._value - 273.15) * 21 / 40 + 7.5)
        raise TypeError


class Newton(AbstractTemperature):
    """
    Class to represent Newton temperature scale.

    Attributes
    ----------

    _symbol : str
        Newton official scale symbol.

    _value : float
        Temperature value (e.g. `36` or `-3.14`).
    """

    _symbol = 'ºN'

    def convert_to(self, temp_cls: type[T]) -> T:
        if temp_cls is Celsius:
            return temp_cls(self._value / 0.33)
        if temp_cls is Fahrenheit:
            return temp_cls(self._value * 60 / 11 + 32)
        if temp_cls is Delisle:
            return temp_cls((33 - self._value) * 50 / 11)
        if temp_cls is Kelvin:
            return temp_cls(self._value / 0.33000 + 273.15)
        if temp_cls is Newton:
            return temp_cls(self._value)
        if temp_cls is Rankine:
            return temp_cls(self._value * 60 / 11 + 491.67)
        if temp_cls is Reaumur:
            return temp_cls(self._value * 80 / 33)
        if temp_cls is Romer:
            return temp_cls(self._value * 35 / 22 + 7.5)
        raise TypeError


class Rankine(AbstractTemperature):
    """
    Class to represent Rankine temperature scale.

    Attributes
    ----------

    _symbol : str
        Rankine official scale symbol.

    _value : float
        Temperature value (e.g. `36` or `-3.14`).
    """

    _symbol = 'ºR'

    def convert_to(self, temp_cls: type[T]) -> T:
        if temp_cls is Celsius:
            return temp_cls((self._value - 491.67) * 5 / 9)
        if temp_cls is Fahrenheit:
            return temp_cls(self._value - 459.67)
        if temp_cls is Delisle:
            return temp_cls((671.67 - self._value) * 5 / 6)
        if temp_cls is Kelvin:
            return temp_cls(self._value * 5 / 9)
        if temp_cls is Newton:
            return temp_cls((self._value - 491.67) * 11 / 60)
        if temp_cls is Rankine:
            return temp_cls(self._value)
        if temp_cls is Reaumur:
            return temp_cls((self._value - 491.67) * 4 / 9)
        if temp_cls is Romer:
            return temp_cls((self._value - 491.67) * 7 / 24 + 7.5)
        raise TypeError


class Reaumur(AbstractTemperature):
    """
    Class to represent Réaumur temperature scale.

    Attributes
    ----------

    _symbol : str
        Réaumur official scale symbol.

    _value : float
        Temperature value (e.g. `36` or `-3.14`).
    """

    _symbol = 'ºRé'

    def convert_to(self, temp_cls: type[T]) -> T:
        if temp_cls is Celsius:
            return temp_cls(self._value * 5 / 4)
        if temp_cls is Fahrenheit:
            return temp_cls(self._value * 9 / 4 + 32)
        if temp_cls is Delisle:
            return temp_cls((80 - self._value) * 15 / 8)
        if temp_cls is Kelvin:
            return temp_cls(self._value * 5 / 4 + 273.15)
        if temp_cls is Newton:
            return temp_cls(self._value * 33 / 80)
        if temp_cls is Rankine:
            return temp_cls(self._value * 9 / 4 + 491.67)
        if temp_cls is Reaumur:
            return temp_cls(self._value)
        if temp_cls is Romer:
            return temp_cls(self._value * 21 / 32 + 7.5)
        raise TypeError


class Romer(AbstractTemperature):
    """
    Class to represent Rømer temperature scale.

    Attributes
    ----------

    _symbol : str
        Rømer official scale symbol.

    _value : float
        Temperature value (e.g. `36` or `-3.14`).
    """

    _symbol = 'ºRø'

    def convert_to(self, temp_cls: type[T]) -> T:
        if temp_cls is Celsius:
            return temp_cls((self._value - 7.5) * 40 / 21)
        if temp_cls is Fahrenheit:
            return temp_cls((self._value - 7.5) * 24 / 7 + 32)
        if temp_cls is Delisle:
            return temp_cls((60 - self._value) * 20 / 7)
        if temp_cls is Kelvin:
            return temp_cls((self._value - 7.5) * 40 / 21 + 273.15)
        if temp_cls is Newton:
            return temp_cls((self._value - 7.5) * 22 / 35)
        if temp_cls is Rankine:
            return temp_cls((self._value - 7.5) * 24 / 7 + 491.67)
        if temp_cls is Reaumur:
            return temp_cls((self._value - 7.5) * 32 / 21)
        if temp_cls is Romer:
            return temp_cls(self._value)
        raise TypeError
