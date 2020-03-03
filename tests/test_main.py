import json
import pytest
import whenzat

def test_loader_loads_from_str():
    """given a json string, json should be returned"""
    base_json = "{'foo': bar}"
    json_test = json.dumps({"foo": "bar"})
    assert whenzat.loader(base_json, from_file=False) == json_test


def test_loader_loads_from_file():
    """given a json file, json should be returned"""
    base_json = 'test/json_test.json'
    json_test = json.dumps({"foo": "bar"})
    assert whenzat.loader(base_json, from_file=False) == json_test
