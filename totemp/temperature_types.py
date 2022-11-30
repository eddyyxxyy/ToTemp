#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from dataclasses import dataclass
from math import trunc
from typing import Generic, TypeVar

TEMP = TypeVar('TEMP', int, float)


@dataclass
class Celsius(Generic[TEMP]):
    """
    A Dataclass that represents Celsius temperature scale
    and provides conversions to other temperature scales.

    ...

    Attributes
    ----------
    value: int | float
        temperature value (e.g. 36ºC)

    Methods
    -------
    precise():
        returns the Celsius object with value converted to float.
    rounded():
        returns the Celsius object with value converted to int (rounded).
    to_fahrenheit():
        returns a Fahrenheit object which contains the converted value.
    to_delisle():
        returns a Delisle object which contains the converted value.
    to_kelvin():
        returns a Kelvin object which contains the converted value.
    to_newton():
        returns a Newton object which contains the converted value.
    to_rankine():
        returns a Rankine object which contains the converted value.
    to_reaumur():
        returns a Réaumur object which contains the converted value.
    to_romer():
        returns a Rømer object which contains the converted value.
    """

    value: TEMP

    def precise(self) -> 'Celsius[float]':
        """
        Returns a Celsius object with float value.

        :return: Celsius Object
        """
        return Celsius(float(self.value))

    def rounded(self) -> 'Celsius[int]':
        """
        Returns a Celsius object with int (rounded) value.

        :return: Celsius Object
        """
        return Celsius(round(self.value))

    def to_fahrenheit(self) -> 'Fahrenheit[TEMP]':
        """
        Returns a Fahrenheit object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        :return: Fahrenheit object
        """
        fahrenheit = type(self.value)(self.value * 9 / 5 + 32)
        return Fahrenheit(fahrenheit)

    def to_delisle(self) -> 'Delisle[TEMP]':
        """
        Returns a Delisle object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        :return: Delisle object
        """
        delisle = type(self.value)(self.value * 1.5000 - 100.00)
        return Delisle(delisle)

    def to_kelvin(self) -> 'Kelvin[TEMP]':
        """
        Returns a Kelvin object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        :return: Kelvin object
        """
        kelvin = type(self.value)(self.value + 273.15)
        return Kelvin(kelvin)

    def to_newton(self) -> 'Newton[TEMP]':
        """
        Returns a Newton object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        :return: Newton object
        """
        newton = type(self.value)(self.value * 33 / 100)
        return Newton(newton)

    def to_rankine(self) -> 'Rankine[TEMP]':
        """
        Returns a Rankine object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        :return: Rankine object
        """
        rankine = type(self.value)(self.value * 9 / 5 + 491.67)
        return Rankine(rankine)

    @staticmethod
    def to_reaumur(celsius: float | int, /, *, float_ret=True) -> float | int:
        """
        Converts Celsius to Réaumur, returning a float by default.

        If the float_ret parameter is False, it returns an approximate int value
        (using the math's module trunc function).

        :param celsius: Celsius value to be converted
        :param float_ret: Optional, True by default to return floats
        :return: float or int
        """
        if float_ret:
            return float(celsius * 4 / 5)
        return trunc(celsius * 4 / 5)

    @staticmethod
    def to_romer(celsius: float | int, /, *, float_ret=True) -> float | int:
        """
        Converts Celsius to Rømer, returning a float by default.

        If the float_ret parameter is False, it returns an approximate int value
        (using the math's module trunc function).

        :param celsius: Celsius value to be converted
        :param float_ret: Optional, True by default to return floats
        :return: float or int
        """
        if float_ret:
            return float(celsius * 21 / 40 + 7.5)
        return trunc(celsius * 21 / 40 + 7.5)


@dataclass
class Fahrenheit(Generic[TEMP]):
    """
    A Dataclass that represents Fahrenheit temperature scale
    and provides conversions to other temperature scales.

    ...

    Attributes
    ----------
    value: int | float
        temperature value (e.g. 36ºF)

    Methods
    -------
    precise():
        returns the Fahrenheit object with value converted to float.
    rounded():
        returns the Fahrenheit object with value converted to int (rounded).
    to_celsius():
        returns a Celsius object which contains the converted value.
    to_delisle():
        returns a Delisle object which contains the converted value.
    to_kelvin():
        returns a Kelvin object which contains the converted value.
    to_newton():
        returns a Newton object which contains the converted value.
    to_rankine():
        returns a Rankine object which contains the converted value.
    to_reaumur():
        returns a Réaumur object which contains the converted value.
    to_romer():
        returns a Rømer object which contains the converted value.
    """

    value: TEMP

    def precise(self) -> 'Fahrenheit[float]':
        """
        Returns a Fahrenheit object with float value.

        :return: Fahrenheit Object
        """
        return Fahrenheit(float(self.value))

    def rounded(self) -> 'Fahrenheit[int]':
        """
        Returns a Fahrenheit object with int (rounded) value.

        :return: Fahrenheit Object
        """
        return Fahrenheit(round(self.value))

    @staticmethod
    def to_celsius(
        fahrenheit: float | int, /, *, float_ret=True
    ) -> float | int:
        """
        Converts Fahrenheit to Celsius, returning a float by default.

        If the float_ret parameter is False, it returns an approximate int value
        (using the math's module trunc function).

        :param fahrenheit: Fahrenheit value to be converted
        :param float_ret: Optional, True by default to return floats
        :return: float or int
        """
        if float_ret:
            return float((fahrenheit - 32) * 5 / 9)
        return trunc((fahrenheit - 32) * 5 / 9)

    @staticmethod
    def to_delisle(
        fahrenheit: float | int, /, *, float_ret=True
    ) -> float | int:
        """
        Converts Fahrenheit to Delisle, returning a float by default.

        If the float_ret parameter is False, it returns an approximate int value
        (using the math's module trunc function).

        :param fahrenheit: Fahrenheit value to be converted
        :param float_ret: Optional, True by default to return floats
        :return: float or int
        """
        if float_ret:
            return float((212 - fahrenheit) * 5 / 6)
        return trunc((212 - fahrenheit) * 5 / 6)

    @staticmethod
    def to_kelvin(
        fahrenheit: float | int, /, *, float_ret=True
    ) -> float | int:
        """
        Converts Fahrenheit to Kelvin, returning a float by default.

        If the float_ret parameter is False, it returns an approximate int value
        (using the math's module trunc function).

        :param fahrenheit: Fahrenheit value to be converted
        :param float_ret: Optional, True by default to return floats
        :return: float or int
        """
        if float_ret:
            return float((fahrenheit + 459.67) * 5 / 9)
        return trunc((fahrenheit + 459.67) * 5 / 9)

    @staticmethod
    def to_newton(
        fahrenheit: float | int, /, *, float_ret=True
    ) -> float | int:
        """
        Converts Fahrenheit to Newton, returning a float by default.

        If the float_ret parameter is False, it returns an approximate int value
        (using the math's module trunc function).

        :param fahrenheit: Fahrenheit value to be converted
        :param float_ret: Optional, True by default to return floats
        :return: float or int
        """
        if float_ret:
            return float((fahrenheit - 32) * 11 / 60)
        return trunc((fahrenheit - 32) * 11 / 60)

    @staticmethod
    def to_rankine(
        fahrenheit: float | int, /, *, float_ret=True
    ) -> float | int:
        """
        Converts Fahrenheit to Rankine, returning a float by default.

        If the float_ret parameter is False, it returns an approximate int value
        (using the math's module trunc function).

        :param fahrenheit: Fahrenheit value to be converted
        :param float_ret: Optional, True by default to return floats
        :return: float or int
        """
        if float_ret:
            return float(fahrenheit + 459.67)
        return trunc(fahrenheit + 459.67)

    @staticmethod
    def to_reaumur(
        fahrenheit: float | int, /, *, float_ret=True
    ) -> float | int:
        """
        Converts Fahrenheit to Réaumur, returning a float by default.

        If the float_ret parameter is False, it returns an approximate int value
        (using the math's module trunc function).

        :param fahrenheit: Fahrenheit value to be converted
        :param float_ret: Optional, True by default to return floats
        :return: float or int
        """
        if float_ret:
            return float((fahrenheit - 32) * 4 / 9)
        return trunc((fahrenheit - 32) * 4 / 9)

    @staticmethod
    def to_romer(fahrenheit: float | int, /, *, float_ret=True) -> float | int:
        """
        Converts Fahrenheit to Rømer, returning a float by default.

        If the float_ret parameter is False, it returns an approximate int value
        (using the math's module trunc function).

        :param fahrenheit: Fahrenheit value to be converted
        :param float_ret: Optional, True by default to return floats
        :return: float or int
        """
        if float_ret:
            return float((fahrenheit - 32) * (7 / 24) + 7.5)
        return trunc((fahrenheit - 32) * (7 / 24) + 7.5)


@dataclass
class Delisle(Generic[TEMP]):
    """
    A Dataclass that represents Delisle temperature scale
    and provides conversions to other temperature scales.

    ...

    Attributes
    ----------
    value: int | float
        temperature value (e.g. 36ºDe)

    Methods
    -------
    precise():
        returns the Delisle object with value converted to float.
    rounded():
        returns the Delisle object with value converted to int (rounded).
    to_celsius():
        returns a Celsius object which contains the converted value.
    to_fahrenheit():
        returns a Fahrenheit object which contains the converted value.
    to_kelvin():
        returns a Kelvin object which contains the converted value.
    to_newton():
        returns a Newton object which contains the converted value.
    to_rankine():
        returns a Rankine object which contains the converted value.
    to_reaumur():
        returns a Réaumur object which contains the converted value.
    to_romer():
        returns a Rømer object which contains the converted value.
    """

    value: TEMP

    def precise(self) -> 'Delisle[float]':
        """
        Returns a Delisle object with float value.

        :return: Delisle Object
        """
        return Delisle(float(self.value))

    def rounded(self) -> 'Delisle[int]':
        """
        Returns a Delisle object with int (rounded) value.

        :return: Delisle Object
        """
        return Delisle(round(self.value))

    @staticmethod
    def to_celsius(delisle: float | int, /, *, float_ret=True) -> float | int:
        """
        Converts Delisle to Celsius, returning a float by default.

        If the float_ret parameter is False, it returns an approximate int value
        (using the math's module trunc function).

        :param delisle: Delisle value to be converted
        :param float_ret: Optional, True by default to return floats
        :return: float or int
        """
        if float_ret:
            return float(100 - delisle * 2 / 3)
        return trunc(100 - delisle * 2 / 3)

    @staticmethod
    def to_fahrenheit(
        delisle: float | int, /, *, float_ret=True
    ) -> float | int:
        """
        Converts Delisle to Fahrenheit, returning a float by default.

        If the float_ret parameter is False, it returns an approximate int value
        (using the math's module trunc function).

        :param delisle: Delisle value to be converted
        :param float_ret: Optional, True by default to return floats
        :return: float or int
        """
        if float_ret:
            return float(212 - delisle * 6 / 5)
        return trunc(212 - delisle * 6 / 5)

    @staticmethod
    def to_kelvin(delisle: float | int, /, *, float_ret=True) -> float | int:
        """
        Converts Delisle to Kelvin, returning a float by default.

        If the float_ret parameter is False, it returns an approximate int value
        (using the math's module trunc function).

        :param delisle: Delisle value to be converted
        :param float_ret: Optional, True by default to return floats
        :return: float or int
        """
        if float_ret:
            return float(373.15 - (delisle * 2 / 3))
        return trunc(373.15 - (delisle * 2 / 3))

    @staticmethod
    def to_newton(delisle: float | int, /, *, float_ret=True) -> float | int:
        """
        Converts Delisle to Newton, returning a float by default.

        If the float_ret parameter is False, it returns an approximate int value
        (using the math's module trunc function).

        :param delisle: Delisle value to be converted
        :param float_ret: Optional, True by default to return floats
        :return: float or int
        """
        if float_ret:
            return float(33 - delisle * 11 / 50)
        return trunc(33 - delisle * 11 / 50)

    @staticmethod
    def to_rankine(delisle: float | int, /, *, float_ret=True) -> float | int:
        """
        Converts Delisle to Rankine, returning a float by default.

        If the float_ret parameter is False, it returns an approximate int value
        (using the math's module trunc function).

        :param delisle: Delisle value to be converted
        :param float_ret: Optional, True by default to return floats
        :return: float or int
        """
        if float_ret:
            return float(671.67 - delisle * 6 / 5)
        return trunc(671.67 - delisle * 6 / 5)

    @staticmethod
    def to_reaumur(delisle: float | int, /, *, float_ret=True) -> float | int:
        """
        Converts Delisle to Réaumur, returning a float by default.

        If the float_ret parameter is False, it returns an approximate int value
        (using the math's module trunc function).

        :param delisle: Delisle value to be converted
        :param float_ret: Optional, True by default to return floats
        :return: float or int
        """
        if float_ret:
            return float(80 - delisle * 8 / 15)
        return trunc(80 - delisle * 8 / 15)

    @staticmethod
    def to_romer(delisle: float | int, /, *, float_ret=True) -> float | int:
        """
        Converts Delisle to Rømer, returning a float by default.

        If the float_ret parameter is False, it returns an approximate int value
        (using the math's module trunc function).

        :param delisle: Delisle value to be converted
        :param float_ret: Optional, True by default to return floats
        :return: float or int
        """
        if float_ret:
            return float(60 - delisle * 7 / 20)
        return trunc(60 - delisle * 7 / 20)


@dataclass
class Kelvin(Generic[TEMP]):
    """
    A Dataclass that represents Kelvin temperature scale
    and provides conversions to other temperature scales.

    ...

    Attributes
    ----------
    value: int | float
        temperature value (e.g. 36ºK)

    Methods
    -------
    precise():
        returns the Kelvin object with value converted to float.
    rounded():
        returns the Kelvin object with value converted to int (rounded).
    to_celsius():
        returns a Celsius object which contains the converted value.
    to_fahrenheit():
        returns a Fahrenheit object which contains the converted value.
    to_delisle():
        returns a Delisle object which contains the converted value.
    to_newton():
        returns a Newton object which contains the converted value.
    to_rankine():
        returns a Rankine object which contains the converted value.
    to_reaumur():
        returns a Réaumur object which contains the converted value.
    to_romer():
        returns a Rømer object which contains the converted value.
    """

    value: TEMP

    def precise(self) -> 'Kelvin[float]':
        """
        Returns a Kelvin object with float value.

        :return: Kelvin Object
        """
        return Kelvin(float(self.value))

    def rounded(self) -> 'Kelvin[int]':
        """
        Returns a Kelvin object with int (rounded) value.

        :return: Kelvin Object
        """
        return Kelvin(round(self.value))

    def to_celsius(self) -> 'Celsius[TEMP]':
        """
        Returns a Celsius object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        :return: Celsius object
        """
        celsius = type(self.value)((self.value - 273.15))
        return Celsius(celsius)

    def to_fahrenheit(self) -> 'Fahrenheit[TEMP]':
        """
        Returns a Fahrenheit object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        :return: Fahrenheit object
        """
        fahrenheit = type(self.value)((self.value * 9 / 5) - 459.67)
        return Fahrenheit(fahrenheit)

    def to_delisle(self) -> 'Delisle[TEMP]':
        """
        Returns a Delisle object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        :return: Delisle object
        """
        delisle = type(self.value)((373.15 - self.value) * 3 / 2)
        return Delisle(delisle)

    def to_newton(self) -> 'Newton[TEMP]':
        """
        Returns a Newton object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        :return: Newton object
        """
        newton = type(self.value)((self.value - 273.15) * 33 / 100)
        return Newton(newton)

    def to_rankine(self) -> 'Rankine[TEMP]':
        """
        Returns a Rankine object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        :return: Rankine object
        """
        rankine = type(self.value)(self.value * 1.8)
        return Rankine(rankine)

    def to_reaumur(self) -> 'Reaumur[TEMP]':
        """
        Returns a Réaumur object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        :return: Reaumur object
        """
        reaumur = type(self.value)((self.value - 273.15) * 4 / 5)
        return Reaumur(reaumur)

    def to_romer(self) -> 'Romer[TEMP]':
        """
        Returns a Rømer object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        :return: Romer object
        """
        romer = type(self.value)((self.value - 273.15) * (21 / 40) + 7.5)
        return Romer(romer)


@dataclass
class Newton(Generic[TEMP]):
    """
    A Dataclass that represents Newton temperature scale
    and provides conversions to other temperature scales.

    ...

    Attributes
    ----------
    value: int | float
        temperature value (e.g. 36ºN)

    Methods
    -------
    precise():
        returns the Newton object with value converted to float.
    rounded():
        returns the Newton object with value converted to int (rounded).
    to_celsius():
        returns a Celsius object which contains the converted value.
    to_fahrenheit():
        returns a Fahrenheit object which contains the converted value.
    to_delisle():
        returns a Delisle object which contains the converted value.
    to_kelvin():
        returns a Kelvin object which contains the converted value.
    to_rankine():
        returns a Rankine object which contains the converted value.
    to_reaumur():
        returns a Réaumur object which contains the converted value.
    to_romer():
        returns a Rømer object which contains the converted value.
    """

    value: TEMP

    def precise(self) -> 'Newton[float]':
        """
        Returns a Newton object with float value.

        :return: Newton Object
        """
        return Newton(float(self.value))

    def rounded(self) -> 'Newton[int]':
        """
        Returns a Newton object with int (rounded) value.

        :return: Newton Object
        """
        return Newton(round(self.value))

    def to_celsius(self) -> 'Celsius[TEMP]':
        """
        Returns a Celsius object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        :return: Celsius object
        """
        celsius = type(self.value)((self.value / 0.33))
        return Celsius(celsius)

    def to_fahrenheit(self) -> 'Fahrenheit[TEMP]':
        """
        Returns a Fahrenheit object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        :return: Fahrenheit object
        """
        fahrenheit = type(self.value)(self.value * 60 / 11 + 32)
        return Fahrenheit(fahrenheit)

    def to_delisle(self) -> 'Delisle[TEMP]':
        """
        Returns a Delisle object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        :return: Delisle object
        """
        delisle = type(self.value)(self.value * 4.5455 - 100)
        return Delisle(delisle)

    def to_kelvin(self) -> 'Kelvin[TEMP]':
        """
        Returns a Kelvin object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        :return: Kelvin object
        """
        kelvin = type(self.value)(self.value / 0.33000 + 273.15)
        return Kelvin(kelvin)

    def to_rankine(self) -> 'Rankine[TEMP]':
        """
        Returns a Rankine object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        :return: Rankine object
        """
        rankine = type(self.value)(self.value * 5.4545 + 491.67)
        return Rankine(rankine)

    def to_reaumur(self) -> 'Reaumur[TEMP]':
        """
        Returns a Réaumur object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        :return: Reaumur object
        """
        reaumur = type(self.value)(self.value * 80 / 33)
        return Reaumur(reaumur)

    def to_romer(self) -> 'Romer[TEMP]':
        """
        Returns a Rømer object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        :return: Romer object
        """
        romer = type(self.value)(self.value * 35 / 22 + 7.5)
        return Romer(romer)


@dataclass
class Rankine(Generic[TEMP]):
    """
    A Dataclass that represents Rankine temperature scale
    and provides conversions to other temperature scales.

    ...

    Attributes
    ----------
    value: int | float
        temperature value (e.g. 36ºR)

    Methods
    -------
    precise():
        returns the Rankine object with value converted to float.
    rounded():
        returns the Rankine object with value converted to int (rounded).
    to_celsius():
        returns a Celsius object which contains the converted value.
    to_fahrenheit():
        returns a Fahrenheit object which contains the converted value.
    to_delisle():
        returns a Delisle object which contains the converted value.
    to_kelvin():
        returns a Kelvin object which contains the converted value.
    to_newton():
        returns a Newton object which contains the converted value.
    to_reaumur():
        returns a Réaumur object which contains the converted value.
    to_romer():
        returns a Rømer object which contains the converted value.
    """

    value: TEMP

    def precise(self) -> 'Rankine[float]':
        """
        Returns a Rankine object with float value.

        :return: Rankine Object
        """
        return Rankine(float(self.value))

    def rounded(self) -> 'Rankine[int]':
        """
        Returns a Rankine object with int (rounded) value.

        :return: Rankine Object
        """
        return Rankine(round(self.value))

    def to_celsius(self) -> 'Celsius[TEMP]':
        """
        Returns a Celsius object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        :return: Celsius object
        """
        celsius = type(self.value)((self.value - 491.67) * 5 / 9)
        return Celsius(celsius)

    def to_fahrenheit(self) -> 'Fahrenheit[TEMP]':
        """
        Returns a Fahrenheit object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        :return: Fahrenheit object
        """
        fahrenheit = type(self.value)(self.value - 459.67)
        return Fahrenheit(fahrenheit)

    def to_delisle(self) -> 'Delisle[TEMP]':
        """
        Returns a Delisle object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        :return: Delisle object
        """
        delisle = type(self.value)((671.67 - self.value) * 5 / 6)
        return Delisle(delisle)

    def to_kelvin(self) -> 'Kelvin[TEMP]':
        """
        Returns a Kelvin object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        :return: Kelvin object
        """
        kelvin = type(self.value)(self.value * 5 / 9)
        return Kelvin(kelvin)

    def to_newton(self) -> 'Newton[TEMP]':
        """
        Returns a Newton object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        :return: Newton object
        """
        newton = type(self.value)((self.value - 491.67) * 11 / 60)
        return Newton(newton)

    def to_reaumur(self) -> 'Reaumur[TEMP]':
        """
        Returns a Réaumur object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        :return: Reaumur object
        """
        reaumur = type(self.value)((self.value - 491.67) * 4 / 9)
        return Reaumur(reaumur)

    def to_romer(self) -> 'Romer[TEMP]':
        """
        Returns a Rømer object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        :return: Romer object
        """
        romer = type(self.value)((self.value - 491.67) * (7 / 24) + 7.5)
        return Romer(romer)


@dataclass
class Reaumur(Generic[TEMP]):
    """
    A Dataclass that represents Réaumur temperature scale
    and provides conversions to other temperature scales.

    ...

    Attributes
    ----------
    value: int | float
        temperature value (e.g. 36ºRé)

    Methods
    -------
    precise():
        returns the Réaumur object with value converted to float.
    rounded():
        returns the Réaumur object with value converted to int (rounded).
    to_celsius():
        returns a Celsius object which contains the converted value.
    to_fahrenheit():
        returns a Fahrenheit object which contains the converted value.
    to_delisle():
        returns a Delisle object which contains the converted value.
    to_kelvin():
        returns a Kelvin object which contains the converted value.
    to_newton():
        returns a Newton object which contains the converted value.
    to_rankine():
        returns a Rankine object which contains the converted value.
    to_romer():
        returns a Rømer object which contains the converted value.
    """

    value: TEMP

    def precise(self) -> 'Reaumur[float]':
        """
        Returns a Réaumur object with float value.

        :return: Réaumur Object
        """
        return Reaumur(float(self.value))

    def rounded(self) -> 'Reaumur[int]':
        """
        Returns a Réaumur object with int (rounded) value.

        :return: Réaumur Object
        """
        return Reaumur(round(self.value))


@dataclass
class Romer(Generic[TEMP]):
    """
    A Dataclass that represents Rømer temperature scale
    and provides conversions to other temperature scales.

    ...

    Attributes
    ----------
    value: int | float
        temperature value (e.g. 36ºRø)

    Methods
    -------
    precise():
        returns the Rømer object with value converted to float.
    rounded():
        returns the Rømer object with value converted to int (rounded).
    to_celsius():
        returns a Celsius object which contains the converted value.
    to_fahrenheit():
        returns a Fahrenheit object which contains the converted value.
    to_delisle():
        returns a Delisle object which contains the converted value.
    to_kelvin():
        returns a Kelvin object which contains the converted value.
    to_newton():
        returns a Newton object which contains the converted value.
    to_rankine():
        returns a Rankine object which contains the converted value.
    to_reaumur():
        returns a Réaumur object which contains the converted value.
    """

    value: TEMP

    def precise(self) -> 'Romer[float]':
        """
        Returns a Rømer object with float value.

        :return: Rømer Object
        """
        return Romer(float(self.value))

    def rounded(self) -> 'Romer[int]':
        """
        Returns a Rømer object with int (rounded) value.

        :return: Rømer Object
        """
        return Romer(round(self.value))
