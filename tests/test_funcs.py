#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def func_to_test_precise_rounded_results(temps: tuple) -> list:
    errors: list = []

    if not temps[0] == temps[1]:
        errors.append(f'{temps[0]} != {temps[1]} -> should be equal')
    if not temps[2] == temps[3]:
        errors.append(f'{temps[2]} != {temps[3]} -> should be equal')

    return errors
