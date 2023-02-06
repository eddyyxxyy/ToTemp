#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tests.test_funcs import func_to_test_precise_rounded_results
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
    def test_default_rounded_return_celsius_to_fahrenheit(self) -> None:
        """Tests the default and rounded result of the conversion Celsius to Fahrenheit"""
        temps = (
            Celsius(25).to_fahrenheit(),
            Fahrenheit(77.0),
            Celsius(25).to_fahrenheit().rounded(),
            Fahrenheit(77),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_default_rounded_return_celsius_to_delisle(self) -> None:
        """Tests the default and rounded result of the conversion Celsius to Delisle"""
        temps = (
            Celsius(25).to_delisle(),
            Delisle(112.5),
            Celsius(25).to_delisle().rounded(),
            Delisle(112),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_default_rounded_return_celsius_to_kelvin(self) -> None:
        """Tests the default and rounded result of the conversion Celsius to Kelvin"""
        temps = (
            Celsius(25).to_kelvin(),
            Kelvin(298.15),
            Celsius(25.25).to_kelvin().rounded(),
            Kelvin(298),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_default_rounded_return_celsius_to_newton(self) -> None:
        """Tests the default and rounded result of the conversion Celsius to Newton"""
        temps = (
            Celsius(25).to_newton(),
            Newton(8.25),
            Celsius(25).to_newton().rounded(),
            Newton(8),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_default_rounded_return_celsius_to_rankine(self) -> None:
        """Tests the default and rounded result of the conversion Celsius to Rankine"""
        temps = (
            Celsius(25).to_rankine(),
            Rankine(536.67),
            Celsius(25).to_rankine().rounded(),
            Rankine(537),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_default_rounded_return_celsius_to_reaumur(self) -> None:
        """Tests the default and rounded result of the conversion Celsius to Réaumur"""
        temps = (
            Celsius(25).to_reaumur(),
            Reaumur(20.0),
            Celsius(25.25).to_reaumur().rounded(),
            Reaumur(20),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_default_rounded_return_celsius_to_romer(self) -> None:
        """Tests the default and rounded result of the conversion Celsius to Rømer"""
        temps = (
            Celsius(25).to_romer(),
            Romer(20.625),
            Celsius(25.25).to_romer().rounded(),
            Romer(21),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    # Fahrenheit to <other temp scale> tests
    def test_default_rounded_return_fahrenheit_to_celsius(self) -> None:
        """Tests the default and rounded result of the conversion Fahrenheit to Celsius"""
        temps = (
            Fahrenheit(25).to_celsius(),
            Celsius(-3.888888888888889),
            Fahrenheit(25).to_celsius().rounded(),
            Celsius(-4),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_default_rounded_return_fahrenheit_to_delisle(self) -> None:
        """Tests the default and rounded result of the conversion Fahrenheit to Delisle"""
        temps = (
            Fahrenheit(25).to_delisle(),
            Delisle(155.83333333333334),
            Fahrenheit(25).to_delisle().rounded(),
            Delisle(156),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_default_rounded_return_fahrenheit_to_kelvin(self) -> None:
        """Tests the default and rounded result of the conversion Fahrenheit to Kelvin"""
        temps = (
            Fahrenheit(25).to_kelvin(),
            Kelvin(269.2611111111111),
            Fahrenheit(25).to_kelvin().rounded(),
            Kelvin(269),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_default_rounded_return_fahrenheit_to_newton(self) -> None:
        """Tests the default and rounded result of the conversion Fahrenheit to Newton"""
        temps = (
            Fahrenheit(25).to_newton(),
            Newton(-1.2833333333333334),
            Fahrenheit(25).to_newton().rounded(),
            Newton(-1),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_default_rounded_return_fahrenheit_to_rankine(self) -> None:
        """Tests the default and rounded result of the conversion Fahrenheit to Rankine"""
        temps = (
            Fahrenheit(25).to_rankine(),
            Rankine(484.67),
            Fahrenheit(25).to_rankine().rounded(),
            Rankine(485),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_default_rounded_return_fahrenheit_to_reaumur(self) -> None:
        """Tests the default and rounded result of the conversion Fahrenheit to Réaumur"""
        temps = (
            Fahrenheit(25).to_reaumur(),
            Reaumur(-3.111111111111111),
            Fahrenheit(25).to_reaumur().rounded(),
            Reaumur(-3),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_default_rounded_return_fahrenheit_to_romer(self) -> None:
        """Tests the default and rounded result of the conversion Fahrenheit to Rømer"""
        temps = (
            Fahrenheit(25).to_romer(),
            Romer(5.458333333333333),
            Fahrenheit(25).to_romer().rounded(),
            Romer(5),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    # Delisle to <other temp scale> tests
    def test_default_rounded_return_delisle_to_celsius(self) -> None:
        """Tests the default and rounded result of the conversion Delisle to Celsius"""
        temps = (
            Delisle(25).to_celsius(),
            Celsius(83.33333333333333),
            Delisle(25).to_celsius().rounded(),
            Celsius(83),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_default_rounded_return_delisle_to_fahrenheit(self) -> None:
        """Tests the default and rounded result of the conversion Delisle to Fahrenheit"""
        temps = (
            Delisle(25).to_fahrenheit(),
            Fahrenheit(182.0),
            Delisle(25).to_fahrenheit().rounded(),
            Fahrenheit(182),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_default_rounded_return_delisle_to_kelvin(self) -> None:
        """Tests the default and rounded result of the conversion Delisle to Kelvin"""
        temps = (
            Delisle(25).to_kelvin(),
            Kelvin(356.4833333333333),
            Delisle(25).to_kelvin().rounded(),
            Kelvin(356),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_default_rounded_return_delisle_to_newton(self) -> None:
        """Tests the default and rounded result of the conversion Delisle to Newton"""
        temps = (
            Delisle(25).to_newton(),
            Newton(27.5),
            Delisle(25).to_newton().rounded(),
            Newton(28),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_default_rounded_return_delisle_to_rankine(self) -> None:
        """Tests the default and rounded result of the conversion Delisle to Rankine"""
        temps = (
            Delisle(25).to_rankine(),
            Rankine(641.67),
            Delisle(25).to_rankine().rounded(),
            Rankine(642),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_default_rounded_return_delisle_to_reaumur(self) -> None:
        """Tests the default and rounded result of the conversion Delisle to Réaumur"""
        temps = (
            Delisle(25).to_reaumur(),
            Reaumur(66.66666666666667),
            Delisle(25).to_reaumur().rounded(),
            Reaumur(67),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_default_rounded_return_delisle_to_romer(self) -> None:
        """Tests the default and rounded result of the conversion Delisle to Rømer"""
        temps = (
            Delisle(25).to_romer(),
            Romer(51.25),
            Delisle(25).to_romer().rounded(),
            Romer(51),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    # Kelvin to <other temp scale> tests
    def test_default_rounded_return_kelvin_to_celsius(self) -> None:
        """Tests the default and rounded result of the conversion Kelvin to Celsius"""
        temps = (
            Kelvin(25).to_celsius(),
            Celsius(-248.14999999999998),
            Kelvin(25).to_celsius().rounded(),
            Celsius(-248),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_default_rounded_return_kelvin_to_delisle(self) -> None:
        """Tests the default and rounded result of the conversion Kelvin to Delisle"""
        temps = (
            Kelvin(25).to_delisle(),
            Delisle(522.2249999999999),
            Kelvin(25).to_delisle().rounded(),
            Delisle(522),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_default_rounded_return_kelvin_to_fahrenheit(self) -> None:
        """Tests the default and rounded result of the conversion Kelvin to Fahrenheit"""
        temps = (
            Kelvin(25).to_fahrenheit(),
            Fahrenheit(-414.67),
            Kelvin(25).to_fahrenheit().rounded(),
            Fahrenheit(-415),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_default_rounded_return_kelvin_to_newton(self) -> None:
        """Tests the default and rounded result of the conversion Kelvin to Newton"""
        temps = (
            Kelvin(25).to_newton(),
            Newton(-81.889499999999987),
            Kelvin(25).to_newton().rounded(),
            Newton(-82),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_default_rounded_return_kelvin_to_rankine(self) -> None:
        """Tests the default and rounded result of the conversion Kelvin to Rankine"""
        temps = (
            Kelvin(25).to_rankine(),
            Rankine(45.0),
            Kelvin(25).to_rankine().rounded(),
            Rankine(45),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_default_rounded_return_kelvin_to_reaumur(self) -> None:
        """Tests the default and rounded result of the conversion Kelvin to Réaumur"""
        temps = (
            Kelvin(25).to_reaumur(),
            Reaumur(-198.51999999999998),
            Kelvin(25).to_reaumur().rounded(),
            Reaumur(-199),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_default_rounded_return_kelvin_to_romer(self) -> None:
        """Tests the default and rounded result of the conversion Kelvin to Rømer"""
        temps = (
            Kelvin(25).to_romer(),
            Romer(-122.77875),
            Kelvin(25).to_romer().rounded(),
            Romer(-123),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    # Newton to <other temp scale> tests
    def test_default_rounded_return_newton_to_celsius(self) -> None:
        """Tests the default and rounded result of the conversion Newton to Celsius"""
        temps = (
            Newton(25).to_celsius(),
            Celsius(75.75757575757575),
            Newton(25).to_celsius().rounded(),
            Celsius(76),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_default_rounded_return_newton_to_fahrenheit(self) -> None:
        """Tests the default and rounded result of the conversion Newton to Fahrenheit"""
        temps = (
            Newton(25).to_fahrenheit(),
            Fahrenheit(168.36363636363637),
            Newton(25).to_fahrenheit().rounded(),
            Fahrenheit(168),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_default_rounded_return_newton_to_delisle(self) -> None:
        """Tests the default and rounded result of the conversion Newton to Delisle"""
        temps = (
            Newton(25).to_delisle(),
            Delisle(36.36363636363637),
            Newton(25).to_delisle().rounded(),
            Delisle(36),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_default_rounded_return_newton_to_kelvin(self) -> None:
        """Tests the default and rounded result of the conversion Newton to Kelvin"""
        temps = (
            Newton(25).to_kelvin(),
            Kelvin(348.9075757575757),
            Newton(25).to_kelvin().rounded(),
            Kelvin(349),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_default_rounded_return_newton_to_rankine(self) -> None:
        """Tests the default and rounded result of the conversion Newton to Rankine"""
        temps = (
            Newton(25).to_rankine(),
            Rankine(628.0336363636363),
            Newton(25).to_rankine().rounded(),
            Rankine(628),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_default_rounded_return_newton_to_reaumur(self) -> None:
        """Tests the default and rounded result of the conversion Newton to Réaumur"""
        temps = (
            Newton(25).to_reaumur(),
            Reaumur(60.60606060606061),
            Newton(25).to_reaumur().rounded(),
            Reaumur(61),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_default_rounded_return_newton_to_romer(self) -> None:
        """Tests the default and rounded result of the conversion Newton to Rømer"""
        temps = (
            Newton(25).to_romer(),
            Romer(47.27272727272727),
            Newton(25).to_romer().rounded(),
            Romer(47),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    # Rankine to <other temp scale> tests
    def test_default_rounded_return_rankine_to_celsius(self) -> None:
        """Tests the default and rounded result of the conversion Rankine to Celsius"""
        temps = (
            Rankine(25).to_celsius(),
            Celsius(-259.2611111111111),
            Rankine(25).to_celsius().rounded(),
            Celsius(-259),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_default_rounded_return_rankine_to_fahrenheit(self) -> None:
        """Tests the default and rounded result of the conversion Rankine to Fahrenheit"""
        temps = (
            Rankine(25).to_fahrenheit(),
            Fahrenheit(-434.67),
            Rankine(25).to_fahrenheit().rounded(),
            Fahrenheit(-435),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_default_rounded_return_rankine_to_delisle(self) -> None:
        """Tests the default and rounded result of the conversion Rankine to Delisle"""
        temps = (
            Rankine(25).to_delisle(),
            Delisle(538.8916666666667),
            Rankine(25).to_delisle().rounded(),
            Delisle(539),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_default_rounded_return_rankine_to_kelvin(self) -> None:
        """Tests the default and rounded result of the conversion Rankine to Kelvin"""
        temps = (
            Rankine(25).to_kelvin(),
            Kelvin(13.88888888888889),
            Rankine(25).to_kelvin().rounded(),
            Kelvin(14),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_default_rounded_return_rankine_to_newton(self) -> None:
        """Tests the default and rounded result of the conversion Rankine to Newton"""
        temps = (
            Rankine(25).to_newton(),
            Newton(-85.55616666666667),
            Rankine(25).to_newton().rounded(),
            Newton(-86),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_default_rounded_return_rankine_to_reaumur(self) -> None:
        """Tests the default and rounded result of the conversion Rankine to Réaumur"""
        temps = (
            Rankine(25).to_reaumur(),
            Reaumur(-207.4088888888889),
            Rankine(25).to_reaumur().rounded(),
            Reaumur(-207),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_default_rounded_return_rankine_to_romer(self) -> None:
        """Tests the default and rounded result of the conversion Rankine to Rømer"""
        temps = (
            Rankine(25).to_romer(),
            Romer(-128.61208333333335),
            Rankine(25).to_romer().rounded(),
            Romer(-129),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    # Réaumur to <other temp scale> tests
    def test_default_rounded_return_reaumur_to_celsius(self) -> None:
        """Tests the default and rounded result of the conversion Réaumur to Celsius"""
        temps = (
            Reaumur(25).to_celsius(),
            Celsius(31.25),
            Reaumur(25).to_celsius().rounded(),
            Celsius(31),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_default_rounded_return_reaumur_to_fahrenheit(self) -> None:
        """Tests the default and rounded result of the conversion Réaumur to Fahrenheit"""
        temps = (
            Reaumur(25).to_fahrenheit(),
            Fahrenheit(88.25),
            Reaumur(25).to_fahrenheit().rounded(),
            Fahrenheit(88),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_default_rounded_return_reaumur_to_delisle(self) -> None:
        """Tests the default and rounded result of the conversion Réaumur to Delisle"""
        temps = (
            Reaumur(25).to_delisle(),
            Delisle(103.125),
            Reaumur(25).to_delisle().rounded(),
            Delisle(103),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_default_rounded_return_reaumur_to_kelvin(self) -> None:
        """Tests the default and rounded result of the conversion Réaumur to Kelvin"""
        temps = (
            Reaumur(25).to_kelvin(),
            Kelvin(304.4),
            Reaumur(25).to_kelvin().rounded(),
            Kelvin(304),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_default_rounded_return_reaumur_to_newton(self) -> None:
        """Tests the default and rounded result of the conversion Réaumur to Newton"""
        temps = (
            Reaumur(25).to_newton(),
            Newton(10.3125),
            Reaumur(25).to_newton().rounded(),
            Newton(10),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_default_rounded_return_reaumur_to_rankine(self) -> None:
        """Tests the default and rounded result of the conversion Réaumur to Rankine"""
        temps = (
            Reaumur(25).to_rankine(),
            Rankine(547.9200000000001),
            Reaumur(25).to_rankine().rounded(),
            Rankine(548),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_default_rounded_return_reaumur_to_romer(self) -> None:
        """Tests the default and rounded result of the conversion Réaumur to Rømer"""
        temps = (
            Reaumur(25).to_romer(),
            Romer(23.90625),
            Reaumur(25).to_romer().rounded(),
            Romer(24),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    # Rømer to <other temp scale> tests
    def test_default_rounded_return_romer_to_celsius(self) -> None:
        """Tests the default and rounded result of the conversion Rømer to Celsius"""
        temps = (
            Romer(25).to_celsius(),
            Celsius(33.333333333333336),
            Romer(25).to_celsius().rounded(),
            Celsius(33),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_default_rounded_return_romer_to_fahrenheit(self) -> None:
        """Tests the default and rounded result of the conversion Rømer to Fahrenheit"""
        temps = (
            Romer(25).to_fahrenheit(),
            Fahrenheit(92.0),
            Romer(25).to_fahrenheit().rounded(),
            Fahrenheit(92),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_default_rounded_return_romer_to_delisle(self) -> None:
        """Tests the default and rounded result of the conversion Rømer to Delisle"""
        temps = (
            Romer(25).to_delisle(),
            Delisle(100.0),
            Romer(25).to_delisle().rounded(),
            Delisle(100),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_default_rounded_return_romer_to_kelvin(self) -> None:
        """Tests the default and rounded result of the conversion Rømer to Kelvin"""
        temps = (
            Romer(25).to_kelvin(),
            Kelvin(306.4833333333333),
            Romer(25).to_kelvin().rounded(),
            Kelvin(306),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_default_rounded_return_romer_to_newton(self) -> None:
        """Tests the default and rounded result of the conversion Rømer to Newton"""
        temps = (
            Romer(25).to_newton(),
            Newton(11.0),
            Romer(25).to_newton().rounded(),
            Newton(11),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_default_rounded_return_romer_to_rankine(self) -> None:
        """Tests the default and rounded result of the conversion Rømer to Rankine"""
        temps = (
            Romer(25).to_rankine(),
            Rankine(551.6700000000001),
            Romer(25).to_rankine().rounded(),
            Rankine(552),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))

    def test_default_rounded_return_romer_to_reaumur(self) -> None:
        """Tests the default and rounded result of the conversion Rømer to Réaumur"""
        temps = (
            Romer(25).to_reaumur(),
            Reaumur(26.666666666666668),
            Romer(25).to_reaumur().rounded(),
            Reaumur(27),
        )
        errors = func_to_test_precise_rounded_results(temps)

        assert not errors, 'errors occurred:\n{}'.format('\n'.join(errors))
