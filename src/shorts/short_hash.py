#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-

def short_hash(long_url: str):
    short_url = hash(long_url)
    return f"https://simkusr.io/{short_url}"