# lib/testing/functions_test.py
import pytest
from lib.functions import *

def test_greet_programmer(capsys):
    greet_programmer()
    captured = capsys.readouterr()
    assert captured.out == "Hello, programmer!\n"

def test_greet(capsys):
    greet("Alice")
    captured = capsys.readouterr()
    assert captured.out == "Hello, Alice!\n"

def test_greet_with_default(capsys):
    greet_with_default()
    captured = capsys.readouterr()
    assert captured.out == "Hello, programmer!\n"
    greet_with_default("Bob")
    captured = capsys.readouterr()
    assert captured.out == "Hello, Bob!\n"

def test_add():
    assert add(3, 5) == 8
    assert add(-2, 4) == 2

def test_halve():
    assert halve(10) == 5
    assert halve(7) == 3.5
