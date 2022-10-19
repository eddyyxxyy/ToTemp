#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Celsius:
    """Provides conversion of Celsius to other temperature types"""

    @staticmethod
    def to_delisle(celsius: float | int) -> float:
        """
        Converts Celsius to Delisle
        :param celsius: float | int
        :return: float
        """
        return (100 - celsius) * 3 / 2

    @staticmethod
    def to_fahrenheit(celsius: float | int) -> float:
        """
        Converts Celsius to Fahrenheit
        :param celsius: float | int
        :return: float
        """
        return celsius * 9 / 5 + 32

    @staticmethod
    def to_kelvin(celsius: float | int) -> float:
        """
        Converts Celsius to Kelvin
        :param celsius: float | int
        :return: float
        """
        return celsius + 273.15

    @staticmethod
    def to_newton(celsius: float | int) -> float:
        """
        Converts Celsius to Newton
        :param celsius: float | int
        :return: float
        """
        return celsius * 33 / 100

    @staticmethod
    def to_rankine(celsius: float | int) -> float:
        """
        Converts Celsius to Rankine
        :param celsius: float | int
        :return: float
        """
        return celsius * 9 / 5 + 491.67

    @staticmethod
    def to_reaumur(celsius: float | int):
        """
        Converts Celsius to Réaumur
        :param celsius: float | int
        :return: float
        """
        return celsius * 4 / 5

    @staticmethod
    def to_romer(celsius):
        """
        Converts Celsius to Rømer
        :param celsius: float | int
        :return: float
        """
        return celsius * 21 / 40 + 7.5
