"use strict";

// Synthetic catalog: integer paise avoided because all prices are fixed whole rupees.
const PRODUCTS = Object.freeze({
  tote: Object.freeze({ id: "tote", name: "Canvas Tote", price: 499 }),
  bottle: Object.freeze({ id: "bottle", name: "Steel Bottle", price: 299 }),
});
const money = (amount) => new Intl.NumberFormat("en-IN", {
  style: "currency", currency: "INR", minimumFractionDigits: 2, maximumFractionDigits: 2,
}).format(amount);

const cart = new Map(); // product ID -> quantity (1 to 99)
let orderPlaced = false;
let discounted = false;
const $ = (id) => document.getElementById(id);
const els = {
  productList: $("product-list"), emptyCart: $("empty-cart"), cartWrapper: $("cart-wrapper"),
  cartRows: $("cart-rows"), itemCount: $("item-count"), orderTotal: $("order-total"),
  form: $("checkout-form"), name: $("customer-name"), error: $("validation-message"),
  placeOrder: $("place-order"), confirmation: $("order-confirmation"),
  confirmedName: $("confirmed-name"), confirmedTotal: $("confirmed-total"),
  reference: $("order-reference"),
};

function subtotal() {
  return [...cart].reduce((sum, [id, qty]) => sum + PRODUCTS[id].price * qty, 0);
}

function discount() { return discounted ? Math.round(subtotal() * 10) / 100 : 0; }
function totalPrice() { return subtotal() - discount(); }
$('apply-discount').addEventListener('click', () => {
  if (orderPlaced) return;
  if ($('promo-code').value.trim().toUpperCase() !== 'SAVE10') {
    showValidation('Invalid discount code.'); return;
  }
  discounted = true;
  clearValidation();
  $('promo-status').textContent = 'SAVE10 applied — 10% discount';
  updateTotals();
});
$('remove-discount').addEventListener('click', () => {
  if (orderPlaced) return;
  discounted = false;
  $('promo-code').value = '';
  $('promo-status').textContent = 'Discount removed.';
  clearValidation(); updateTotals();
});

function itemCount() {
  return [...cart.values()].reduce((sum, qty) => sum + qty, 0);
}

function clearValidation() {
  els.error.hidden = true;
  els.error.textContent = "";
  els.name.removeAttribute("aria-invalid");
}

function showValidation(message, field) {
  els.error.textContent = message;
  els.error.hidden = false;
  if (field === "name") {
    els.name.setAttribute("aria-invalid", "true");
    els.name.focus();
  }
}

function updateTotals() {
  $('subtotal').textContent = money(subtotal());
  $('discount-amount').textContent = '−' + money(discount());
  const count = itemCount();
  $('header-count').textContent = count;
  els.itemCount.textContent = `${count} ${count === 1 ? "item" : "items"}`;
  els.orderTotal.textContent = money(totalPrice());
}

function renderCart() {
  const hasItems = cart.size > 0;
  els.emptyCart.hidden = hasItems;
  els.cartWrapper.hidden = !hasItems;
  els.cartRows.replaceChildren();

  for (const [id, quantity] of cart) {
    const product = PRODUCTS[id];
    const row = document.createElement("tr");
    const nameCell = document.createElement("td");
    nameCell.textContent = product.name;

    const quantityCell = document.createElement("td");
    const quantityInput = document.createElement("input");
    quantityInput.className = "quantity-input";
    quantityInput.type = "number";
    quantityInput.min = "1";
    quantityInput.max = "99";
    quantityInput.step = "1";
    quantityInput.value = String(quantity);
    quantityInput.setAttribute("aria-label", `Quantity for ${product.name}`);

    const lineCell = document.createElement("td");
    lineCell.className = "line-total";
    lineCell.textContent = money(product.price * quantity);
    const actionCell = document.createElement("td");
    const remove = document.createElement("button");
    remove.type = "button";
    remove.className = "remove-button";
    remove.textContent = "Remove";
    remove.setAttribute("aria-label", `Remove ${product.name}`);
    remove.addEventListener("click", () => {
      if (orderPlaced) return;
      cart.delete(id);
      clearValidation();
      renderCart();
    });
    quantityInput.addEventListener("input", () => {
      if (orderPlaced) return;
      const raw = quantityInput.value;
      if (!/^[1-9][0-9]?$/.test(raw)) return; // Don't erase a value while typing.
      const nextQty = Number(raw);
      cart.set(id, nextQty);
      lineCell.textContent = money(product.price * nextQty);
      clearValidation();
      updateTotals();
    });
    quantityInput.addEventListener("change", () => {
      // Revert incomplete or out-of-range quantity entries on commitment.
      const value = quantityInput.value;
      if (!/^[1-9][0-9]?$/.test(value)) { quantityInput.value = String(cart.get(id)); showValidation('Enter a valid quantity of 1 or more.'); }
    });
    const minus = document.createElement('button');
    const plus = document.createElement('button');
    for (const [button, delta, label] of [[minus, -1, 'Decrease'], [plus, 1, 'Increase']]) {
      button.type = 'button'; button.textContent = delta < 0 ? '−' : '+';
      button.setAttribute('aria-label', `${label} quantity for ${product.name}`);
      button.addEventListener('click', () => {
        if (orderPlaced) return;
        const next = cart.get(id) + delta;
        if (next < 1 || next > 99) { showValidation('Enter a valid quantity of 1 or more.'); return; }
        cart.set(id, next); clearValidation(); renderCart();
      });
    }
    quantityCell.append(minus, quantityInput, plus);
    actionCell.append(remove);
    row.append(nameCell, quantityCell, lineCell, actionCell);
    els.cartRows.append(row);
  }
  updateTotals();
}

els.productList.addEventListener("click", (event) => {
  const button = event.target.closest("button[data-add]");
  if (!button || orderPlaced) return;
  const id = button.dataset.add;
  const current = cart.get(id) ?? 0;
  if (current >= 99) {
    showValidation(`Maximum quantity for ${PRODUCTS[id].name} is 99.`);
    return;
  }
  cart.set(id, current + 1);
  clearValidation();
  renderCart();
});

els.name.addEventListener("input", clearValidation);

els.form.addEventListener("submit", (event) => {
  event.preventDefault(); // Never call a payment or remote API.
  if (orderPlaced) return; // Idempotency guard for rapid double-clicks.

  if (cart.size === 0) {
    showValidation("Your cart is empty. Add an item to continue.");
    return;
  }
  const name = els.name.value.trim();
  if (!name) {
    showValidation(els.name.value ? "Please enter a valid name." : "Please enter your name.", "name");
    return; // The cart and user input are intentionally preserved.
  }

  // Set synchronously before modifying the UI: further submissions do nothing.
  orderPlaced = true;
  $('discount-controls').querySelectorAll('button, input').forEach(control => { control.disabled = true; });
  clearValidation();
  const reference = `ORD-${Date.now().toString(36).toUpperCase()}-${Math.random().toString(36).slice(2, 6).toUpperCase()}`;
  els.confirmedName.textContent = name; // textContent avoids HTML injection.
  els.confirmedTotal.textContent = money(totalPrice());
  els.reference.textContent = reference;
  $('confirmed-subtotal').textContent = money(subtotal());
  $('confirmed-discount').textContent = '−' + money(discount());
  $('confirmed-discount-label').textContent = discounted ? 'SAVE10 · 10% off' : 'Discount';
  $('confirmed-items').replaceChildren();
  for (const [id, quantity] of cart) {
    const row = document.createElement('div'); row.className = 'receipt-row';
    const label = document.createElement('span');
    label.textContent = `${PRODUCTS[id].name} × ${quantity}`;
    const amount = document.createElement('strong'); amount.textContent = money(PRODUCTS[id].price * quantity);
    row.append(label, amount); $('confirmed-items').append(row);
  }
  els.confirmation.hidden = false;
  $('confirmation-title').focus({ preventScroll: true });
  els.confirmation.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  els.placeOrder.disabled = true;
  els.placeOrder.textContent = "Order placed";
  els.name.disabled = true;
  els.productList.querySelectorAll("button[data-add]").forEach((button) => { button.disabled = true; });
  els.cartRows.querySelectorAll("button, input").forEach((control) => { control.disabled = true; });
});

$('new-order').addEventListener('click', () => window.location.reload());

renderCart();
