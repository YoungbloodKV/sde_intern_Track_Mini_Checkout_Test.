"""Prioritise user-visible assertions, no fixed sleeps, independent tests."""
import re
from pathlib import Path

from playwright.sync_api import expect

EVIDENCE = Path(__file__).resolve().parents[1] / "evidence"


def capture(page, filename):
    EVIDENCE.mkdir(exist_ok=True)
    page.screenshot(path=str(EVIDENCE / filename), full_page=True)


def test_successful_checkout_shows_single_confirmation(page):
    page.get_by_role("button", name="Add Canvas Tote to cart").click()
    page.get_by_label("Your name").fill("Alex Example")
    page.get_by_role("button", name="Place order").click()

    expect(page.get_by_role("heading", name="Order placed successfully!")).to_be_visible()
    expect(page.get_by_text("Thanks, Alex Example. Your order is confirmed.")).to_be_visible()
    expect(page.locator("#order-reference")).to_have_text(re.compile(r"^ORD-[A-Z0-9]+-[A-Z0-9]{4}$"))
    expect(page.get_by_role("button", name="Order placed")).to_be_disabled()
    expect(page.locator("#order-confirmation")).to_have_count(1)
    capture(page, "01-successful-checkout.png")


def test_missing_name_blocks_checkout_and_preserves_cart(page):
    page.get_by_role("button", name="Add Steel Bottle to cart").click()
    page.get_by_role("button", name="Place order").click()

    expect(page.get_by_role("alert")).to_have_text("Please enter your name.")
    expect(page.locator("#order-total")).to_have_text("₹299.00")
    expect(page.get_by_label("Quantity for Steel Bottle", exact=True)).to_have_value("1")
    expect(page.get_by_label("Your name")).to_have_value("")
    expect(page.locator("#order-confirmation")).to_be_hidden()
    capture(page, "02-missing-name.png")


def test_quantity_change_updates_exact_line_and_order_total(page):
    page.get_by_role("button", name="Add Canvas Tote to cart").click()
    page.get_by_role("button", name="Add Steel Bottle to cart").click()
    qty = page.get_by_label("Quantity for Canvas Tote", exact=True)
    qty.fill("2")
    qty.press("Tab")

    expect(page.locator("#cart-rows tr").filter(has_text="Canvas Tote").locator(".line-total")).to_have_text("₹998.00")
    expect(page.locator("#cart-rows tr").filter(has_text="Steel Bottle").locator(".line-total")).to_have_text("₹299.00")
    expect(page.locator("#order-total")).to_have_text("₹1,297.00")
    expect(page.locator("#item-count")).to_have_text("3 items")
    capture(page, "03-quantity-total.png")


def test_empty_cart_is_blocked(page):
    page.get_by_label("Your name").fill("Alex Example")
    page.get_by_role("button", name="Place order").click()

    expect(page.get_by_role("alert")).to_have_text("Your cart is empty. Add an item to continue.")
    expect(page.get_by_label("Your name")).to_have_value("Alex Example")
    expect(page.locator("#order-confirmation")).to_be_hidden()
    capture(page, "04-empty-cart.png")


def test_rapid_double_submit_never_duplicates_confirmation(page):
    page.get_by_role("button", name="Add Canvas Tote to cart").click()
    page.get_by_label("Your name").fill("Alex Example")
    # Two submit events within one JS turn simulate faster-than-human double-submit.
    references = page.evaluate("""() => {
        const form = document.querySelector('#checkout-form');
        form.dispatchEvent(new Event('submit', { bubbles: true, cancelable: true }));
        const first = document.querySelector('#order-reference').textContent;
        form.dispatchEvent(new Event('submit', { bubbles: true, cancelable: true }));
        const second = document.querySelector('#order-reference').textContent;
        return [first, second];
    }""")

    assert references[0] == references[1], "Second submit must retain the first order reference"
    expect(page.get_by_role("heading", name="Order placed successfully!")).to_have_count(1)
    expect(page.locator("#order-confirmation")).to_have_count(1)
    expect(page.locator("#order-reference")).to_have_text(re.compile(r"^ORD-"))
    expect(page.get_by_role("button", name="Order placed")).to_be_disabled()
    capture(page, "05-double-submit.png")
