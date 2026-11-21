# Requirement-to-test traceability

| Requirement | Test IDs | Source |
|---|---|---|
| Successful checkout, reference and amount | T01, T32–T35 | test_checkout.py, test_order_safety.py |
| Cart add/remove/count | T06–T13 | test_cart.py |
| Exact quantity arithmetic and INR | T03, T14–T16, T23–T24 | test_checkout.py, test_cart.py |
| Reject invalid quantities, restore previous value | T17–T22 | test_cart.py |
| Name required, trimming, safe rendering, state retained | T02, T25–T31 | test_checkout.py, test_validation.py |
| Empty-cart prevention | T04, T30; human T04 | test_checkout.py, test_validation.py, MANUAL_TEST_LOG.md |
| Duplicate prevention and editing lock | T05, T36–T39; human T05 | test_checkout.py, test_order_safety.py |
| Enter/Tab navigation and accessible errors | T40, T43, T47 | test_order_safety.py, test_browser.py |
| Refresh and browser isolation | T41–T42 | test_browser.py |
| Mobile controls and overflow | T44 | test_browser.py |
| Cross-engine essential behavior | T45 plus full suite per engine | test_browser.py, generated reports |
| No console/runtime errors | T46 | test_browser.py |
| Repeatable execution | T48 | repeated full-suite reports |
| SAVE10 case-insensitivity | D01 (3 inputs) | test_discounts.py |
| Invalid coupon and existing discount preservation | D02, D06 | test_discounts.py |
| No stacking, removal, recalculation | D03–D05 | test_discounts.py |
| Discount bounds and zero subtotal | D07 (2 inputs), D08 | test_discounts.py |
| Discounted receipt and reset | D09 | test_discounts.py |

Execution status and actual counts are in TEST_RESULTS.md. Test IDs in reports are preserved in function/parameter names, except the original T01–T05 descriptive functions in test_checkout.py (in that order).
