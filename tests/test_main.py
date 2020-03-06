import pendulum
import json
import pytest
import whenzat

def test_loader_loads_from_str():
    """given a json string, json should be returned"""
    base_json = '{"foo": "bar"}'
    json_test = {"foo": "bar"}
    assert whenzat.loader(base_json, from_file=False) == json_test


def test_loader_loads_from_file():
    """given a json file, json should be returned"""
    base_json = 'tests/test_json.json'
    json_test = {"foo": "bar"}
    assert whenzat.loader(base_json) == json_test


def test_parse_int_date_if_less_than_target_date():
    """If date is greater than or equal to the current date, it should return the same day"""
    dt = pendulum.datetime(2020, 1, 15, tz=pendulum.local_timezone())
    starting_date = pendulum.datetime(2020, 1, 14)
    assert whenzat.parse_int(dt.day, starting_date=starting_date) == dt


def test_parse_int_date_if_greater_than_target_date():
    """If date is greater than or equal to the current date, it should return the same day"""
    dt = pendulum.datetime(2020, 1, 15, tz=pendulum.local_timezone())
    starting_date = pendulum.datetime(2020, 1, 16)
    assert whenzat.parse_int(dt.day, starting_date=starting_date) == dt.add(months=1)
