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

    def test_dynamic_type_return_celsius_to_rankine(self) -> None:
        """Tests the dynamic typed results of the conversion Celsius to Rankine"""
        temps = (
            Celsius(randint(1, 20)).to_rankine(),
            Celsius(uniform(0.0, 20.0)).to_rankine(),
        )
        errors = func_to_test_dynamic_returns(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_precise_rounded_celsius_to_rankine(self) -> None:
        """Tests the rounded and precise result of the conversion Celsius to Rankine"""
        temps = (
            Celsius(25).precise().to_rankine(),
            Rankine(value=536.6700000000001),
            Celsius(25.25).rounded().to_rankine(),
            Rankine(value=536),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_dynamic_type_return_celsius_to_reaumur(self) -> None:
        """Tests the dynamic typed results of the conversion Celsius to Réaumur"""
        temps = (
            Celsius(randint(1, 20)).to_reaumur(),
            Celsius(uniform(0.0, 20.0)).to_reaumur(),
        )
        errors = func_to_test_dynamic_returns(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_precise_rounded_celsius_to_reaumur(self) -> None:
        """Tests the rounded and precise result of the conversion Celsius to Réaumur"""
        temps = (
            Celsius(25).precise().to_reaumur(),
            Reaumur(value=20.00000),
            Celsius(25.25).rounded().to_reaumur(),
            Reaumur(value=20),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_dynamic_type_return_celsius_to_romer(self) -> None:
        """Tests the dynamic typed results of the conversion Celsius to Rømer"""
        temps = (
            Celsius(randint(1, 20)).to_romer(),
            Celsius(uniform(0.0, 20.0)).to_romer(),
        )
        errors = func_to_test_dynamic_returns(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_precise_rounded_celsius_to_romer(self) -> None:
        """Tests the rounded and precise result of the conversion Celsius to Rømer"""
        temps = (
            Celsius(25).precise().to_romer(),
            Romer(value=20.62500),
            Celsius(25.25).rounded().to_romer(),
            Romer(value=20),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    # Fahrenheit to <other temp scale> tests
    def test_dynamic_type_return_fahrenheit_to_celsius(self) -> None:
        """Tests the dynamic typed results of the conversion Fahrenheit to Celsius"""
        temps = (
            Fahrenheit(randint(1, 20)).to_celsius(),
            Fahrenheit(uniform(0.0, 20.0)).to_celsius(),
        )
        errors = func_to_test_dynamic_returns(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_precise_rounded_fahrenheit_to_celsius(self) -> None:
        """Tests the rounded and precise result of the conversion Fahrenheit to Celsius"""
        temps = (
            Fahrenheit(25).precise().to_celsius(),
            Celsius(value=-3.888888888888889),
            Fahrenheit(25.25).rounded().to_celsius(),
            Celsius(value=-3),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_dynamic_type_return_fahrenheit_to_delisle(self) -> None:
        """Tests the dynamic typed results of the conversion Fahrenheit to Delisle"""
        temps = (
            Fahrenheit(randint(1, 20)).to_delisle(),
            Fahrenheit(uniform(0.0, 20.0)).to_delisle(),
        )
        errors = func_to_test_dynamic_returns(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_precise_rounded_fahrenheit_to_delisle(self) -> None:
        """Tests the rounded and precise result of the conversion Fahrenheit to Delisle"""
        temps = (
            Fahrenheit(25).precise().to_delisle(),
            Delisle(value=155.83333333333334),
            Fahrenheit(25.25).rounded().to_delisle(),
            Delisle(value=155),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_dynamic_type_return_fahrenheit_to_kelvin(self) -> None:
        """Tests the dynamic typed results of the conversion Fahrenheit to Kelvin"""
        temps = (
            Fahrenheit(randint(1, 20)).to_kelvin(),
            Fahrenheit(uniform(0.0, 20.0)).to_kelvin(),
        )
        errors = func_to_test_dynamic_returns(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_precise_rounded_fahrenheit_to_kelvin(self) -> None:
        """Tests the rounded and precise result of the conversion Fahrenheit to Kelvin"""
        temps = (
            Fahrenheit(25).precise().to_kelvin(),
            Kelvin(value=269.2611111111111),
            Fahrenheit(25.25).rounded().to_kelvin(),
            Kelvin(value=269),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_dynamic_type_return_fahrenheit_to_newton(self) -> None:
        """Tests the dynamic typed results of the conversion Fahrenheit to Newton"""
        temps = (
            Fahrenheit(randint(1, 20)).to_newton(),
            Fahrenheit(uniform(0.0, 20.0)).to_newton(),
        )
        errors = func_to_test_dynamic_returns(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_precise_rounded_fahrenheit_to_newton(self) -> None:
        """Tests the rounded and precise result of the conversion Fahrenheit to Newton"""
        temps = (
            Fahrenheit(25).precise().to_newton(),
            Newton(value=-1.2833333333333334),
            Fahrenheit(25.25).rounded().to_newton(),
            Newton(value=-1),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_dynamic_type_return_fahrenheit_to_rankine(self) -> None:
        """Tests the dynamic typed results of the conversion Fahrenheit to Rankine"""
        temps = (
            Fahrenheit(randint(1, 20)).to_rankine(),
            Fahrenheit(uniform(0.0, 20.0)).to_rankine(),
        )
        errors = func_to_test_dynamic_returns(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_precise_rounded_fahrenheit_to_rankine(self) -> None:
        """Tests the rounded and precise result of the conversion Fahrenheit to Rankine"""
        temps = (
            Fahrenheit(25).precise().to_rankine(),
            Rankine(value=484.67),
            Fahrenheit(25.25).rounded().to_rankine(),
            Rankine(value=484),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_dynamic_type_return_fahrenheit_to_reaumur(self) -> None:
        """Tests the dynamic typed results of the conversion Fahrenheit to Réaumur"""
        temps = (
            Fahrenheit(randint(1, 20)).to_reaumur(),
            Fahrenheit(uniform(0.0, 20.0)).to_reaumur(),
        )
        errors = func_to_test_dynamic_returns(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_precise_rounded_fahrenheit_to_reaumur(self) -> None:
        """Tests the rounded and precise result of the conversion Fahrenheit to Réaumur"""
        temps = (
            Fahrenheit(25).precise().to_reaumur(),
            Reaumur(value=-3.111111111111111),
            Fahrenheit(25.25).rounded().to_reaumur(),
            Reaumur(value=-3),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_dynamic_type_return_fahrenheit_to_romer(self) -> None:
        """Tests the dynamic typed results of the conversion Fahrenheit to Rømer"""
        temps = (
            Fahrenheit(randint(1, 20)).to_romer(),
            Fahrenheit(uniform(0.0, 20.0)).to_romer(),
        )
        errors = func_to_test_dynamic_returns(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_precise_rounded_fahrenheit_to_romer(self) -> None:
        """Tests the rounded and precise result of the conversion Fahrenheit to Rømer"""
        temps = (
            Fahrenheit(25).precise().to_romer(),
            Romer(value=5.458333333333333),
            Fahrenheit(25.25).rounded().to_romer(),
            Romer(value=5),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    # Kelvin to <other temp scale> tests
    def test_dynamic_type_return_kelvin_to_celsius(self) -> None:
        """Tests the dynamic typed results of the conversion Kelvin to Celsius"""
        temps = (
            Kelvin(randint(1, 20)).to_celsius(),
            Kelvin(uniform(0.0, 20.0)).to_celsius(),
        )
        errors = func_to_test_dynamic_returns(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_precise_rounded_kelvin_to_celsius(self) -> None:
        """Tests the rounded and precise result of the conversion Kelvin to Celsius"""
        temps = (
            Kelvin(25).precise().to_celsius(),
            Celsius(value=-248.14999999999998),
            Kelvin(25.25).rounded().to_celsius(),
            Celsius(value=-248),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_dynamic_type_return_kelvin_to_delisle(self) -> None:
        """Tests the dynamic typed results of the conversion Kelvin to Delisle"""
        temps = (
            Kelvin(randint(1, 20)).to_delisle(),
            Kelvin(uniform(0.0, 20.0)).to_delisle(),
        )
        errors = func_to_test_dynamic_returns(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_precise_rounded_kelvin_to_delisle(self) -> None:
        """Tests the rounded and precise result of the conversion Kelvin to Delisle"""
        temps = (
            Kelvin(25).precise().to_delisle(),
            Delisle(value=522.2249999999999),
            Kelvin(25.25).rounded().to_delisle(),
            Delisle(value=522),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_dynamic_type_return_kelvin_to_fahrenheit(self) -> None:
        """Tests the dynamic typed results of the conversion Kelvin to Fahrenheit"""
        temps = (
            Kelvin(randint(1, 20)).to_fahrenheit(),
            Kelvin(uniform(0.0, 20.0)).to_fahrenheit(),
        )
        errors = func_to_test_dynamic_returns(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_precise_rounded_kelvin_to_fahrenheit(self) -> None:
        """Tests the rounded and precise result of the conversion Kelvin to Fahrenheit"""
        temps = (
            Kelvin(25).precise().to_fahrenheit(),
            Fahrenheit(value=-414.67),
            Kelvin(25.25).rounded().to_fahrenheit(),
            Fahrenheit(value=-414),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_dynamic_type_return_kelvin_to_newton(self) -> None:
        """Tests the dynamic typed results of the conversion Kelvin to Newton"""
        temps = (
            Kelvin(randint(1, 20)).to_newton(),
            Kelvin(uniform(0.0, 20.0)).to_newton(),
        )
        errors = func_to_test_dynamic_returns(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_precise_rounded_kelvin_to_newton(self) -> None:
        """Tests the rounded and precise result of the conversion Kelvin to Newton"""
        temps = (
            Kelvin(25).precise().to_newton(),
            Newton(value=-81.889499999999987),
            Kelvin(25.25).rounded().to_newton(),
            Newton(value=-81),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_dynamic_type_return_kelvin_to_rankine(self) -> None:
        """Tests the dynamic typed results of the conversion Kelvin to Rankine"""
        temps = (
            Kelvin(randint(1, 20)).to_rankine(),
            Kelvin(uniform(0.0, 20.0)).to_rankine(),
        )
        errors = func_to_test_dynamic_returns(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_precise_rounded_kelvin_to_rankine(self) -> None:
        """Tests the rounded and precise result of the conversion Kelvin to Rankine"""
        temps = (
            Kelvin(25).precise().to_rankine(),
            Rankine(value=45.0),
            Kelvin(25.25).rounded().to_rankine(),
            Rankine(value=45),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_dynamic_type_return_kelvin_to_reaumur(self) -> None:
        """Tests the dynamic typed results of the conversion Kelvin to Réaumur"""
        temps = (
            Kelvin(randint(1, 20)).to_reaumur(),
            Kelvin(uniform(0.0, 20.0)).to_reaumur(),
        )
        errors = func_to_test_dynamic_returns(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_precise_rounded_kelvin_to_reaumur(self) -> None:
        """Tests the rounded and precise result of the conversion Kelvin to Réaumur"""
        temps = (
            Kelvin(25).precise().to_reaumur(),
            Reaumur(value=-198.51999999999998),
            Kelvin(25.25).rounded().to_reaumur(),
            Reaumur(value=-198),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_dynamic_type_return_kelvin_to_romer(self) -> None:
        """Tests the dynamic typed results of the conversion Kelvin to Rømer"""
        temps = (
            Kelvin(randint(1, 20)).to_romer(),
            Kelvin(uniform(0.0, 20.0)).to_romer(),
        )
        errors = func_to_test_dynamic_returns(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_precise_rounded_kelvin_to_romer(self) -> None:
        """Tests the rounded and precise result of the conversion Kelvin to Rømer"""
        temps = (
            Kelvin(25).precise().to_romer(),
            Romer(value=-122.77875),
            Kelvin(25.25).rounded().to_romer(),
            Romer(value=-122),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    # Delisle to <other temp scale> tests
    def test_dynamic_type_return_delisle_to_celsius(self) -> None:
        """Tests the dynamic typed results of the conversion Delisle to Celsius"""
        temps = (
            Delisle(randint(1, 20)).to_celsius(),
            Delisle(uniform(0.0, 20.0)).to_celsius(),
        )
        errors = func_to_test_dynamic_returns(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_precise_rounded_delisle_to_celsius(self) -> None:
        """Tests the rounded and precise result of the conversion Delisle to Celsius"""
        temps = (
            Delisle(25).precise().to_celsius(),
            Celsius(value=83.33333333333333),
            Delisle(25.25).rounded().to_celsius(),
            Celsius(value=83),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_dynamic_type_return_delisle_to_fahrenheit(self) -> None:
        """Tests the dynamic typed results of the conversion Delisle to Fahrenheit"""
        temps = (
            Delisle(randint(1, 20)).to_fahrenheit(),
            Delisle(uniform(0.0, 20.0)).to_fahrenheit(),
        )
        errors = func_to_test_dynamic_returns(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_precise_rounded_delisle_to_fahrenheit(self) -> None:
        """Tests the rounded and precise result of the conversion Delisle to Fahrenheit"""
        temps = (
            Delisle(25).precise().to_fahrenheit(),
            Fahrenheit(value=182.0),
            Delisle(25.25).rounded().to_fahrenheit(),
            Fahrenheit(value=182),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_dynamic_type_return_delisle_to_kelvin(self) -> None:
        """Tests the dynamic typed results of the conversion Delisle to Kelvin"""
        temps = (
            Delisle(randint(1, 20)).to_kelvin(),
            Delisle(uniform(0.0, 20.0)).to_kelvin(),
        )
        errors = func_to_test_dynamic_returns(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_precise_rounded_delisle_to_kelvin(self) -> None:
        """Tests the rounded and precise result of the conversion Delisle to Kelvin"""
        temps = (
            Delisle(25).precise().to_kelvin(),
            Kelvin(value=356.4833333333333),
            Delisle(25.25).rounded().to_kelvin(),
            Kelvin(value=356),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_dynamic_type_return_delisle_to_newton(self) -> None:
        """Tests the dynamic typed results of the conversion Delisle to Newton"""
        temps = (
            Delisle(randint(1, 20)).to_newton(),
            Delisle(uniform(0.0, 20.0)).to_newton(),
        )
        errors = func_to_test_dynamic_returns(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_precise_rounded_delisle_to_newton(self) -> None:
        """Tests the rounded and precise result of the conversion Delisle to Newton"""
        temps = (
            Delisle(25).precise().to_newton(),
            Newton(value=27.5),
            Delisle(25.25).rounded().to_newton(),
            Newton(value=27),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_dynamic_type_return_delisle_to_rankine(self) -> None:
        """Tests the dynamic typed results of the conversion Delisle to Rankine"""
        temps = (
            Delisle(randint(1, 20)).to_rankine(),
            Delisle(uniform(0.0, 20.0)).to_rankine(),
        )
        errors = func_to_test_dynamic_returns(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_precise_rounded_delisle_to_rankine(self) -> None:
        """Tests the rounded and precise result of the conversion Delisle to Rankine"""
        temps = (
            Delisle(25).precise().to_rankine(),
            Rankine(value=641.67),
            Delisle(25.25).rounded().to_rankine(),
            Rankine(value=641),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_dynamic_type_return_delisle_to_reaumur(self) -> None:
        """Tests the dynamic typed results of the conversion Delisle to Réaumur"""
        temps = (
            Delisle(randint(1, 20)).to_reaumur(),
            Delisle(uniform(0.0, 20.0)).to_reaumur(),
        )
        errors = func_to_test_dynamic_returns(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_precise_rounded_delisle_to_reaumur(self) -> None:
        """Tests the rounded and precise result of the conversion Delisle to Réaumur"""
        temps = (
            Delisle(25).precise().to_reaumur(),
            Reaumur(value=66.66666666666667),
            Delisle(25.25).rounded().to_reaumur(),
            Reaumur(value=66),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_dynamic_type_return_delisle_to_romer(self) -> None:
        """Tests the dynamic typed results of the conversion Delisle to Rømer"""
        temps = (
            Delisle(randint(1, 20)).to_romer(),
            Delisle(uniform(0.0, 20.0)).to_romer(),
        )
        errors = func_to_test_dynamic_returns(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_precise_rounded_delisle_to_romer(self) -> None:
        """Tests the rounded and precise result of the conversion Delisle to Rømer"""
        temps = (
            Delisle(25).precise().to_romer(),
            Romer(value=51.25),
            Delisle(25.25).rounded().to_romer(),
            Romer(value=51),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

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

    # Rømer to <other temp scale> tests
    def test_dynamic_type_return_romer_to_celsius(self) -> None:
        """Tests the dynamic typed results of the conversion Rømer to Celsius"""
        temps = (
            Romer(randint(1, 20)).to_celsius(),
            Romer(uniform(0.0, 20.0)).to_celsius(),
        )
        errors = func_to_test_dynamic_returns(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_precise_rounded_romer_to_celsius(self) -> None:
        """Tests the rounded and precise result of the conversion Rømer to Celsius"""
        temps = (
            Romer(25).precise().to_celsius(),
            Celsius(value=33.333333333333336),
            Romer(25.25).rounded().to_celsius(),
            Celsius(value=33),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_dynamic_type_return_romer_to_fahrenheit(self) -> None:
        """Tests the dynamic typed results of the conversion Rømer to Fahrenheit"""
        temps = (
            Romer(randint(1, 20)).to_fahrenheit(),
            Romer(uniform(0.0, 20.0)).to_fahrenheit(),
        )
        errors = func_to_test_dynamic_returns(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_precise_rounded_romer_to_fahrenheit(self) -> None:
        """Tests the rounded and precise result of the conversion Rømer to Fahrenheit"""
        temps = (
            Romer(25).precise().to_fahrenheit(),
            Fahrenheit(value=92.0),
            Romer(25.25).rounded().to_fahrenheit(),
            Fahrenheit(value=92),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_dynamic_type_return_romer_to_delisle(self) -> None:
        """Tests the dynamic typed results of the conversion Rømer to Delisle"""
        temps = (
            Romer(randint(1, 20)).to_delisle(),
            Romer(uniform(0.0, 20.0)).to_delisle(),
        )
        errors = func_to_test_dynamic_returns(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_precise_rounded_romer_to_delisle(self) -> None:
        """Tests the rounded and precise result of the conversion Rømer to Delisle"""
        temps = (
            Romer(25).precise().to_delisle(),
            Delisle(value=100.0),
            Romer(25.25).rounded().to_delisle(),
            Delisle(value=100),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_dynamic_type_return_romer_to_kelvin(self) -> None:
        """Tests the dynamic typed results of the conversion Rømer to Kelvin"""
        temps = (
            Romer(randint(1, 20)).to_kelvin(),
            Romer(uniform(0.0, 20.0)).to_kelvin(),
        )
        errors = func_to_test_dynamic_returns(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_precise_rounded_romer_to_kelvin(self) -> None:
        """Tests the rounded and precise result of the conversion Rømer to Kelvin"""
        temps = (
            Romer(25).precise().to_kelvin(),
            Kelvin(value=306.4833333333333),
            Romer(25.25).rounded().to_kelvin(),
            Kelvin(value=306),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_dynamic_type_return_romer_to_newton(self) -> None:
        """Tests the dynamic typed results of the conversion Rømer to Newton"""
        temps = (
            Romer(randint(1, 20)).to_newton(),
            Romer(uniform(0.0, 20.0)).to_newton(),
        )
        errors = func_to_test_dynamic_returns(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_precise_rounded_romer_to_newton(self) -> None:
        """Tests the rounded and precise result of the conversion Rømer to Newton"""
        temps = (
            Romer(25).precise().to_newton(),
            Newton(value=11.0),
            Romer(25.25).rounded().to_newton(),
            Newton(value=11),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_dynamic_type_return_romer_to_rankine(self) -> None:
        """Tests the dynamic typed results of the conversion Rømer to Rankine"""
        temps = (
            Romer(randint(1, 20)).to_rankine(),
            Romer(uniform(0.0, 20.0)).to_rankine(),
        )
        errors = func_to_test_dynamic_returns(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_precise_rounded_romer_to_rankine(self) -> None:
        """Tests the rounded and precise result of the conversion Rømer to Rankine"""
        temps = (
            Romer(25).precise().to_rankine(),
            Rankine(value=551.6700000000001),
            Romer(25.25).rounded().to_rankine(),
            Rankine(value=551),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))
