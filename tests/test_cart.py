import re
import pytest
from playwright.sync_api import expect
from helpers import add, qty, total, order

def test_T06(page):
    add(page); expect(page.locator('#cart-rows')).to_contain_text('Canvas Tote')


def test_T07(page):
    add(page); add(page, 'Steel Bottle'); expect(page.locator('#cart-rows tr')).to_have_count(2)


def test_T08(page):
    add(page); add(page); expect(page.get_by_label('Quantity for Canvas Tote', exact=True)).to_have_value('2')


@pytest.mark.parametrize('case', ['T09', 'T10', 'T11', 'T12'])
def test_removal(page, case):
    add(page); add(page, 'Steel Bottle')
    page.get_by_role('button', name='Remove Canvas Tote', exact=True).click()
    expect(page.locator('#cart-rows')).not_to_contain_text('Canvas Tote')
    expect(page.get_by_label('Quantity for Steel Bottle', exact=True)).to_have_value('1')
    total(page, '₹299.00')
    if case == 'T10':
        page.get_by_role('button', name='Remove Steel Bottle', exact=True).click()
        expect(page.locator('#empty-cart')).to_be_visible(); total(page, '₹0.00')
    if case == 'T11':
        add(page); expect(page.get_by_label('Quantity for Canvas Tote', exact=True)).to_have_value('1')


def test_T13(page):
    add(page); add(page, 'Steel Bottle'); qty(page, 3)
    expect(page.locator('#item-count')).to_have_text('4 items'); expect(page.locator('#header-count')).to_have_text('4')


def test_T14(page):
    add(page); page.get_by_role('button', name='Increase quantity for Canvas Tote').click()
    expect(page.locator('.line-total')).to_have_text('₹998.00'); total(page, '₹998.00')


def test_T15(page):
    add(page); add(page, 'Steel Bottle'); qty(page, 3); qty(page, 2, 'Steel Bottle'); total(page, '₹2,095.00')


def test_T16(page):
    add(page); qty(page, 99); total(page, '₹49,401.00')
    add(page); expect(page.get_by_label('Quantity for Canvas Tote', exact=True)).to_have_value('99')


@pytest.mark.parametrize('case,value', [('T17','100'),('T18','0'),('T19','-1'),('T20','1.5'),('T21','')])
def test_invalid_quantity(page, case, value):
    add(page); qty(page, 2); qty(page, value)
    expect(page.get_by_label('Quantity for Canvas Tote', exact=True)).to_have_value('2'); total(page, '₹998.00')
    expect(page.get_by_role('alert')).to_have_text('Enter a valid quantity of 1 or more.')


def test_T22(page):
    add(page); q=page.get_by_label('Quantity for Canvas Tote', exact=True)
    q.focus(); q.press('ControlOrMeta+A'); q.press_sequentially('abc'); q.press('Tab')
    expect(q).to_have_value('1'); total(page, '₹499.00')


def test_T23(page):
    add(page)
    for n, expected in [(3,'₹1,497.00'),(9,'₹4,491.00'),(1,'₹499.00')]:
        qty(page,n); total(page,expected)


def test_T24(page):
    add(page); add(page, 'Steel Bottle'); qty(page,99); qty(page,99,'Steel Bottle'); total(page,'₹79,002.00')


