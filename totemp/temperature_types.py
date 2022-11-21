#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import trunc


class Celsius:
    """Provides conversion of Celsius to other temperature scales"""

    @staticmethod
    def to_fahrenheit(
        celsius: float | int, /, *, float_ret=True
    ) -> float | int:
        """
        Converts Celsius to Fahrenheit, returning a float by default.

        If the float_ret parameter is False, it returns an approximate int value
        (using the math's module trunc function).

        :param celsius: Celsius value to be converted
        :param float_ret: Optional, True by default to return floats
        :return: float or int
        """
        if float_ret:
            return float(celsius * 9 / 5 + 32)
        return trunc(celsius * 9 / 5 + 32)

    @staticmethod
    def to_delisle(celsius: float | int, /, *, float_ret=True) -> float | int:
        """
        Converts Celsius to Delisle, returning a float by default.

        If the float_ret parameter is False, it returns an approximate int value
        (using the math's module trunc function).

        :param celsius: Celsius value to be converted
        :param float_ret: Optional, True by default to return floats
        :return: float or int
        """
        if float_ret:
            return float((100 - celsius) * 3 / 2)
        return trunc((100 - celsius) * 3 / 2)

    @staticmethod
    def to_kelvin(celsius: float | int, /, *, float_ret=True) -> float | int:
        """
        Converts Celsius to Kelvin, returning a float by default.

        If the float_ret parameter is False, it returns an approximate int value
        (using the math's module trunc function).

        :param celsius: Celsius value to be converted
        :param float_ret: Optional, True by default to return floats
        :return: float or int
        """
        if float_ret:
            return float(celsius + 273.15)
        return trunc(celsius + 273.15)

    @staticmethod
    def to_newton(celsius: float | int, /, *, float_ret=True) -> float | int:
        """
        Converts Celsius to Newton, returning a float by default.

        If the float_ret parameter is False, it returns an approximate int value
        (using the math's module trunc function).

        :param celsius: Celsius value to be converted
        :param float_ret: Optional, True by default to return floats
        :return: float or int
        """
        if float_ret:
            return float(celsius * 33 / 100)
        return trunc(celsius * 33 / 100)

    @staticmethod
    def to_rankine(celsius: float | int, /, *, float_ret=True) -> float | int:
        """
        Converts Celsius to Rankine, returning a float by default.

        If the float_ret parameter is False, it returns an approximate int value
        (using the math's module trunc function).

        :param celsius: Celsius value to be converted
        :param float_ret: Optional, True by default to return floats
        :return: float or int
        """
        if float_ret:
            return float(celsius * 9 / 5 + 491.67)
        return trunc(celsius * 9 / 5 + 491.67)

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


class Fahrenheit:
    """Provides conversion of Fahrenheit to other temperature scales"""

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


class Delisle:
    """Provides conversion of Delisle to other temperature scales"""

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


class Kelvin:
    """Provides conversion of Kelvin to other temperature scales"""

    @staticmethod
    def to_celsius(kelvin: float | int, /, *, float_ret=True) -> float | int:
        """
        Converts Kelvin to Celsius, returning a float by default.
        If the float_ret parameter is False, it returns an approximate int value
        (using the math's module trunc function).
        :param kelvin: Kelvin value to be converted
        :param float_ret: Optional, True by default to return floats
        :return: float or int
        """
        if float_ret:
            return float(kelvin - 273.15)
        return trunc(kelvin - 273.15)

    @staticmethod
    def to_delisle(kelvin: float | int, /, *, float_ret=True) -> float | int:
        """
        Converts Kelvin to Delisle, returning a float by default.
        If the float_ret parameter is False, it returns an approximate int value
        (using the math's module trunc function).
        :param kelvin: Kelvin value to be converted
        :param float_ret: Optional, True by default to return floats
        :return: float or int
        """
        if float_ret:
            return float((373.15 - kelvin) * 3 / 2)
        return trunc((373.15 - kelvin) * 3 / 2)

    @staticmethod
    def to_fahrenheit(
        kelvin: float | int, /, *, float_ret=True
    ) -> float | int:
        """
        Converts Kelvin to Fahrenheit, returning a float by default.
        If the float_ret parameter is False, it returns an approximate int value
        (using the math's module trunc function).
        :param kelvin: Kelvin value to be converted
        :param float_ret: Optional, True by default to return floats
        :return: float or int
        """
        if float_ret:
            return float((kelvin * 9 / 5) - 459.67)
        return trunc((kelvin * 9 / 5) - 459.67)

    @staticmethod
    def to_newton(kelvin: float | int, /, *, float_ret=True) -> float | int:
        """
        Converts Kelvin to Newton, returning a float by default.
        If the float_ret parameter is False, it returns an approximate int value
        (using the math's module trunc function).
        :param kelvin: Kelvin value to be converted
        :param float_ret: Optional, True by default to return floats
        :return: float or int
        """
        if float_ret:
            return float((kelvin - 273.15) * 33 / 100)
        return trunc((kelvin - 273.15) * 33 / 100)

    @staticmethod
    def to_rankine(kelvin: float | int, /, *, float_ret=True) -> float | int:
        """
        Converts Kelvin to Rankine, returning a float by default.
        If the float_ret parameter is False, it returns an approximate int value
        (using the math's module trunc function).
        :param kelvin: Kelvin value to be converted
        :param float_ret: Optional, True by default to return floats
        :return: float or int
        """
        if float_ret:
            return float(kelvin * 1.8)
        return trunc(kelvin * 1.8)

    @staticmethod
    def to_reaumur(kelvin: float | int, /, *, float_ret=True) -> float | int:
        """
        Converts Kelvin to Réaumur, returning a float by default.
        If the float_ret parameter is False, it returns an approximate int value
        (using the math's module trunc function).
        :param kelvin: Kelvin value to be converted
        :param float_ret: Optional, True by default to return floats
        :return: float or int
        """
        if float_ret:
            return float((kelvin - 273.15) * 4 / 5)
        return trunc((kelvin - 273.15) * 4 / 5)

    @staticmethod
    def to_romer(kelvin: float | int, /, *, float_ret=True) -> float | int:
        """
        Converts Kelvin to Rømer, returning a float by default.
        If the float_ret parameter is False, it returns an approximate int value
        (using the math's module trunc function).
        :param kelvin: Kelvin value to be converted
        :param float_ret: Optional, True by default to return floats
        :return: float or int
        """
        if float_ret:
            return float((kelvin - 273.15) * (21 / 40) + 7.5)
        return trunc((kelvin - 273.15) * (21 / 40) + 7.5)


class Newton:
    """Provides conversion of Newton to other temperature scales"""

    @staticmethod
    def to_celsius(newton: float | int, /, *, float_ret=True) -> float | int:
        """
        Converts Newton to Celsius, returning a float by default.
        If the float_ret parameter is False, it returns an approximate int value
        (using the math's module trunc function).
        :param Newton: Newton value to be converted
        :param float_ret: Optional, True by default to return floats
        :return: float or int
        """
        if float_ret:
            return float(newton / 0.33)
        return trunc(newton / 0.33)

    @staticmethod
    def to_fahrenheit(
        newton: float | int, /, *, float_ret=True
    ) -> float | int:
        """
        Converts Newton to Fahrenheit, returning a float by default.
        If the float_ret parameter is False, it returns an approximate int value
        (using the math's module trunc function).
        :param Newton: Newton value to be converted
        :param float_ret: Optional, True by default to return floats
        :return: float or int
        """
        if float_ret:
            return float((newton * 5.4545) + 32.00)
        return trunc((newton * 5.4545) + 32.00)
