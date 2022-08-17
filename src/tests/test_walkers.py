#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests classes in walkers module"""

from walkers import Walker


def test_walker_speed():
    """Test whether the walker speed is calculated correctly in the specified range (lowest value is min_speed and highest value is max_speed + 2.5% (for Superhumans to occur)"""
    total_steps = 100
    n_walkers = 5

    test_walker = Walker(total_steps=total_steps, n_walkers=n_walkers)
    test_walker.min_speed = 3
    test_walker.max_speed = 10

    # Tests
    for i in range(1000):  # check for 1000 times
        i += 1
        test_walker.walker_speed = test_walker.get_random_speed()

        assert 3 <= test_walker.walker_speed <= 10.25

    # Result: the range of values where the walker speed is expected is correct


def test_take_step_left():
    """Test if position of the walker is correct after taking a step in predefined direction"""
    total_steps = 1222
    n_walkers = 27
    step = 4
    direction = "West"
    expected_x = -20.8
    expected_y = 0.0

    test_walker = Walker(total_steps, n_walkers)
    test_walker.walker_speed = 5.2
    test_walker.x[0] = 0
    test_walker.y[0] = 0

    # Tests
    for i in range(step):
        i += 1
        test_walker.plan_next_step(direction, i)

    assert test_walker.x[step] == expected_x and test_walker.y[step] == expected_y

    # Result: the array is filled with the correct values in x-direction


def test_take_step_up():
    """Test if position of the walker is correct after taking a step in predefined direction"""
    total_steps = 1222
    n_walkers = 27
    step = 2
    direction = "North"
    expected_x = 0.0
    expected_y = 10.4

    test_walker = Walker(total_steps, n_walkers)
    test_walker.walker_speed = 5.2
    test_walker.x[0] = 0
    test_walker.y[0] = 0

    # Tests
    for i in range(step):
        i += 1
        test_walker.plan_next_step(direction, i)

    assert test_walker.y[step] == expected_y and test_walker.x[step] == expected_x

    # Result: the array is filled with the correct values in y-direction


def test_walker_type():
    """Test whether the walker types are assigned correctly"""
    total_steps = 100
    n_walkers = 5

    test_walker = Walker(total_steps=total_steps, n_walkers=n_walkers)
    test_walker.min_speed = 1
    test_walker.max_speed = 10

    # Tests
    speed1 = 8.5
    expected_walker_type1 = "Fast Walker"
    test_walker.walker_speed = speed1
    actual_walker_type = test_walker.walker_type()
    assert actual_walker_type == expected_walker_type1

    speed2 = 1.6
    expected_walker_type2 = "Slow Walker"
    test_walker.walker_speed = speed2
    actual_walker_type = test_walker.walker_type()
    assert actual_walker_type == expected_walker_type2

    speed3 = 10.12
    expected_walker_type3 = "Superhuman"
    test_walker.walker_speed = speed3
    actual_walker_type = test_walker.walker_type()
    assert actual_walker_type == expected_walker_type3

    speed4 = 6
    expected_walker_type4 = "Normal Walker"
    test_walker.walker_speed = speed4
    actual_walker_type = test_walker.walker_type()
    assert actual_walker_type == expected_walker_type4

    # Result: the walker types are recognized correctly
