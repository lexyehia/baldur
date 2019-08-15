from models.transaction import *


def test_line_item_creation():
    line_item = LineItem(type=1, amount=1000, account=21)
    assert type(line_item) is LineItem
    assert line_item.account == 21
    assert line_item.amount == 1000
    assert line_item.type == 1


def test_line_item_to_dict():
    line_item = LineItem(type=1, amount=1000, account=21)
    line_item_dict = line_item.as_dict()
    assert type(line_item_dict) is dict
    assert line_item_dict['type'] == 1
    assert line_item_dict['amount'] == 1000
    assert line_item_dict['account'] == 21


def test_line_item_from_dict():
    line_dict = {'type': 1, 'amount': 1000, 'account': 21}
    line_item = LineItem(**line_dict)
    assert type(line_item) is LineItem
    assert line_item.account == 21
    assert line_item.amount == 1000
    assert line_item.type == 1
