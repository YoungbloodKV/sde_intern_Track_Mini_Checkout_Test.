from playwright.sync_api import expect

def add(p, product='Canvas Tote'):
    p.get_by_role('button', name=f'Add {product} to cart').click()


def qty(p, value, product='Canvas Tote'):
    q = p.get_by_label(f'Quantity for {product}', exact=True)
    q.fill(str(value)); q.press('Tab')


def total(p, value):
    expect(p.locator('#order-total')).to_have_text(value)


def order(p, name='Alex Example'):
    add(p); p.get_by_label('Your name').fill(name)
    p.get_by_role('button', name='Place order', exact=True).click()


