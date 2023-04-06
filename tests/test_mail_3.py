"""Конструкция yeild"""

# Конструкция 'yeild' - до неё это всё что выполняется до каждого теста,
# а после неё это то что выполняется после каждого теста

import pytest

@pytest.fixture()
def set_up():
    print("Entry in system is done")
    yield
    print("Sign out from sistem")

def test_sending_mail_5(set_up):
    print("Letter sent")

def test_sending_mail_6(set_up):
    print("Letter sent")



