import re
import pytest
from playwright.sync_api import expect
from helpers import add, qty, total, order

@pytest.mark.parametrize('case,name,message', [('T25','','Please enter your name.'),('T26','   ','Please enter a valid name.')])
def test_name_validation(page,case,name,message):
    order(page,name); expect(page.get_by_role('alert')).to_have_text(message); expect(page.locator('#order-confirmation')).to_be_hidden()


def test_T27(page):
    order(page,'  Alex Example  '); expect(page.locator('#confirmed-name')).to_have_text('Alex Example')


def test_T28(page):
    order(page,''); page.get_by_label('Your name').fill('Alex'); expect(page.get_by_role('alert')).to_be_hidden()


def test_T29(page):
    add(page); qty(page,3); page.get_by_role('button',name='Place order',exact=True).click()
    total(page,'₹1,497.00'); expect(page.get_by_label('Quantity for Canvas Tote',exact=True)).to_have_value('3')


def test_T30(page):
    page.get_by_role('button',name='Place order',exact=True).click()
    expect(page.get_by_role('alert')).to_contain_text('Your cart is empty'); expect(page.locator('#order-confirmation')).to_be_hidden()


def test_T31(page):
    name='<img src=x onerror=alert(1)>'; order(page,name)
    expect(page.locator('#confirmed-name')).to_have_text(name); expect(page.locator('#confirmed-name img')).to_have_count(0)


