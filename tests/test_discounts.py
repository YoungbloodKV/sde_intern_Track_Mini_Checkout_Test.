import pytest
from playwright.sync_api import expect
from helpers import add, qty, total


def apply(page, code='SAVE10'):
    page.locator('#promo-code').fill(code)
    page.locator('#apply-discount').click()


@pytest.mark.parametrize('code',['SAVE10','save10',' SaVe10 '], ids=['D01-uppercase','D01-lowercase','D01-trimmed'])
def test_valid_code(page, code):
    add(page); apply(page,code)
    expect(page.locator('#discount-amount')).to_have_text('−₹49.90'); total(page,'₹449.10')


def test_D02_invalid(page):
    add(page); apply(page,'WRONG'); expect(page.get_by_role('alert')).to_have_text('Invalid discount code.'); total(page,'₹499.00')


def test_D03_no_stacking(page):
    add(page); apply(page); apply(page); total(page,'₹449.10')


def test_D04_remove(page):
    add(page); apply(page); page.locator('#remove-discount').click(); total(page,'₹499.00')


def test_D05_recalculate(page):
    add(page); add(page,'Steel Bottle'); apply(page); qty(page,2)
    expect(page.locator('#subtotal')).to_have_text('₹1,297.00')
    expect(page.locator('#discount-amount')).to_have_text('−₹129.70'); total(page,'₹1,167.30')


def test_D06_invalid_preserves_discount(page):
    add(page); apply(page); apply(page,'BAD'); total(page,'₹449.10')


@pytest.mark.parametrize('quantity,discount,amount',[(1,'−₹49.90','₹449.10'),(99,'−₹4,940.10','₹44,460.90')],ids=['D07-min','D07-max'])
def test_discount_boundaries(page,quantity,discount,amount):
    add(page); qty(page,quantity); apply(page)
    expect(page.locator('#discount-amount')).to_have_text(discount); total(page,amount)


def test_D08_empty_cart(page):
    apply(page); total(page,'₹0.00'); expect(page.locator('#discount-amount')).to_have_text('−₹0.00')


def test_D09_receipt_and_reset(page):
    add(page); apply(page); page.locator('#customer-name').fill('Alex'); page.locator('#place-order').click()
    expect(page.locator('#confirmed-items')).to_contain_text('Canvas Tote × 1')
    expect(page.locator('#confirmed-subtotal')).to_have_text('₹499.00')
    expect(page.locator('#confirmed-discount')).to_have_text('−₹49.90')
    expect(page.locator('#confirmed-total')).to_have_text('₹449.10')
    page.locator('#new-order').click(); expect(page.locator('#empty-cart')).to_be_visible(); total(page,'₹0.00')
