import re
import pytest
from playwright.sync_api import expect
from helpers import add, qty, total, order

def test_T41(page):
    add(page); page.get_by_label('Your name').fill('Alex'); page.reload()
    expect(page.locator('#empty-cart')).to_be_visible(); expect(page.get_by_label('Your name')).to_have_value('')


def test_T42(page,browser,base_url):
    order(page)
    with browser.new_context() as context:
        other=context.new_page(); other.goto(base_url)
        expect(other.locator('#empty-cart')).to_be_visible(); expect(other.locator('#order-confirmation')).to_be_hidden()


def test_T43(page):
    page.locator('.store-logo').focus()
    for selector in ['.bag-link','button[data-add="tote"]','button[data-add="bottle"]','#promo-code','#apply-discount','#remove-discount','#customer-name','#place-order']:
        page.keyboard.press('Tab'); expect(page.locator(selector)).to_be_focused()


def test_T44(page):
    page.set_viewport_size({'width':375,'height':812}); add(page); add(page,'Steel Bottle')
    assert page.evaluate('document.documentElement.scrollWidth <= innerWidth')
    for control in page.locator('button:not(#new-order),input').all():
        control.scroll_into_view_if_needed(); expect(control).to_be_visible()
        box=control.bounding_box(); assert box['x']>=0 and box['x']+box['width']<=375
    page.get_by_label('Your name').fill('Alex'); page.get_by_role('button',name='Place order',exact=True).click()
    expect(page.locator('#order-confirmation')).to_be_visible()


def test_T45(page):
    order(page); expect(page.locator('#order-confirmation')).to_be_visible()


def test_T46(page):
    errors=[]; page.on('pageerror',lambda e: errors.append(str(e)))
    page.on('console',lambda msg: errors.append(msg.text) if msg.type=='error' else None)
    page.reload(); order(page); assert errors == []


def test_T47(page):
    order(page,''); expect(page.get_by_role('alert')).to_be_visible()
    expect(page.get_by_label('Your name')).to_have_attribute('aria-invalid','true')
    expect(page.get_by_label('Your name')).to_be_focused()


