#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def func_to_test_dynamic_returns(temps: tuple) -> list:
    errors: list = []

    if not isinstance(temps[0].value, int):
        errors.append(
            f'temps[0] value -> ({temps[0].value}) -> should be an integer'
        )
    if not isinstance(temps[1].value, float):
        errors.append(f'temps[1] value -> {temps[1].value} -> should be float')

    return errors


def func_to_test_precise_rounded_results(temps: tuple) -> list:
    errors: list = []

    if not temps[0] == temps[1]:
        errors.append(f'{temps[0]} != ({temps[1]}) -> should be equal')
    if not temps[2] == temps[3]:
        errors.append(f'{temps[2]} != ({temps[3]}) -> should be equal')
    if not isinstance(temps[0].value, float):
        errors.append(f'({temps[0]}) -> should be float')
    if not isinstance(temps[2].value, int):
        errors.append(f'({temps[2]}) -> should be int')

    return errors
