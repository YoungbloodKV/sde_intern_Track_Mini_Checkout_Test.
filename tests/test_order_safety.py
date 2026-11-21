import re
import pytest
from playwright.sync_api import expect
from helpers import add, qty, total, order

@pytest.mark.parametrize('case',['T32','T33','T34','T35','T38','T39'])
def test_confirmation(page,case):
    order(page)
    expect(page.locator('#order-confirmation')).to_be_visible()
    expect(page.locator('#order-reference')).to_have_text(re.compile(r'^ORD-[A-Z0-9]+-[A-Z0-9]{4}$'))
    expect(page.locator('#confirmed-total')).to_have_text('₹499.00'); expect(page.locator('#confirmed-name')).to_have_text('Alex Example')
    for control in page.locator('#cart-rows button, #cart-rows input, #product-list button, #customer-name, #discount-controls button, #discount-controls input').all():
        expect(control).to_be_disabled()


def test_T36(page):
    add(page); page.get_by_label('Your name').fill('Alex')
    page.get_by_role('button',name='Place order',exact=True).dblclick()
    expect(page.locator('#order-confirmation')).to_have_count(1); expect(page.locator('#order-confirmation')).to_be_visible()


def test_T37(page):
    order(page); ref=page.locator('#order-reference').inner_text()
    for _ in range(5): page.locator('#checkout-form').dispatch_event('submit')
    expect(page.locator('#order-reference')).to_have_text(ref)


def test_T40(page):
    add(page); page.get_by_label('Your name').fill('Alex'); page.get_by_label('Your name').press('Enter')
    expect(page.locator('#order-confirmation')).to_be_visible()


