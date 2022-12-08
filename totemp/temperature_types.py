#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from dataclasses import dataclass, field
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
    value : int | float
        Temperature value (e.g. 36ºC).

    __symbol : str
        Official Celsius scale symbol.

    Methods
    -------
    precise()
        returns the Celsius object with value converted to float.

    rounded()
        returns the Celsius object with value converted to int (rounded).

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
    """

    value: TEMP
    __symbol: str = field(compare=False, repr=False, default='ºC')

    def __str__(self) -> str:
        return f'{self.value}{self.__symbol}'

    @property
    def symbol(self) -> str:
        """
        Returns Celsius object official symbol.

        Returns
        -------
        __symbol : str
            'ºC'
        """
        return self.__symbol

    def precise(self) -> 'Celsius[float]':
        """
        Returns a Celsius object with the same value now converted to float.

        Returns
        -------
        Celsius[float]
        """
        return Celsius(float(self.value))

    def rounded(self) -> 'Celsius[int]':
        """
        Returns a Celsius object with the same value now converted to int (rounded).

        Returns
        -------
        Celsius[int]
        """
        return Celsius(round(self.value))

    def to_fahrenheit(self) -> 'Fahrenheit[TEMP]':
        """
        Returns a Fahrenheit object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        Returns
        -------
        Fahrenheit[TEMP]
        """
        fahrenheit = type(self.value)(self.value * 9 / 5 + 32)
        return Fahrenheit(fahrenheit)

    def to_delisle(self) -> 'Delisle[TEMP]':
        """
        Returns a Delisle object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        Returns
        -------
        Delisle[TEMP]
        """
        delisle = type(self.value)(self.value * 1.5000 - 100.00)
        return Delisle(delisle)

    def to_kelvin(self) -> 'Kelvin[TEMP]':
        """
        Returns a Kelvin object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        Returns
        -------
        Kelvin[TEMP]
        """
        kelvin = type(self.value)(self.value + 273.15)
        return Kelvin(kelvin)

    def to_newton(self) -> 'Newton[TEMP]':
        """
        Returns a Newton object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        Returns
        -------
        Newton[TEMP]
        """
        newton = type(self.value)(self.value * 33 / 100)
        return Newton(newton)

    def to_rankine(self) -> 'Rankine[TEMP]':
        """
        Returns a Rankine object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        Returns
        -------
        Rankine[TEMP]
        """
        rankine = type(self.value)(self.value * 9 / 5 + 491.67)
        return Rankine(rankine)

    def to_reaumur(self) -> 'Reaumur[TEMP]':
        """
        Returns a Réaumur object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        Returns
        -------
        Reaumur[TEMP]
        """
        reaumur = type(self.value)(self.value * 4 / 5)
        return Reaumur(reaumur)

    def to_romer(self) -> 'Romer[TEMP]':
        """
        Returns a Rømer object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        Returns
        -------
        Romer[TEMP]
        """
        romer = type(self.value)(self.value * 0.52500 + 7.50)
        return Romer(romer)


@dataclass
class Fahrenheit(Generic[TEMP]):
    """
    A Dataclass that represents Fahrenheit temperature scale
    and provides conversions to other temperature scales.

    ...

    Attributes
    ----------
    value : int | float
        Temperature value (e.g. 36ºF).

    __symbol : str
        Official Fahrenheit scale symbol.

    Methods
    -------
    precise()
        returns the Fahrenheit object with value converted to float.

    rounded()
        returns the Fahrenheit object with value converted to int (rounded).

    to_celsius()
        returns a Celsius object which contains the converted value.

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
    """

    value: TEMP
    __symbol: str = field(compare=False, repr=False, default='ºF')

    def __str__(self) -> str:
        return f'{self.value}{self.__symbol}'

    @property
    def symbol(self) -> str:
        """
        Returns Fahrenheit object official symbol.

        Returns
        -------
        __symbol : str
            'ºF'
        """
        return self.__symbol

    def precise(self) -> 'Fahrenheit[float]':
        """
        Returns a Fahrenheit object with the same value now converted to float.

        Returns
        -------
        Fahrenheit[float]
        """
        return Fahrenheit(float(self.value))

    def rounded(self) -> 'Fahrenheit[int]':
        """
        Returns a Fahrenheit object with the same value now converted to int (rounded).

        Returns
        -------
        Fahrenheit[int]
        """
        return Fahrenheit(round(self.value))

    def to_celsius(self) -> 'Celsius[TEMP]':
        """
        Returns a Celsius object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        Returns
        -------
        Celsius[TEMP]
        """
        celsius = type(self.value)((self.value - 32) * 5 / 9)
        return Celsius(celsius)

    def to_delisle(self) -> 'Delisle[TEMP]':
        """
        Returns a Delisle object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        Returns
        -------
        Delisle[TEMP]
        """
        delisle = type(self.value)((212 - self.value) * 5 / 6)
        return Delisle(delisle)

    def to_kelvin(self) -> 'Kelvin[TEMP]':
        """
        Returns a Kelvin object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        Returns
        -------
        Kelvin[TEMP]
        """
        kelvin = type(self.value)((self.value + 459.67) * 5 / 9)
        return Kelvin(kelvin)

    def to_newton(self) -> 'Newton[TEMP]':
        """
        Returns a Newton object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        Returns
        -------
        Newton[TEMP]
        """
        newton = type(self.value)((self.value - 32) * 11 / 60)
        return Newton(newton)

    def to_rankine(self) -> 'Rankine[TEMP]':
        """
        Returns a Rankine object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        Returns
        -------
        Rankine[TEMP]
        """
        rankine = type(self.value)(self.value + 459.67)
        return Rankine(rankine)

    def to_reaumur(self) -> 'Reaumur[TEMP]':
        """
        Returns a Réaumur object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        Returns
        -------
        Reaumur[TEMP]
        """
        reaumur = type(self.value)((self.value - 32) * 4 / 9)
        return Reaumur(reaumur)

    def to_romer(self) -> 'Romer[TEMP]':
        """
        Returns a Rømer object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        Returns
        -------
        Romer[TEMP]
        """
        romer = type(self.value)((self.value - 32) * (7 / 24) + 7.5)
        return Romer(romer)


@dataclass
class Delisle(Generic[TEMP]):
    """
    A Dataclass that represents Delisle temperature scale
    and provides conversions to other temperature scales.

    ...

    Attributes
    ----------
    value : int | float
        Temperature value (e.g. 36ºDe).

    __symbol : str
        Official Delisle scale symbol.

    Methods
    -------
    precise()
        returns the Delisle object with value converted to float.

    rounded()
        returns the Delisle object with value converted to int (rounded).

    to_celsius()
        returns a Celsius object which contains the converted value.

    to_fahrenheit()
        returns a Fahrenheit object which contains the converted value.

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
    """

    value: TEMP
    __symbol: str = field(compare=False, repr=False, default='ºDe')

    def __str__(self) -> str:
        return f'{self.value}{self.__symbol}'

    @property
    def symbol(self) -> str:
        """
        Returns Delisle object official symbol.

        Returns
        -------
        __symbol : str
            'ºDe'
        """
        return self.__symbol

    def precise(self) -> 'Delisle[float]':
        """
        Returns a Delisle object with the same value now converted to float.

        Returns
        -------
        Delisle[float]
        """
        return Delisle(float(self.value))

    def rounded(self) -> 'Delisle[int]':
        """
        Returns a Delisle object with the same value now converted to int (rounded).

        Returns
        -------
        Delisle[int]
        """
        return Delisle(round(self.value))

    def to_celsius(self) -> 'Celsius[TEMP]':
        """
        Returns a Celsius object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        Returns
        -------
        Celsius[TEMP]
        """
        celsius = type(self.value)((100 - self.value * 2 / 3))
        return Celsius(celsius)

    def to_fahrenheit(self) -> 'Fahrenheit[TEMP]':
        """
        Returns a Fahrenheit object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        Returns
        -------
        Fahrenheit[TEMP]
        """
        fahrenheit = type(self.value)(212 - self.value * 6 / 5)
        return Fahrenheit(fahrenheit)

    def to_kelvin(self) -> 'Kelvin[TEMP]':
        """
        Returns a Kelvin object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        Returns
        -------
        Kelvin[TEMP]
        """
        kelvin = type(self.value)(373.15 - (self.value * 2 / 3))
        return Kelvin(kelvin)

    def to_newton(self) -> 'Newton[TEMP]':
        """
        Returns a Newton object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        Returns
        -------
        Newton[TEMP]
        """
        newton = type(self.value)(33 - self.value * 11 / 50)
        return Newton(newton)

    def to_rankine(self) -> 'Rankine[TEMP]':
        """
        Returns a Rankine object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        Returns
        -------
        Rankine[TEMP]
        """
        rankine = type(self.value)(671.67 - self.value * 6 / 5)
        return Rankine(rankine)

    def to_reaumur(self) -> 'Reaumur[TEMP]':
        """
        Returns a Réaumur object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        Returns
        -------
        Reaumur[TEMP]
        """
        reaumur = type(self.value)(80 - self.value * 8 / 15)
        return Reaumur(reaumur)

    def to_romer(self) -> 'Romer[TEMP]':
        """
        Returns a Rømer object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        Returns
        -------
        Romer[TEMP]
        """
        romer = type(self.value)(60 - self.value * 7 / 20)
        return Romer(romer)


@dataclass
class Kelvin(Generic[TEMP]):
    """
    A Dataclass that represents Kelvin temperature scale
    and provides conversions to other temperature scales.

    ...

    Attributes
    ----------
    value : int | float
        Temperature value (e.g. 36ºK).

    __symbol : str
        Official Kelvin scale symbol.

    Methods
    -------
    precise()
        returns the Kelvin object with value converted to float.

    rounded()
        returns the Kelvin object with value converted to int (rounded).

    to_celsius()
        returns a Celsius object which contains the converted value.

    to_fahrenheit()
        returns a Fahrenheit object which contains the converted value.

    to_delisle()
        returns a Delisle object which contains the converted value.

    to_newton()
        returns a Newton object which contains the converted value.

    to_rankine()
        returns a Rankine object which contains the converted value.

    to_reaumur()
        returns a Réaumur object which contains the converted value.

    to_romer()
        returns a Rømer object which contains the converted value.
    """

    value: TEMP
    __symbol: str = field(compare=False, repr=False, default='ºK')

    def __str__(self) -> str:
        return f'{self.value}{self.__symbol}'

    @property
    def symbol(self) -> str:
        """
        Returns Kelvin object official symbol.

        Returns
        -------
        __symbol : str
            'ºK'
        """
        return self.__symbol

    def precise(self) -> 'Kelvin[float]':
        """
        Returns a Kelvin object with the same value now converted to float.

        Returns
        -------
        Kelvin[float]
        """
        return Kelvin(float(self.value))

    def rounded(self) -> 'Kelvin[int]':
        """
        Returns a Kelvin object with the same value now converted to int (rounded).

        Returns
        -------
        Kelvin[int]
        """
        return Kelvin(round(self.value))

    def to_celsius(self) -> 'Celsius[TEMP]':
        """
        Returns a Celsius object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        Returns
        -------
        Celsius[TEMP]
        """
        celsius = type(self.value)((self.value - 273.15))
        return Celsius(celsius)

    def to_fahrenheit(self) -> 'Fahrenheit[TEMP]':
        """
        Returns a Fahrenheit object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        Returns
        -------
        Fahrenheit[TEMP]
        """
        fahrenheit = type(self.value)((self.value * 9 / 5) - 459.67)
        return Fahrenheit(fahrenheit)

    def to_delisle(self) -> 'Delisle[TEMP]':
        """
        Returns a Delisle object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        Returns
        -------
        Delisle[TEMP]
        """
        delisle = type(self.value)((373.15 - self.value) * 3 / 2)
        return Delisle(delisle)

    def to_newton(self) -> 'Newton[TEMP]':
        """
        Returns a Newton object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        Returns
        -------
        Newton[TEMP]
        """
        newton = type(self.value)((self.value - 273.15) * 33 / 100)
        return Newton(newton)

    def to_rankine(self) -> 'Rankine[TEMP]':
        """
        Returns a Rankine object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        Returns
        -------
        Rankine[TEMP]
        """
        rankine = type(self.value)(self.value * 1.8)
        return Rankine(rankine)

    def to_reaumur(self) -> 'Reaumur[TEMP]':
        """
        Returns a Réaumur object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        Returns
        -------
        Reaumur[TEMP]
        """
        reaumur = type(self.value)((self.value - 273.15) * 4 / 5)
        return Reaumur(reaumur)

    def to_romer(self) -> 'Romer[TEMP]':
        """
        Returns a Rømer object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        Returns
        -------
        Romer[TEMP]
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
    value : int | float
        Temperature value (e.g. 36ºN).

    __symbol : str
        Official Newton scale symbol.

    Methods
    -------
    precise()
        returns the Newton object with value converted to float.

    rounded()
        returns the Newton object with value converted to int (rounded).

    to_celsius()
        returns a Celsius object which contains the converted value.

    to_fahrenheit()
        returns a Fahrenheit object which contains the converted value.

    to_delisle()
        returns a Delisle object which contains the converted value.

    to_kelvin()
        returns a Kelvin object which contains the converted value.

    to_rankine()
        returns a Rankine object which contains the converted value.

    to_reaumur()
        returns a Réaumur object which contains the converted value.

    to_romer()
        returns a Rømer object which contains the converted value.
    """

    value: TEMP
    __symbol: str = field(compare=False, repr=False, default='ºN')

    def __str__(self) -> str:
        return f'{self.value}{self.__symbol}'

    @property
    def symbol(self) -> str:
        """
        Returns Newton object official symbol.

        Returns
        -------
        __symbol : str
            'ºN'
        """
        return self.__symbol

    def precise(self) -> 'Newton[float]':
        """
        Returns a Newton object with the same value now converted to float.

        Returns
        -------
        Newton[float]
        """
        return Newton(float(self.value))

    def rounded(self) -> 'Newton[int]':
        """
        Returns a Newton object with the same value now converted to int (rounded).

        Returns
        -------
        Newton[int]
        """
        return Newton(round(self.value))

    def to_celsius(self) -> 'Celsius[TEMP]':
        """
        Returns a Celsius object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        Returns
        -------
        Celsius[TEMP]
        """
        celsius = type(self.value)((self.value / 0.33))
        return Celsius(celsius)

    def to_fahrenheit(self) -> 'Fahrenheit[TEMP]':
        """
        Returns a Fahrenheit object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        Returns
        -------
        Fahrenheit[TEMP]
        """
        fahrenheit = type(self.value)(self.value * 60 / 11 + 32)
        return Fahrenheit(fahrenheit)

    def to_delisle(self) -> 'Delisle[TEMP]':
        """
        Returns a Delisle object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        Returns
        -------
        Delisle[TEMP]
        """
        delisle = type(self.value)(self.value * 4.5455 - 100)
        return Delisle(delisle)

    def to_kelvin(self) -> 'Kelvin[TEMP]':
        """
        Returns a Kelvin object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        Returns
        -------
        Kelvin[TEMP]
        """
        kelvin = type(self.value)(self.value / 0.33000 + 273.15)
        return Kelvin(kelvin)

    def to_rankine(self) -> 'Rankine[TEMP]':
        """
        Returns a Rankine object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        Returns
        -------
        Rankine[TEMP]
        """
        rankine = type(self.value)(self.value * 5.4545 + 491.67)
        return Rankine(rankine)

    def to_reaumur(self) -> 'Reaumur[TEMP]':
        """
        Returns a Réaumur object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        Returns
        -------
        Reaumur[TEMP]
        """
        reaumur = type(self.value)(self.value * 80 / 33)
        return Reaumur(reaumur)

    def to_romer(self) -> 'Romer[TEMP]':
        """
        Returns a Rømer object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        Returns
        -------
        Romer[TEMP]
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
    value : int | float
        Temperature value (e.g. 36ºR).

    __symbol : str
        Official Rankine scale symbol.

    Methods
    -------
    precise()
        returns the Rankine object with value converted to float.

    rounded()
        returns the Rankine object with value converted to int (rounded).

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

    to_reaumur()
        returns a Réaumur object which contains the converted value.

    to_romer()
        returns a Rømer object which contains the converted value.
    """

    value: TEMP
    __symbol: str = field(compare=False, repr=False, default='ºR')

    def __str__(self) -> str:
        return f'{self.value}{self.__symbol}'

    @property
    def symbol(self) -> str:
        """
        Returns Rankine object official symbol.

        Returns
        -------
        __symbol : str
            'ºR'
        """
        return self.__symbol

    def precise(self) -> 'Rankine[float]':
        """
        Returns a Rankine object with the same value now converted to float.

        Returns
        -------
        Rankine[float]
        """
        return Rankine(float(self.value))

    def rounded(self) -> 'Rankine[int]':
        """
        Returns a Rankine object with the same value now converted to int (rounded).

        Returns
        -------
        Rankine[int]
        """
        return Rankine(round(self.value))

    def to_celsius(self) -> 'Celsius[TEMP]':
        """
        Returns a Celsius object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        Returns
        -------
        Celsius[TEMP]
        """
        celsius = type(self.value)((self.value - 491.67) * 5 / 9)
        return Celsius(celsius)

    def to_fahrenheit(self) -> 'Fahrenheit[TEMP]':
        """
        Returns a Fahrenheit object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        Returns
        -------
        Fahrenheit[TEMP]
        """
        fahrenheit = type(self.value)(self.value - 459.67)
        return Fahrenheit(fahrenheit)

    def to_delisle(self) -> 'Delisle[TEMP]':
        """
        Returns a Delisle object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        Returns
        -------
        Delisle[TEMP]
        """
        delisle = type(self.value)((671.67 - self.value) * 5 / 6)
        return Delisle(delisle)

    def to_kelvin(self) -> 'Kelvin[TEMP]':
        """
        Returns a Kelvin object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        Returns
        -------
        Kelvin[TEMP]
        """
        kelvin = type(self.value)(self.value * 5 / 9)
        return Kelvin(kelvin)

    def to_newton(self) -> 'Newton[TEMP]':
        """
        Returns a Newton object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        Returns
        -------
        Newton[TEMP]
        """
        newton = type(self.value)((self.value - 491.67) * 11 / 60)
        return Newton(newton)

    def to_reaumur(self) -> 'Reaumur[TEMP]':
        """
        Returns a Réaumur object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        Returns
        -------
        Reaumur[TEMP]
        """
        reaumur = type(self.value)((self.value - 491.67) * 4 / 9)
        return Reaumur(reaumur)

    def to_romer(self) -> 'Romer[TEMP]':
        """
        Returns a Rømer object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        Returns
        -------
        Romer[TEMP]
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
    value : int | float
        Temperature value (e.g. 36ºRé).

    __symbol : str
        Official Réaumur scale symbol.

    Methods
    -------
    precise()
        returns the Réaumur object with value converted to float.

    rounded()
        returns the Réaumur object with value converted to int (rounded).

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

    to_romer()
        returns a Rømer object which contains the converted value.
    """

    value: TEMP
    __symbol: str = field(compare=False, repr=False, default='ºRé')

    def __str__(self) -> str:
        return f'{self.value}{self.__symbol}'

    @property
    def symbol(self) -> str:
        """
        Returns Réaumur object official symbol.

        Returns
        -------
        __symbol : str
            'ºRé'
        """
        return self.__symbol

    def precise(self) -> 'Reaumur[float]':
        """
        Returns a Réaumur object with the same value now converted to float.

        Returns
        -------
        Reaumur[float]
        """
        return Reaumur(float(self.value))

    def rounded(self) -> 'Reaumur[int]':
        """
        Returns a Réaumur object with the same value now converted to int (rounded).

        Returns
        -------
        Reaumur[int]
        """
        return Reaumur(round(self.value))

    def to_celsius(self) -> 'Celsius[TEMP]':
        """
        Returns a Celsius object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        Returns
        -------
        Celsius[TEMP]
        """
        celsius = type(self.value)(self.value * 5 / 4)
        return Celsius(celsius)

    def to_fahrenheit(self) -> 'Fahrenheit[TEMP]':
        """
        Returns a Fahrenheit object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        Returns
        -------
        Fahrenheit[TEMP]
        """
        fahrenheit = type(self.value)(self.value * 9 / 4 + 32)
        return Fahrenheit(fahrenheit)

    def to_delisle(self) -> 'Delisle[TEMP]':
        """
        Returns a Delisle object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        Returns
        -------
        Delisle[TEMP]
        """
        delisle = type(self.value)((80 - self.value) * 15 / 8)
        return Delisle(delisle)

    def to_kelvin(self) -> 'Kelvin[TEMP]':
        """
        Returns a Kelvin object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        Returns
        -------
        Kelvin[TEMP]
        """
        kelvin = type(self.value)(self.value * 5 / 4 + 273.15)
        return Kelvin(kelvin)

    def to_newton(self) -> 'Newton[TEMP]':
        """
        Returns a Newton object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        Returns
        -------
        Newton[TEMP]
        """
        newton = type(self.value)(self.value * 33 / 80)
        return Newton(newton)


@dataclass
class Romer(Generic[TEMP]):
    """
    A Dataclass that represents Rømer temperature scale
    and provides conversions to other temperature scales.

    ...

    Attributes
    ----------
    value : int | float
        Temperature value (e.g. 36ºRø).

    __symbol : str
        Official Rømer scale symbol.

    Methods
    -------
    precise()
        returns the Rømer object with value converted to float.

    rounded()
        returns the Rømer object with value converted to int (rounded).

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
    """

    value: TEMP
    __symbol: str = field(compare=False, repr=False, default='ºRø')

    def __str__(self) -> str:
        return f'{self.value}{self.__symbol}'

    @property
    def symbol(self) -> str:
        """
        Returns Rømer object official symbol.

        Returns
        -------
        __symbol : str
            'ºRø'
        """
        return self.__symbol

    def precise(self) -> 'Romer[float]':
        """
        Returns a Rømer object with the same value now converted to float.

        Returns
        -------
        Romer[float]
        """
        return Romer(float(self.value))

    def rounded(self) -> 'Romer[int]':
        """
        Returns a Rømer object with the same value now converted to int (rounded).

        Returns
        -------
        Romer[int]
        """
        return Romer(round(self.value))

    def to_celsius(self) -> 'Celsius[TEMP]':
        """
        Returns a Celsius object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        Returns
        -------
        Celsius[TEMP]
        """
        celsius = type(self.value)((self.value - 7.5) * 40 / 21)
        return Celsius(celsius)

    def to_fahrenheit(self) -> 'Fahrenheit[TEMP]':
        """
        Returns a Fahrenheit object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        Returns
        -------
        Fahrenheit[TEMP]
        """
        fahrenheit = type(self.value)((self.value - 7.5) * 24 / 7 + 32)
        return Fahrenheit(fahrenheit)

    def to_delisle(self) -> 'Delisle[TEMP]':
        """
        Returns a Delisle object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        Returns
        -------
        Delisle[TEMP]
        """
        delisle = type(self.value)((60 - self.value) * 20 / 7)
        return Delisle(delisle)

    def to_kelvin(self) -> 'Kelvin[TEMP]':
        """
        Returns a Kelvin object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        Returns
        -------
        Kelvin[TEMP]
        """
        kelvin = type(self.value)((self.value - 7.5) * 40 / 21 + 273.15)
        return Kelvin(kelvin)

    def to_newton(self) -> 'Newton[TEMP]':
        """
        Returns a Newton object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        Returns
        -------
        Newton[TEMP]
        """
        newton = type(self.value)((self.value - 7.5) * 22 / 35)
        return Newton(newton)

    def to_rankine(self) -> 'Rankine[TEMP]':
        """
        Returns a Rankine object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        Returns
        -------
        Rankine[TEMP]
        """
        rankine = type(self.value)((self.value - 7.5) * 24 / 7 + 491.67)
        return Rankine(rankine)

    def to_reaumur(self) -> 'Reaumur[TEMP]':
        """
        Returns a Réaumur object which contains the class attribute "value"
        with the result from the conversion typed the same as the attribute.

        Returns
        -------
        Reaumur[TEMP]
        """
        reaumur = type(self.value)((self.value - 7.5) * 32 / 21)
        return Reaumur(reaumur)
