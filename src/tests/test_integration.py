#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Integration tests"""

import subprocess


def test_run_main():
    """Tests whether main runs correctly"""
    subprocess.check_call(["python", "./src/main.py", "-s -0", "-w -0", "-r -0"])
