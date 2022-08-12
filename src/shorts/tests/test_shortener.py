#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-
from src.shorts.short_hash import short_hash

import pytest


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (
            "https://www.example.com/this-long-url-will-be-short",
            hash('https://www.example.com/this-long-url-will-be-short')
        ),
        (
            "https://www.example.com/this-long-url-will-be-short-long",
            hash('https://www.example.com/this-long-url-will-be-short-long')
        )
    ]
)
def test_shorten_url(test_input, expected):
    actual = short_hash(test_input)
    assert expected == actual
