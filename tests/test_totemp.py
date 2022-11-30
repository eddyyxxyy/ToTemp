#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from random import randint, uniform

from tests.test_funcs import (
    func_to_test_dynamic_returns,
    func_to_test_precise_rounded_results,
)
from totemp import (
    Celsius,
    Delisle,
    Fahrenheit,
    Kelvin,
    Newton,
    Rankine,
    Reaumur,
    Romer,
)


class TestToTemp:
    """Tests all methods of all Classes in temperature_types.py"""

    # Celsius to <other temp scale> tests
    def test_dynamic_type_return_celsius_to_fahrenheit(self) -> None:
        """Tests the dynamic typed results of the conversion Celsius to Fahrenheit"""
        temps = (
            Celsius(randint(1, 20)).to_fahrenheit(),
            Celsius(uniform(0.0, 20.0)).to_fahrenheit(),
        )
        errors = func_to_test_dynamic_returns(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_precise_rounded_celsius_to_fahrenheit(self) -> None:
        """Tests the rounded and precise result of the conversion Celsius to Fahrenheit"""
        temps = (
            Celsius(25).precise().to_fahrenheit(),
            Fahrenheit(value=77.00000),
            Celsius(25.25).rounded().to_fahrenheit(),
            Fahrenheit(value=77),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_dynamic_type_return_celsius_to_delisle(self) -> None:
        """Tests the dynamic typed results of the conversion Celsius to Delisle"""
        temps = (
            Celsius(randint(1, 20)).to_delisle(),
            Celsius(uniform(0.0, 20.0)).to_delisle(),
        )
        errors = func_to_test_dynamic_returns(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_precise_rounded_celsius_to_delisle(self) -> None:
        """Tests the rounded and precise result of the conversion Celsius to Delisle"""
        temps = (
            Celsius(25).precise().to_delisle(),
            Delisle(value=-62.50000),
            Celsius(25.25).rounded().to_delisle(),
            Delisle(value=-62),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_dynamic_type_return_celsius_to_kelvin(self) -> None:
        """Tests the dynamic typed results of the conversion Celsius to Kelvin"""
        temps = (
            Celsius(randint(1, 20)).to_kelvin(),
            Celsius(uniform(0.0, 20.0)).to_kelvin(),
        )
        errors = func_to_test_dynamic_returns(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_precise_rounded_celsius_to_kelvin(self) -> None:
        """Tests the rounded and precise result of the conversion Celsius to Kelvin"""
        temps = (
            Celsius(25).precise().to_kelvin(),
            Kelvin(value=298.1500),
            Celsius(25.25).rounded().to_kelvin(),
            Kelvin(value=298),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_dynamic_type_return_celsius_to_newton(self) -> None:
        """Tests the dynamic typed results of the conversion Celsius to Newton"""
        temps = (
            Celsius(randint(1, 20)).to_newton(),
            Celsius(uniform(0.0, 20.0)).to_newton(),
        )
        errors = func_to_test_dynamic_returns(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_precise_rounded_celsius_to_newton(self) -> None:
        """Tests the rounded and precise result of the conversion Celsius to Newton"""
        temps = (
            Celsius(25).precise().to_newton(),
            Newton(value=8.250000),
            Celsius(25.25).rounded().to_newton(),
            Newton(value=8),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_celsius_to_rankine_default_type(self) -> None:
        """
        Tests the type of the value returned on the conversion Celsius to Rankine
        with default parameter values
        """
        assert isinstance(Celsius.to_rankine(18), float)

    def test_celsius_to_rankine_type_trunc_ret(self) -> None:
        """
        Tests the type of the value returned on the conversion Celsius to Rankine
        with default parameter set to False
        """
        assert isinstance(Celsius.to_rankine(18, float_ret=False), int)

    def test_celsius_to_reaumur(self) -> None:
        """Tests the result of the conversion Celsius to Réaumur"""
        assert Celsius.to_reaumur(123.212) == 98.56960000000001

    def test_celsius_to_reaumur_default_type(self) -> None:
        """
        Tests the type of the value returned on the conversion Celsius to Réaumur
        with default parameter values
        """
        assert isinstance(Celsius.to_reaumur(123), float)

    def test_celsius_to_reaumur_type_trunc_ret(self) -> None:
        """
        Tests the type of the value returned on the conversion Celsius to Réaumur
        with default parameter set to False
        """
        assert isinstance(Celsius.to_reaumur(123, float_ret=False), int)

    def test_celsius_to_romer(self) -> None:
        """Tests the result of the conversion Celsius to Rømer"""
        assert Celsius.to_romer(237.236438) == 132.04912995

    def test_celsius_to_romer_default_type(self) -> None:
        """
        Tests the type of the value returned on the conversion Celsius to Rømer
        with default parameter values
        """
        assert isinstance(Celsius.to_romer(237), float)

    def test_celsius_to_romer_type_trunc_ret(self) -> None:
        """
        Tests the type of the value returned on the conversion Celsius to Réaumur
        with default parameter set to False
        """
        assert isinstance(Celsius.to_romer(237, float_ret=False), int)

    # Fahrenheit to <other temp scale> tests
    def test_fahrenheit_to_celsius(self) -> None:
        """Tests the result of the conversion Fahrenheit to Celsius"""
        assert Fahrenheit.to_celsius(107.57300000000001) == 41.985

    def test_fahrenheit_to_celsius_default_type(self) -> None:
        """
        Tests the type of the value returned on the conversion Fahrenheit to Celsius
        with default parameter values
        """
        assert isinstance(Fahrenheit.to_celsius(107), float)

    def test_fahrenheit_to_celsius_type_trunc_ret(self) -> None:
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
        """Tests the result of the conversion Kelvin to Celsius"""
        assert Kelvin.to_celsius(67.498259) == -205.65174099999996

    def test_kelvin_to_celsius_default_type(self) -> None:
        """
        Tests the type of the value returned on the conversion Kelvin to Celsius
        with default parameter values
        """
        assert isinstance(Kelvin.to_celsius(10), float)

    def test_kelvin_to_celsius_type_trunc_ret(self) -> None:
        """
        Tests the type of the value returned on the conversion Kelvin to Celsius
        with default parameter set to False
        """
        assert isinstance(Kelvin.to_celsius(10.498259, float_ret=False), int)

    def test_kelvin_to_delisle(self) -> None:
        """Tests the result of the conversion Kelvin to Delisle"""
        assert Kelvin.to_delisle(10.568) == 543.873

    def test_kelvin_to_delisle_default_type(self) -> None:
        """
        Tests the type of the value returned on the conversion Kelvin to Delisle
        with default parameter values
        """
        assert isinstance(Kelvin.to_delisle(10), float)

    def test_kelvin_to_delisle_type_trunc_ret(self) -> None:
        """
        Tests the type of the value returned on the conversion Kelvin to Delisle
        with default parameter set to False
        """
        assert isinstance(Kelvin.to_delisle(10.498259, float_ret=False), int)

    def test_kelvin_to_fahrenheit(self) -> None:
        """Tests the result of the conversion Kelvin to Fahrenheit"""
        assert Kelvin.to_fahrenheit(44.28137746) == -379.963520572

    def test_kelvin_to_fahrenheit_default_type(self) -> None:
        """
        Tests the type of the value returned on the conversion Kelvin to Fahrenheit
        with default parameter values
        """
        assert isinstance(Kelvin.to_fahrenheit(10), float)

    def test_kelvin_to_fahrenheit_type_trunc_ret(self) -> None:
        """
        Tests the type of the value returned on the conversion Kelvin to Fahrenheit
        with default parameter set to False
        """
        assert isinstance(Kelvin.to_fahrenheit(25.8456, float_ret=False), int)

    def test_kelvin_to_newton(self) -> None:
        """Tests the result of the conversion Kelvin to Newton"""
        assert Kelvin.to_newton(44.28137746) == -75.52664543819999

    def test_kelvin_to_newton_default_type(self) -> None:
        """
        Tests the type of the value returned on the conversion Kelvin to Newton
        with default parameter values
        """
        assert isinstance(Kelvin.to_newton(10), float)

    def test_kelvin_to_newton_type_trunc_ret(self) -> None:
        """
        Tests the type of the value returned on the conversion Kelvin to Newton
        with default parameter set to False
        """
        assert isinstance(Kelvin.to_newton(25.8456, float_ret=False), int)

    def test_kelvin_to_rankine(self) -> None:
        """Tests the result of the conversion Kelvin to Rankine"""
        assert Kelvin.to_rankine(44.28137746) == 79.70647942800001

    def test_kelvin_to_rankine_default_type(self) -> None:
        """
        Tests the type of the value returned on the conversion Kelvin to Rankine
        with default parameter values
        """
        assert isinstance(Kelvin.to_rankine(10), float)

    def test_kelvin_to_rankine_type_trunc_ret(self) -> None:
        """
        Tests the type of the value returned on the conversion Kelvin to Rankine
        with default parameter set to False
        """
        assert isinstance(Kelvin.to_rankine(25.8456, float_ret=False), int)

    def test_kelvin_to_reaumur(self) -> None:
        """Tests the result of the conversion Kelvin to Réaumur"""
        assert Kelvin.to_reaumur(44.28137746) == -183.094898032

    def test_kelvin_to_reaumur_default_type(self) -> None:
        """
        Tests the type of the value returned on the conversion Kelvin to Réaumur
        with default parameter values
        """
        assert isinstance(Kelvin.to_reaumur(10), float)

    def test_kelvin_to_reaumur_type_trunc_ret(self) -> None:
        """
        Tests the type of the value returned on the conversion Kelvin to Réaumur
        with default parameter set to False
        """
        assert isinstance(Kelvin.to_reaumur(25.8456, float_ret=False), int)

    def test_kelvin_to_romer(self) -> None:
        """Tests the result of the conversion Kelvin to Rømer"""
        assert Kelvin.to_romer(44.28137746) == -112.6560268335

    def test_kelvin_to_romer_default_type(self) -> None:
        """
        Tests the type of the value returned on the conversion Kelvin to Rømer
        with default parameter values
        """
        assert isinstance(Kelvin.to_romer(10), float)

    def test_kelvin_to_romer_type_trunc_ret(self) -> None:
        """
        Tests the type of the value returned on the conversion Kelvin to Rømer
        with default parameter set to False
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

    # Newton to <other temp scale> tests
    def test_dynamic_type_return_newton_to_celsius(self) -> None:
        """Tests the dynamic typed results of the conversion Newton to Celsius"""
        temps = (
            Newton(randint(1, 20)).to_celsius(),
            Newton(uniform(0.0, 20.0)).to_celsius(),
        )
        errors = func_to_test_dynamic_returns(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_precise_rounded_newton_to_celsius(self) -> None:
        """Tests the rounded and precise result of the conversion Newton to Celsius"""
        temps = (
            Newton(25).precise().to_celsius(),
            Celsius(value=75.75757575757575),
            Newton(25.25).rounded().to_celsius(),
            Celsius(value=75),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_dynamic_type_return_newton_to_fahrenheit(self) -> None:
        """Tests the dynamic typed results of the conversion Newton to Fahrenheit"""
        temps = (
            Newton(randint(1, 20)).to_fahrenheit(),
            Newton(uniform(0.0, 20.0)).to_fahrenheit(),
        )
        errors = func_to_test_dynamic_returns(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_precise_rounded_newton_to_fahrenheit(self) -> None:
        """Tests the rounded and precise result of the conversion Newton to Fahrenheit"""
        temps = (
            Newton(25).precise().to_fahrenheit(),
            Fahrenheit(value=168.36363636363637),
            Newton(25.25).rounded().to_fahrenheit(),
            Fahrenheit(value=168),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_dynamic_type_return_newton_to_delisle(self) -> None:
        """Tests the dynamic typed results of the conversion Newton to Delisle"""
        temps = (
            Newton(randint(1, 20)).to_delisle(),
            Newton(uniform(0.0, 20.0)).to_delisle(),
        )
        errors = func_to_test_dynamic_returns(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_precise_rounded_newton_to_delisle(self) -> None:
        """Tests the rounded and precise result of the conversion Newton to Delisle"""
        temps = (
            Newton(25).precise().to_delisle(),
            Delisle(value=13.637499999999989),
            Newton(25.25).rounded().to_delisle(),
            Delisle(value=13),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_dynamic_type_return_newton_to_rankine(self) -> None:
        """Tests the dynamic typed results of the conversion Newton to Rankine"""
        temps = (
            Newton(randint(1, 20)).to_rankine(),
            Newton(uniform(0.0, 20.0)).to_rankine(),
        )
        errors = func_to_test_dynamic_returns(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_precise_rounded_newton_to_rankine(self) -> None:
        """Tests the rounded and precise result of the conversion Newton to Rankine"""
        temps = (
            Newton(25).precise().to_rankine(),
            Rankine(value=628.0325),
            Newton(25.25).rounded().to_rankine(),
            Rankine(value=628),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_dynamic_type_return_newton_to_kelvin(self) -> None:
        """Tests the dynamic typed results of the conversion Newton to Kelvin"""
        temps = (
            Newton(randint(1, 20)).to_kelvin(),
            Newton(uniform(0.0, 20.0)).to_kelvin(),
        )
        errors = func_to_test_dynamic_returns(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_precise_rounded_newton_to_kelvin(self) -> None:
        """Tests the rounded and precise result of the conversion Newton to Kelvin"""
        temps = (
            Newton(25).precise().to_kelvin(),
            Kelvin(value=348.9075757575757),
            Newton(25.25).rounded().to_kelvin(),
            Kelvin(value=348),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_dynamic_type_return_newton_to_romer(self) -> None:
        """Tests the dynamic typed results of the conversion Newton to Rømer"""
        temps = (
            Newton(randint(1, 20)).to_romer(),
            Newton(uniform(0.0, 20.0)).to_romer(),
        )
        errors = func_to_test_dynamic_returns(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_precise_rounded_newton_to_romer(self) -> None:
        """Tests the rounded and precise result of the conversion Newton to Rømer"""
        temps = (
            Newton(25).precise().to_romer(),
            Romer(value=47.27272727272727),
            Newton(25.25).rounded().to_romer(),
            Romer(value=47),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_dynamic_type_return_newton_to_reaumur(self) -> None:
        """Tests the dynamic typed results of the conversion Newton to Réaumur"""
        temps = (
            Newton(randint(1, 20)).to_reaumur(),
            Newton(uniform(0.0, 20.0)).to_reaumur(),
        )
        errors = func_to_test_dynamic_returns(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_precise_rounded_newton_to_reaumur(self) -> None:
        """Tests the rounded and precise result of the conversion Newton to Réaumur"""
        temps = (
            Newton(25).precise().to_reaumur(),
            Reaumur(value=60.60606060606061),
            Newton(25.25).rounded().to_reaumur(),
            Reaumur(value=60),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    # Rankine to <other temp scale> tests
    def test_dynamic_type_return_rankine_to_celsius(self) -> None:
        """Tests the dynamic typed results of the conversion Rankine to Celsius"""
        temps = (
            Rankine(randint(1, 20)).to_celsius(),
            Rankine(uniform(0.0, 20.0)).to_celsius(),
        )
        errors = func_to_test_dynamic_returns(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_precise_rounded_rankine_to_celsius(self) -> None:
        """Tests the rounded and precise result of the conversion Rankine to Celsius"""
        temps = (
            Rankine(25).precise().to_celsius(),
            Celsius(value=-259.2611111111111),
            Rankine(25.25).rounded().to_celsius(),
            Celsius(value=-259),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_dynamic_type_return_rankine_to_fahrenheit(self) -> None:
        """Tests the dynamic typed results of the conversion Rankine to Fahrenheit"""
        temps = (
            Rankine(randint(1, 20)).to_fahrenheit(),
            Rankine(uniform(0.0, 20.0)).to_fahrenheit(),
        )
        errors = func_to_test_dynamic_returns(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_precise_rounded_rankine_to_fahrenheit(self) -> None:
        """Tests the rounded and precise result of the conversion Rankine to Fahrenheit"""
        temps = (
            Rankine(25).precise().to_fahrenheit(),
            Fahrenheit(value=-434.67),
            Rankine(25.25).rounded().to_fahrenheit(),
            Fahrenheit(value=-434),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_dynamic_type_return_rankine_to_delisle(self) -> None:
        """Tests the dynamic typed results of the conversion Rankine to Delisle"""
        temps = (
            Rankine(randint(1, 20)).to_delisle(),
            Rankine(uniform(0.0, 20.0)).to_delisle(),
        )
        errors = func_to_test_dynamic_returns(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_precise_rounded_rankine_to_delisle(self) -> None:
        """Tests the rounded and precise result of the conversion Rankine to Delisle"""
        temps = (
            Rankine(25).precise().to_delisle(),
            Delisle(value=538.8916666666667),
            Rankine(25.25).rounded().to_delisle(),
            Delisle(value=538),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_dynamic_type_return_rankine_to_kelvin(self) -> None:
        """Tests the dynamic typed results of the conversion Rankine to Kelvin"""
        temps = (
            Rankine(randint(1, 20)).to_kelvin(),
            Rankine(uniform(0.0, 20.0)).to_kelvin(),
        )
        errors = func_to_test_dynamic_returns(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_precise_rounded_rankine_to_kelvin(self) -> None:
        """Tests the rounded and precise result of the conversion Rankine to Kelvin"""
        temps = (
            Rankine(25).precise().to_kelvin(),
            Kelvin(value=13.88888888888889),
            Rankine(25.25).rounded().to_kelvin(),
            Kelvin(value=13),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_dynamic_type_return_rankine_to_newton(self) -> None:
        """Tests the dynamic typed results of the conversion Rankine to Newton"""
        temps = (
            Rankine(randint(1, 20)).to_newton(),
            Rankine(uniform(0.0, 20.0)).to_newton(),
        )
        errors = func_to_test_dynamic_returns(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_precise_rounded_rankine_to_newton(self) -> None:
        """Tests the rounded and precise result of the conversion Rankine to Newton"""
        temps = (
            Rankine(25).precise().to_newton(),
            Newton(value=-85.55616666666667),
            Rankine(25.25).rounded().to_newton(),
            Newton(value=-85),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_dynamic_type_return_rankine_to_reaumur(self) -> None:
        """Tests the dynamic typed results of the conversion Rankine to Réaumur"""
        temps = (
            Rankine(randint(1, 20)).to_reaumur(),
            Rankine(uniform(0.0, 20.0)).to_reaumur(),
        )
        errors = func_to_test_dynamic_returns(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_precise_rounded_rankine_to_reaumur(self) -> None:
        """Tests the rounded and precise result of the conversion Rankine to Réaumur"""
        temps = (
            Rankine(25).precise().to_reaumur(),
            Reaumur(value=-207.4088888888889),
            Rankine(25.25).rounded().to_reaumur(),
            Reaumur(value=-207),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_dynamic_type_return_rankine_to_romer(self) -> None:
        """Tests the dynamic typed results of the conversion Rankine to Rømer"""
        temps = (
            Rankine(randint(1, 20)).to_romer(),
            Rankine(uniform(0.0, 20.0)).to_romer(),
        )
        errors = func_to_test_dynamic_returns(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_precise_rounded_rankine_to_romer(self) -> None:
        """Tests the rounded and precise result of the conversion Rankine to Rømer"""
        temps = (
            Rankine(25).precise().to_romer(),
            Romer(value=-128.61208333333335),
            Rankine(25.25).rounded().to_romer(),
            Romer(value=-128),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))
