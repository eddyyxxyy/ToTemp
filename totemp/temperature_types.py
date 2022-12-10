#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations
from abc import ABCMeta, abstractmethod
from typing import Any, ClassVar, TypeVar


T = TypeVar("T", bound="AbstractTemperature")


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
                "Temperature subclasses must set the `_symbol` class attribute"
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

    @property
    def value(self) -> float:
        return self._value

    @value.setter
    def value(self, other: float) -> None:
        self._value = other

    @property
    def symbol(self) -> str:
        return self._symbol

    def rounded(self: T) -> T:
        return self.__class__(int(round(self._value)))

    def to_celsius(self) -> Celsius:
        return self.convert_to(Celsius)

    def to_fahrenheit(self) -> Fahrenheit:
        return self.convert_to(Fahrenheit)

    def to_delisle(self) -> Delisle:
        return self.convert_to(Delisle)

    def to_kelvin(self) -> Kelvin:
        return self.convert_to(Kelvin)

    def to_newton(self) -> Newton:
        return self.convert_to(Newton)

    def to_rankine(self) -> Rankine:
        return self.convert_to(Rankine)

    def to_reaumur(self) -> Reaumur:
        return self.convert_to(Reaumur)

    def to_romer(self) -> Romer:
        return self.convert_to(Romer)

    @abstractmethod
    def convert_to(self, temp_cls: type[T]) -> T:
        """
        Returns an instance of `temp_cls` containing the converted value.

        If no conversion to `temp_cls` is possible, `TypeError` is raised.
        """
        ...


class Celsius(AbstractTemperature):
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
