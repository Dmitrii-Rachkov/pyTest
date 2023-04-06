"""Научимся задавать очередность выполнения тестов"""
import pytest


@pytest.mark.run(order=2)
def test_method_1():
    print("Letter method_1")

@pytest.mark.run(order=1)
def test_method_2():
    print("Letter method_2")

@pytest.mark.run(order=6)
def test_method_3():
    print("Letter method_3")

@pytest.mark.run(order=4)
def test_method_4():
    print("Letter method_4")

@pytest.mark.run(order=3)
def test_method_5():
    print("Letter method_5")

@pytest.mark.run(order=5)
def test_method_6():
    print("Letter method_6")

# Команда для установки библиотеки 'ordering' - 'pip3 install pytest-ordering'
# Декоратор позволяющий определить очередность запуска тестов - '@pytest.mark.run(order=2)'
