# Test Cases

Each test starts with a clean browser context. Parameterized case IDs appear separately in the generated reports. Helpers: `add` adds the named product; `qty` commits a quantity; `total` asserts the exact INR total; `order` adds a tote and submits a customer name.

## test_T41 — test_browser.py

Steps: `add(page); page.get_by_label('Your name').fill('Alex'); page.reload()`

Expected assertions: `expect(page.locator('#empty-cart')).to_be_visible(); expect(page.get_by_label('Your name')).to_have_value('')`

## test_T42 — test_browser.py

Steps: `order(page); with browser.new_context() as context:; other=context.new_page(); other.goto(base_url)`

Expected assertions: `expect(other.locator('#empty-cart')).to_be_visible(); expect(other.locator('#order-confirmation')).to_be_hidden()`

## test_T43 — test_browser.py

Steps: `page.locator('.store-logo').focus(); for selector in ['.bag-link','button[data-add="tote"]','button[data-add="bottle"]','#promo-code','#apply-discount','#remove-discount','#customer-name','#place-order']:`

Expected assertions: `page.keyboard.press('Tab'); expect(page.locator(selector)).to_be_focused()`

## test_T44 — test_browser.py

Steps: `page.set_viewport_size({'width':375,'height':812}); add(page); add(page,'Steel Bottle'); for control in page.locator('button:not(#new-order),input').all():; box=control.bounding_box(); assert box['x']>=0 and box['x']+box['width']<=375; page.get_by_label('Your name').fill('Alex'); page.get_by_role('button',name='Place order',exact=True).click()`

Expected assertions: `assert page.evaluate('document.documentElement.scrollWidth <= innerWidth'); control.scroll_into_view_if_needed(); expect(control).to_be_visible(); expect(page.locator('#order-confirmation')).to_be_visible()`

## test_T45 — test_browser.py

Steps: ``

Expected assertions: `order(page); expect(page.locator('#order-confirmation')).to_be_visible()`

## test_T46 — test_browser.py

Steps: `errors=[]; page.on('pageerror',lambda e: errors.append(str(e))); page.on('console',lambda msg: errors.append(msg.text) if msg.type=='error' else None); page.reload(); order(page); assert errors == []`

Expected assertions: `See helper assertions and shared fixture behavior.`

## test_T47 — test_browser.py

Steps: ``

Expected assertions: `order(page,''); expect(page.get_by_role('alert')).to_be_visible(); expect(page.get_by_label('Your name')).to_have_attribute('aria-invalid','true'); expect(page.get_by_label('Your name')).to_be_focused()`

## test_T06 — test_cart.py

Steps: ``

Expected assertions: `add(page); expect(page.locator('#cart-rows')).to_contain_text('Canvas Tote')`

## test_T07 — test_cart.py

Steps: ``

Expected assertions: `add(page); add(page, 'Steel Bottle'); expect(page.locator('#cart-rows tr')).to_have_count(2)`

## test_T08 — test_cart.py

Steps: ``

Expected assertions: `add(page); add(page); expect(page.get_by_label('Quantity for Canvas Tote', exact=True)).to_have_value('2')`

## test_removal — test_cart.py

Steps: `add(page); add(page, 'Steel Bottle'); page.get_by_role('button', name='Remove Canvas Tote', exact=True).click(); total(page, '₹299.00'); if case == 'T10':; page.get_by_role('button', name='Remove Steel Bottle', exact=True).click(); if case == 'T11':`

Expected assertions: `expect(page.locator('#cart-rows')).not_to_contain_text('Canvas Tote'); expect(page.get_by_label('Quantity for Steel Bottle', exact=True)).to_have_value('1'); expect(page.locator('#empty-cart')).to_be_visible(); total(page, '₹0.00'); add(page); expect(page.get_by_label('Quantity for Canvas Tote', exact=True)).to_have_value('1')`

## test_T13 — test_cart.py

Steps: `add(page); add(page, 'Steel Bottle'); qty(page, 3)`

Expected assertions: `expect(page.locator('#item-count')).to_have_text('4 items'); expect(page.locator('#header-count')).to_have_text('4')`

## test_T14 — test_cart.py

Steps: `add(page); page.get_by_role('button', name='Increase quantity for Canvas Tote').click()`

Expected assertions: `expect(page.locator('.line-total')).to_have_text('₹998.00'); total(page, '₹998.00')`

## test_T15 — test_cart.py

Steps: `add(page); add(page, 'Steel Bottle'); qty(page, 3); qty(page, 2, 'Steel Bottle'); total(page, '₹2,095.00')`

Expected assertions: `See helper assertions and shared fixture behavior.`

## test_T16 — test_cart.py

Steps: `add(page); qty(page, 99); total(page, '₹49,401.00')`

Expected assertions: `add(page); expect(page.get_by_label('Quantity for Canvas Tote', exact=True)).to_have_value('99')`

## test_invalid_quantity — test_cart.py

Steps: `add(page); qty(page, 2); qty(page, value)`

Expected assertions: `expect(page.get_by_label('Quantity for Canvas Tote', exact=True)).to_have_value('2'); total(page, '₹998.00'); expect(page.get_by_role('alert')).to_have_text('Enter a valid quantity of 1 or more.')`

## test_T22 — test_cart.py

Steps: `add(page); q=page.get_by_label('Quantity for Canvas Tote', exact=True); q.focus(); q.press('ControlOrMeta+A'); q.press_sequentially('abc'); q.press('Tab')`

Expected assertions: `expect(q).to_have_value('1'); total(page, '₹499.00')`

## test_T23 — test_cart.py

Steps: `add(page); for n, expected in [(3,'₹1,497.00'),(9,'₹4,491.00'),(1,'₹499.00')]:; qty(page,n); total(page,expected)`

Expected assertions: `See helper assertions and shared fixture behavior.`

## test_T24 — test_cart.py

Steps: `add(page); add(page, 'Steel Bottle'); qty(page,99); qty(page,99,'Steel Bottle'); total(page,'₹79,002.00')`

Expected assertions: `See helper assertions and shared fixture behavior.`

## test_successful_checkout_shows_single_confirmation — test_checkout.py

Steps: `page.get_by_role("button", name="Add Canvas Tote to cart").click(); page.get_by_label("Your name").fill("Alex Example"); page.get_by_role("button", name="Place order").click(); capture(page, "01-successful-checkout.png")`

Expected assertions: `expect(page.get_by_role("heading", name="Order placed successfully!")).to_be_visible(); expect(page.get_by_text("Thanks, Alex Example. Your order is confirmed.")).to_be_visible(); expect(page.locator("#order-reference")).to_have_text(re.compile(r"^ORD-[A-Z0-9]+-[A-Z0-9]{4}$")); expect(page.get_by_role("button", name="Order placed")).to_be_disabled(); expect(page.locator("#order-confirmation")).to_have_count(1)`

## test_missing_name_blocks_checkout_and_preserves_cart — test_checkout.py

Steps: `page.get_by_role("button", name="Add Steel Bottle to cart").click(); page.get_by_role("button", name="Place order").click(); capture(page, "02-missing-name.png")`

Expected assertions: `expect(page.get_by_role("alert")).to_have_text("Please enter your name."); expect(page.locator("#order-total")).to_have_text("₹299.00"); expect(page.get_by_label("Quantity for Steel Bottle", exact=True)).to_have_value("1"); expect(page.get_by_label("Your name")).to_have_value(""); expect(page.locator("#order-confirmation")).to_be_hidden()`

## test_quantity_change_updates_exact_line_and_order_total — test_checkout.py

Steps: `page.get_by_role("button", name="Add Canvas Tote to cart").click(); page.get_by_role("button", name="Add Steel Bottle to cart").click(); qty = page.get_by_label("Quantity for Canvas Tote", exact=True); qty.fill("2"); qty.press("Tab"); capture(page, "03-quantity-total.png")`

Expected assertions: `expect(page.locator("#cart-rows tr").filter(has_text="Canvas Tote").locator(".line-total")).to_have_text("₹998.00"); expect(page.locator("#cart-rows tr").filter(has_text="Steel Bottle").locator(".line-total")).to_have_text("₹299.00"); expect(page.locator("#order-total")).to_have_text("₹1,297.00"); expect(page.locator("#item-count")).to_have_text("3 items")`

## test_empty_cart_is_blocked — test_checkout.py

Steps: `page.get_by_label("Your name").fill("Alex Example"); page.get_by_role("button", name="Place order").click(); capture(page, "04-empty-cart.png")`

Expected assertions: `expect(page.get_by_role("alert")).to_have_text("Your cart is empty. Add an item to continue."); expect(page.get_by_label("Your name")).to_have_value("Alex Example"); expect(page.locator("#order-confirmation")).to_be_hidden()`

## test_rapid_double_submit_never_duplicates_confirmation — test_checkout.py

Steps: `page.get_by_role("button", name="Add Canvas Tote to cart").click(); page.get_by_label("Your name").fill("Alex Example"); # Two submit events within one JS turn simulate faster-than-human double-submit.; references = page.evaluate("""() => {; const form = document.querySelector('#checkout-form');; form.dispatchEvent(new Event('submit', { bubbles: true, cancelable: true }));; const first = document.querySelector('#order-reference').textContent;; form.dispatchEvent(new Event('submit', { bubbles: true, cancelable: true }));; const second = document.querySelector('#order-reference').textContent;; return [first, second];; }"""); capture(page, "05-double-submit.png")`

Expected assertions: `assert references[0] == references[1], "Second submit must retain the first order reference"; expect(page.get_by_role("heading", name="Order placed successfully!")).to_have_count(1); expect(page.locator("#order-confirmation")).to_have_count(1); expect(page.locator("#order-reference")).to_have_text(re.compile(r"^ORD-")); expect(page.get_by_role("button", name="Order placed")).to_be_disabled()`

## test_valid_code — test_discounts.py

Steps: `add(page); apply(page,code)`

Expected assertions: `expect(page.locator('#discount-amount')).to_have_text('−₹49.90'); total(page,'₹449.10')`

## test_D02_invalid — test_discounts.py

Steps: ``

Expected assertions: `add(page); apply(page,'WRONG'); expect(page.get_by_role('alert')).to_have_text('Invalid discount code.'); total(page,'₹499.00')`

## test_D03_no_stacking — test_discounts.py

Steps: `add(page); apply(page); apply(page); total(page,'₹449.10')`

Expected assertions: `See helper assertions and shared fixture behavior.`

## test_D04_remove — test_discounts.py

Steps: `add(page); apply(page); page.locator('#remove-discount').click(); total(page,'₹499.00')`

Expected assertions: `See helper assertions and shared fixture behavior.`

## test_D05_recalculate — test_discounts.py

Steps: `add(page); add(page,'Steel Bottle'); apply(page); qty(page,2)`

Expected assertions: `expect(page.locator('#subtotal')).to_have_text('₹1,297.00'); expect(page.locator('#discount-amount')).to_have_text('−₹129.70'); total(page,'₹1,167.30')`

## test_D06_invalid_preserves_discount — test_discounts.py

Steps: `add(page); apply(page); apply(page,'BAD'); total(page,'₹449.10')`

Expected assertions: `See helper assertions and shared fixture behavior.`

## test_discount_boundaries — test_discounts.py

Steps: `add(page); qty(page,quantity); apply(page)`

Expected assertions: `expect(page.locator('#discount-amount')).to_have_text(discount); total(page,amount)`

## test_D08_empty_cart — test_discounts.py

Steps: ``

Expected assertions: `apply(page); total(page,'₹0.00'); expect(page.locator('#discount-amount')).to_have_text('−₹0.00')`

## test_D09_receipt_and_reset — test_discounts.py

Steps: `add(page); apply(page); page.locator('#customer-name').fill('Alex'); page.locator('#place-order').click()`

Expected assertions: `expect(page.locator('#confirmed-items')).to_contain_text('Canvas Tote × 1'); expect(page.locator('#confirmed-subtotal')).to_have_text('₹499.00'); expect(page.locator('#confirmed-discount')).to_have_text('−₹49.90'); expect(page.locator('#confirmed-total')).to_have_text('₹449.10'); page.locator('#new-order').click(); expect(page.locator('#empty-cart')).to_be_visible(); total(page,'₹0.00')`

## test_confirmation — test_order_safety.py

Steps: `order(page); for control in page.locator('#cart-rows button, #cart-rows input, #product-list button, #customer-name, #discount-controls button, #discount-controls input').all():`

Expected assertions: `expect(page.locator('#order-confirmation')).to_be_visible(); expect(page.locator('#order-reference')).to_have_text(re.compile(r'^ORD-[A-Z0-9]+-[A-Z0-9]{4}$')); expect(page.locator('#confirmed-total')).to_have_text('₹499.00'); expect(page.locator('#confirmed-name')).to_have_text('Alex Example'); expect(control).to_be_disabled()`

## test_T36 — test_order_safety.py

Steps: `add(page); page.get_by_label('Your name').fill('Alex'); page.get_by_role('button',name='Place order',exact=True).dblclick()`

Expected assertions: `expect(page.locator('#order-confirmation')).to_have_count(1); expect(page.locator('#order-confirmation')).to_be_visible()`

## test_T37 — test_order_safety.py

Steps: `order(page); ref=page.locator('#order-reference').inner_text(); for _ in range(5): page.locator('#checkout-form').dispatch_event('submit')`

Expected assertions: `expect(page.locator('#order-reference')).to_have_text(ref)`

## test_T40 — test_order_safety.py

Steps: `add(page); page.get_by_label('Your name').fill('Alex'); page.get_by_label('Your name').press('Enter')`

Expected assertions: `expect(page.locator('#order-confirmation')).to_be_visible()`

## test_name_validation — test_validation.py

Steps: ``

Expected assertions: `order(page,name); expect(page.get_by_role('alert')).to_have_text(message); expect(page.locator('#order-confirmation')).to_be_hidden()`

## test_T27 — test_validation.py

Steps: ``

Expected assertions: `order(page,'  Alex Example  '); expect(page.locator('#confirmed-name')).to_have_text('Alex Example')`

## test_T28 — test_validation.py

Steps: ``

Expected assertions: `order(page,''); page.get_by_label('Your name').fill('Alex'); expect(page.get_by_role('alert')).to_be_hidden()`

## test_T29 — test_validation.py

Steps: `add(page); qty(page,3); page.get_by_role('button',name='Place order',exact=True).click()`

Expected assertions: `total(page,'₹1,497.00'); expect(page.get_by_label('Quantity for Canvas Tote',exact=True)).to_have_value('3')`

## test_T30 — test_validation.py

Steps: `page.get_by_role('button',name='Place order',exact=True).click()`

Expected assertions: `expect(page.get_by_role('alert')).to_contain_text('Your cart is empty'); expect(page.locator('#order-confirmation')).to_be_hidden()`

## test_T31 — test_validation.py

Steps: `name='<img src=x onerror=alert(1)>'; order(page,name)`

Expected assertions: `expect(page.locator('#confirmed-name')).to_have_text(name); expect(page.locator('#confirmed-name img')).to_have_count(0)`

## T48 — Repeatability

Run the full suite twice in separate executions. Expect equal passing counts and no state leakage. See TEST_RESULTS.md.

## Mandatory human checks

T04: Open a fresh page, enter Alex Example, leave cart empty and click Place order. Expect an empty-cart error, retained name and no receipt.

T05: Open a fresh page, add Canvas Tote, enter Alex Example and physically double-click Place order. Expect one receipt/reference and disabled editing. Record actual observations in MANUAL_TEST_LOG.md.
