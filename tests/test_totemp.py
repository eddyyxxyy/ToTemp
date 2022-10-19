#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from totemp import Celsius


class TestToTemp:
    """Tests all methods of all Classes in temperature_types.py"""

    def test_celsius_to_delisle(self):
        """Tests the convertion: Celsius to Delisle"""
        assert Celsius.to_delisle(20.25) == 119.625

    def test_celsius_to_delisle_type(self):
        """Tests the type of the return on the convertion: Celsius to Delisle"""
        assert isinstance(Celsius.to_delisle(20.25), float)

    def test_celcius_to_fahrenheit(self):
        """Tests the convertion: Celsius to Fahrenheit"""
        assert Celsius.to_fahrenheit(41.985) == 107.57300000000001

    def test_celcius_to_fahrenheit_type(self):
        """Tests the type of the return on the convertion: Celsius to Fahrenheit"""
        assert isinstance(Celsius.to_fahrenheit(41.985), float)

    def test_celcius_to_kelvin(self):
        """Tests the convertion: Celsius to Kelvin"""
        assert Celsius.to_kelvin(72.111) == 345.26099999999997

    def test_celcius_to_kelvin_type(self):
        """Tests the type of the return on the convertion: Celsius to Kelvin"""
        assert isinstance(Celsius.to_kelvin(72.111), float)

    def test_celcius_to_newton(self):
        """Tests the convertion: Celsius to Newton"""
        assert Celsius.to_newton(144.9955) == 47.848515

    def test_celcius_to_newton_type(self):
        """Tests the type of the return on the convertion: Celsius to Kelvin"""
        assert isinstance(Celsius.to_newton(144.9955), float)

    def test_celcius_to_rankine(self):
        """Tests the convertion: Celsius to Rankine"""
        assert Celsius.to_rankine(18.283832) == 524.5808976000001

    def test_celcius_to_rankine_type(self):
        """Tests the type of the return on the convertion: Celsius to Rankine"""
        assert isinstance(Celsius.to_rankine(18.283832), float)

    def test_celcius_to_reaumur(self):
        """Tests the convertion: Celsius to Réaumur"""
        assert Celsius.to_reaumur(123.212) == 98.56960000000001

    def test_celcius_to_reaumur_type(self):
        """Tests the type of the return on the convertion: Celsius to Réaumur"""
        assert isinstance(Celsius.to_reaumur(123.212), float)

    def test_celcius_to_romer(self):
        """Tests the convertion: Celsius to Rømer"""
        assert Celsius.to_romer(237.236438) == 132.04912995

    def test_celcius_to_romer_type(self):
        """Tests the type of the return on the convertion: Celsius to Rømer"""
        assert isinstance(Celsius.to_romer(237.236438), float)
