#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from totemp import Celsius, Delisle, Fahrenheit, Kelvin


class TestToTemp:
    """Tests all methods of all Classes in temperature_types.py"""

    # Celsius to <other temp scale> tests
    def test_celsius_to_delisle(self) -> None:
        """Tests the result of the conversion Celsius to Delisle"""
        assert Celsius.to_delisle(20.25) == 119.625

    def test_celsius_to_delisle_default_type(self) -> None:
        """
        Tests the type of the value returned on the conversion Celsius to Delisle
        with default parameter values
        """
        assert isinstance(Celsius.to_delisle(68), float)

    def test_celsius_to_delisle_type_trunc_ret(self) -> None:
        """
        Tests the type of the value returned on the conversion Celsius to Delisle
        with default parameter set to False
        """
        assert isinstance(Celsius.to_delisle(20, float_ret=False), int)

    def test_celcius_to_fahrenheit(self) -> None:
        """Tests the result of the conversion Celsius to Fahrenheit"""
        assert Celsius.to_fahrenheit(41.985) == 107.57300000000001

    def test_celcius_to_fahrenheit_default_type(self) -> None:
        """
        Tests the type of the value returned on the conversion Celsius to Fahrenheit
        with default parameter values
        """
        assert isinstance(Celsius.to_fahrenheit(41), float)

    def test_celcius_to_fahrenheit_type_trunc_ret(self) -> None:
        """
        Tests the type of the value returned on the conversion Celsius to Fahrenheit
        with default parameter set to False
        """
        assert isinstance(Celsius.to_fahrenheit(41.985, float_ret=False), int)

    def test_celcius_to_kelvin(self) -> None:
        """Tests the result of the conversion Celsius to Kelvin"""
        assert Celsius.to_kelvin(72.111) == 345.26099999999997

    def test_celcius_to_kelvin_default_type(self) -> None:
        """
        Tests the type of the value returned on the conversion Celsius to Kelvin
        with default parameter values
        """
        assert isinstance(Celsius.to_kelvin(72), float)

    def test_celcius_to_kelvin_type_trunc_ret(self) -> None:
        """
        Tests the type of the value returned on the conversion Celsius to Kelvin
        with default parameter set to False
        """
        assert isinstance(Celsius.to_kelvin(72, float_ret=False), int)

    def test_celcius_to_newton(self) -> None:
        """Tests the result of the conversion Celsius to Newton"""
        assert Celsius.to_newton(144.9955) == 47.848515

    def test_celcius_to_newton_default_type(self) -> None:
        """
        Tests the type of the value returned on the conversion Celsius to Kelvin
        with default parameter values
        """
        assert isinstance(Celsius.to_newton(144), float)

    def test_celcius_to_newton_type_trunc_ret(self) -> None:
        """
        Tests the type of the value returned on the conversion Celsius to Kelvin
        with default parameter set to False
        """
        assert isinstance(Celsius.to_newton(144, float_ret=False), int)

    def test_celcius_to_rankine(self) -> None:
        """Tests the result of the conversion Celsius to Rankine"""
        assert Celsius.to_rankine(18.283832) == 524.5808976000001

    def test_celcius_to_rankine_default_type(self) -> None:
        """
        Tests the type of the value returned on the conversion Celsius to Rankine
        with default parameter values
        """
        assert isinstance(Celsius.to_rankine(18), float)

    def test_celcius_to_rankine_type_trunc_ret(self) -> None:
        """
        Tests the type of the value returned on the conversion Celsius to Rankine
        with default parameter set to False
        """
        assert isinstance(Celsius.to_rankine(18, float_ret=False), int)

    def test_celcius_to_reaumur(self) -> None:
        """Tests the result of the conversion Celsius to Réaumur"""
        assert Celsius.to_reaumur(123.212) == 98.56960000000001

    def test_celcius_to_reaumur_default_type(self) -> None:
        """
        Tests the type of the value returned on the conversion Celsius to Réaumur
        with default parameter values
        """
        assert isinstance(Celsius.to_reaumur(123), float)

    def test_celcius_to_reaumur_type_trunc_ret(self) -> None:
        """
        Tests the type of the value returned on the conversion Celsius to Réaumur
        with default parameter set to False
        """
        assert isinstance(Celsius.to_reaumur(123, float_ret=False), int)

    def test_celcius_to_romer(self) -> None:
        """Tests the result of the conversion Celsius to Rømer"""
        assert Celsius.to_romer(237.236438) == 132.04912995

    def test_celcius_to_romer_default_type(self) -> None:
        """
        Tests the type of the value returned on the conversion Celsius to Rømer
        with default parameter values
        """
        assert isinstance(Celsius.to_romer(237), float)

    def test_celcius_to_romer_type_trunc_ret(self) -> None:
        """
        Tests the type of the value returned on the conversion Celsius to Réaumur
        with default parameter set to False
        """
        assert isinstance(Celsius.to_romer(237, float_ret=False), int)

    # Fahrenheit to <other temp scale> tests
    def test_fahrenheit_to_celcius(self) -> None:
        """Tests the result of the conversion Fahrenheit to Celsius"""
        assert Fahrenheit.to_celsius(107.57300000000001) == 41.985

    def test_fahrenheit_to_celcius_default_type(self) -> None:
        """
        Tests the type of the value returned on the conversion Fahrenheit to Celsius
        with default parameter values
        """
        assert isinstance(Fahrenheit.to_celsius(107), float)

    def test_fahrenheit_to_celcius_type_trunc_ret(self) -> None:
        """
        Tests the type of the value returned on the conversion Fahrenheit to Celsius
        with default parameter set to False
        """
        assert isinstance(
            Fahrenheit.to_celsius(107.57300000000001, float_ret=False), int
        )

    def test_fahrenheit_to_delisle(self) -> None:
        """Tests the result of the conversion Fahrenheit to Delisle"""
        assert Fahrenheit.to_delisle(20.25) == 159.79166666666666

    def test_fahrenheit_to_delisle_default_type(self) -> None:
        """
        Tests the type of the value returned on the conversion Fahrenheit to Delisle
        with default parameter values
        """
        assert isinstance(Fahrenheit.to_delisle(20), float)

    def test_fahrenheit_to_delisle_type_trunc_ret(self) -> None:
        """
        Tests the type of the value returned on the conversion Fahrenheit to Delisle
        with default parameter set to False
        """
        assert isinstance(Fahrenheit.to_delisle(20.25, float_ret=False), int)

    def test_fahrenheit_to_kelvin(self) -> None:
        """Tests the result of the conversion Fahrenheit to Kelvin"""
        assert Fahrenheit.to_kelvin(123.4555) == 323.9586111111111

    def test_fahrenheit_to_kelvin_default_type(self) -> None:
        """
        Tests the type of the value returned on the conversion Fahrenheit to Kelvin
        with default parameter values
        """
        assert isinstance(Fahrenheit.to_kelvin(123), float)

    def test_fahrenheit_to_kelvin_type_trunc_ret(self) -> None:
        """
        Tests the type of the value returned on the conversion Fahrenheit to Kelvin
        with default parameter set to False
        """
        assert isinstance(Fahrenheit.to_kelvin(123.4555, float_ret=False), int)

    def test_fahrenheit_to_newton(self) -> None:
        """Tests the result of the conversion Fahrenheit to Newton"""
        assert Fahrenheit.to_newton(58.9011) == 4.931868333333333

    def test_fahrenheit_to_newton_default_type(self) -> None:
        """
        Tests the type of the value returned on the conversion Fahrenheit to Newton
        with default parameter values
        """
        assert isinstance(Fahrenheit.to_newton(58), float)

    def test_fahrenheit_to_newton_type_trunc_ret(self) -> None:
        """
        Tests the type of the value returned on the conversion Fahrenheit to Newton
        with default parameter set to False
        """
        assert isinstance(Fahrenheit.to_newton(58.9011, float_ret=False), int)

    def test_fahrenheit_to_rankine(self) -> None:
        """Tests the result of the conversion Fahrenheit to Rankine"""
        assert Fahrenheit.to_rankine(12.35343264363) == 472.02343264363003

    def test_fahrenheit_to_rankine_default_type(self) -> None:
        """
        Tests the type of the value returned on the conversion Fahrenheit to Rankine
        with default parameter values
        """
        assert isinstance(Fahrenheit.to_rankine(12), float)

    def test_fahrenheit_to_rankine_type_trunc_ret(self) -> None:
        """
        Tests the type of the value returned on the conversion Fahrenheit to Rankine
        with default parameter set to False
        """
        assert isinstance(
            Fahrenheit.to_rankine(12.35343264363, float_ret=False), int
        )

    def test_fahrenheit_to_reaumur(self) -> None:
        """Tests the result of the conversion Fahrenheit to Réaumur"""
        assert Fahrenheit.to_reaumur(1001.03438221) == 430.68194764888887

    def test_fahrenheit_to_reaumur_default_type(self) -> None:
        """
        Tests the type of the value returned on the conversion Fahrenheit to Réaumur
        with default parameter values
        """
        assert isinstance(Fahrenheit.to_reaumur(1001), float)

    def test_fahrenheit_to_reaumur_type_trunc_ret(self) -> None:
        """
        Tests the type of the value returned on the conversion Fahrenheit to Réaumur
        with default parameter set to False
        """
        assert isinstance(
            Fahrenheit.to_reaumur(1001.03438221, float_ret=False), int
        )

    def test_fahrenheit_to_romer(self) -> None:
        """Tests the result of the conversion Fahrenheit to Rømer"""
        assert Fahrenheit.to_romer(395.323729) == 113.46942095833334

    def test_fahrenheit_to_romer_default_type(self) -> None:
        """
        Tests the type of the value returned on the conversion Fahrenheit to Rømer
        with default parameter values
        """
        assert isinstance(Fahrenheit.to_romer(395), float)

    def test_fahrenheit_to_romer_type_trunc_ret(self) -> None:
        """
        Tests the type of the value returned on the conversion Fahrenheit to Rømer
        with default parameter set to False
        """
        assert isinstance(
            Fahrenheit.to_romer(395.323729, float_ret=False), int
        )

    # Kelvin to <other temp scale> tests
    def test_kelvin_to_celsius(self) -> None:
        """Tests the result of the convertion Kelvin to Celsius"""
        assert Kelvin.to_celsius(67.498259) == -205.65174099999996

    def test_kelvin_to_celsius_default_type(self) -> None:
        """
        Tests the type of the value returned on the convertion Kelvin to Celsius
        with default parameter values
        """
        assert isinstance(Kelvin.to_celsius(10), float)

    def test_kelvin_to_celsius_type_trunc_ret(self) -> None:
        """
        Tests the type of the value returned on the convertion Kelvin to Celsius
        with default parameter setted to False
        """
        assert isinstance(Kelvin.to_celsius(10.498259, float_ret=False), int)

    def test_kelvin_to_delisle(self) -> None:
        """Tests the result of the convertion Kelvin to Delisle"""
        assert Kelvin.to_delisle(10.568) == 543.873

    def test_kelvin_to_delisle_default_type(self) -> None:
        """
        Tests the type of the value returned on the convertion Kelvin to Delisle
        with default parameter values
        """
        assert isinstance(Kelvin.to_delisle(10), float)

    def test_kelvin_to_delisle_type_trunc_ret(self) -> None:
        """
        Tests the type of the value returned on the convertion Kelvin to Delisle
        with default parameter setted to False
        """
        assert isinstance(Kelvin.to_delisle(10.498259, float_ret=False), int)

    def test_kelvin_to_fahrenheit(self) -> None:
        """Tests the result of the convertion Kelvin to Fahrenheit"""
        assert Kelvin.to_fahrenheit(44.28137746) == -379.963520572

    def test_kelvin_to_fahrenheit_default_type(self) -> None:
        """
        Tests the type of the value returned on the convertion Kelvin to Fahrenheit
        with default parameter values
        """
        assert isinstance(Kelvin.to_fahrenheit(10), float)

    def test_kelvin_to_fahrenheit_type_trunc_ret(self) -> None:
        """
        Tests the type of the value returned on the convertion Kelvin to Fahrenheit
        with default parameter setted to False
        """
        assert isinstance(Kelvin.to_fahrenheit(25.8456, float_ret=False), int)

    def test_kelvin_to_newton(self) -> None:
        """Tests the result of the convertion Kelvin to Newton"""
        assert Kelvin.to_newton(44.28137746) == -75.52664543819999

    def test_kelvin_to_newton_default_type(self) -> None:
        """
        Tests the type of the value returned on the convertion Kelvin to Newton
        with default parameter values
        """
        assert isinstance(Kelvin.to_newton(10), float)

    def test_kelvin_to_newton_type_trunc_ret(self) -> None:
        """
        Tests the type of the value returned on the convertion Kelvin to Newton
        with default parameter setted to False
        """
        assert isinstance(Kelvin.to_newton(25.8456, float_ret=False), int)

    def test_kelvin_to_rankine(self) -> None:
        """Tests the result of the convertion Kelvin to Rankine"""
        assert Kelvin.to_rankine(44.28137746) == 79.70647942800001

    def test_kelvin_to_rankine_default_type(self) -> None:
        """
        Tests the type of the value returned on the convertion Kelvin to Rankine
        with default parameter values
        """
        assert isinstance(Kelvin.to_rankine(10), float)

    def test_kelvin_to_rankine_type_trunc_ret(self) -> None:
        """
        Tests the type of the value returned on the convertion Kelvin to Rankine
        with default parameter setted to False
        """
        assert isinstance(Kelvin.to_rankine(25.8456, float_ret=False), int)

    def test_kelvin_to_reaumur(self) -> None:
        """Tests the result of the convertion Kelvin to Réaumur"""
        assert Kelvin.to_reaumur(44.28137746) == -183.094898032

    def test_kelvin_to_reaumur_default_type(self) -> None:
        """
        Tests the type of the value returned on the convertion Kelvin to Réaumur
        with default parameter values
        """
        assert isinstance(Kelvin.to_reaumur(10), float)

    def test_kelvin_to_reaumur_type_trunc_ret(self) -> None:
        """
        Tests the type of the value returned on the convertion Kelvin to Réaumur
        with default parameter setted to False
        """
        assert isinstance(Kelvin.to_reaumur(25.8456, float_ret=False), int)

    def test_kelvin_to_romer(self) -> None:
        """Tests the result of the convertion Kelvin to Rømer"""
        assert Kelvin.to_romer(44.28137746) == -112.6560268335

    def test_kelvin_to_romer_default_type(self) -> None:
        """
        Tests the type of the value returned on the convertion Kelvin to Rømer
        with default parameter values
        """
        assert isinstance(Kelvin.to_romer(10), float)

    def test_kelvin_to_romer_type_trunc_ret(self) -> None:
        """
        Tests the type of the value returned on the convertion Kelvin to Rømer
        with default parameter setted to False
        """
        assert isinstance(Kelvin.to_romer(25.8456, float_ret=False), int)

    # Delisle to <other temp scale> tests
    def test_delisle_to_celsius(self) -> None:
        """Tests the result of the conversion Delisle to Celsius"""
        assert Delisle.to_celsius(27.29828) == 81.80114666666667

    def test_delisle_to_celsius_default_type(self) -> None:
        """
        Tests the type of the value returned on the conversion Delisle to Celsius
        with default parameter values
        """
        assert isinstance(Delisle.to_celsius(15), float)

    def test_delisle_to_celsius_type_trunc_ret(self) -> None:
        """
        Tests the type of the value returned on the conversion Delisle to Celsius
        with default parameter set to False
        """
        assert isinstance(Delisle.to_celsius(27.29828, float_ret=False), int)

    def test_delisle_to_fahrenheit(self) -> None:
        """Tests the result of the conversion Delisle to Fahrenheit"""
        assert Delisle.to_fahrenheit(10.28723) == 199.655324

    def test_delisle_to_fahrenheit_default_type(self) -> None:
        """
        Tests the type of the value returned on the conversion Delisle to Fahrenheit
        with default parameter values
        """
        assert isinstance(Delisle.to_fahrenheit(10), float)

    def test_delisle_to_fahrenheit_type_trunc_ret(self) -> None:
        """
        Tests the type of the value returned on the conversion Delisle to Fahrenheit
        with default parameter set to False
        """
        assert isinstance(
            Delisle.to_fahrenheit(10.28723, float_ret=False), int
        )

    def test_delisle_to_kelvin(self) -> None:
        """Tests the result of the conversion Delisle to Kelvin"""
        assert Delisle.to_kelvin(99.227339) == 306.9984406666666

    def test_delisle_to_kelvin_default_type(self) -> None:
        """
        Tests the type of the value returned on the conversion Delisle to Kelvin
        with default parameter values
        """
        assert isinstance(Delisle.to_kelvin(99), float)

    def test_delisle_to_kelvin_type_trunc_ret(self) -> None:
        """
        Tests the type of the value returned on the conversion Delisle to Kelvin
        with default parameter set to False
        """
        assert isinstance(Delisle.to_kelvin(99.227339, float_ret=False), int)

    def test_delisle_to_newton(self) -> None:
        """Tests the result of the conversion Delisle to Newton"""
        assert Delisle.to_newton(1.98327392917266655) == 32.563679735582014

    def test_delisle_to_newton_default_type(self) -> None:
        """
        Tests the type of the value returned on the conversion Delisle to Newton
        with default parameter values
        """
        assert isinstance(Delisle.to_newton(1), float)

    def test_delisle_to_newton_type_trunc_ret(self) -> None:
        """
        Tests the type of the value returned on the conversion Delisle to Newton
        with default parameter set to False
        """
        assert isinstance(
            Delisle.to_newton(1.98327392917266655, float_ret=False), int
        )

    def test_delisle_to_rankine(self) -> None:
        """Tests the result of the conversion Delisle to Rankine"""
        assert Delisle.to_rankine(22.3862619237) == 644.8064856915599

    def test_delisle_to_rankine_default_type(self) -> None:
        """
        Tests the type of the value returned on the conversion Delisle to Rankine
        with default parameter values
        """
        assert isinstance(Delisle.to_rankine(22), float)

    def test_delisle_to_rankine_type_trunc_ret(self) -> None:
        """
        Tests the type of the value returned on the conversion Delisle to Rankine
        with default parameter set to False
        """
        assert isinstance(
            Delisle.to_rankine(22.3862619237, float_ret=False), int
        )

    def test_delisle_to_reaumur(self) -> None:
        """Tests the result of the conversion Delisle to Réaumur"""
        assert Delisle.to_reaumur(57.543) == 49.3104

    def test_delisle_to_reaumur_default_type(self) -> None:
        """
        Tests the type of the value returned on the conversion Delisle to Réaumur
        with default parameter values
        """
        assert isinstance(Delisle.to_reaumur(57), float)

    def test_delisle_to_reaumur_type_trunc_ret(self) -> None:
        """
        Tests the type of the value returned on the conversion Delisle to Réaumur
        with default parameter set to False
        """
        assert isinstance(Delisle.to_reaumur(57.543, float_ret=False), int)

    def test_delisle_to_romer(self) -> None:
        """Tests the result of the conversion Delisle to Rømer"""
        assert Delisle.to_romer(1324.799) == -403.67965000000004

    def test_delisle_to_romer_default_type(self) -> None:
        """
        Tests the type of the value returned on the conversion Delisle to Rømer
        with default parameter values
        """
        assert isinstance(Delisle.to_romer(1324), float)

    def test_delisle_to_romer_type_trunc_ret(self) -> None:
        """
        Tests the type of the value returned on the conversion Delisle to Rømer
        with default parameter set to False
        """
        assert isinstance(Delisle.to_romer(1324.799, float_ret=False), int)
