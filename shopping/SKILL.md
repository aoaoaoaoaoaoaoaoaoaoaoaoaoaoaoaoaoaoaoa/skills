---
name: shopping
description: Find purchasable offers for an exact bill of materials and construct the lowest landed-cost feasible order plan, optionally subject to an arrive-by deadline. Use when Codex must source one or more specified products across manufacturers, retailers, specialist merchants, marketplaces, local pickup, open-box, refurbished, or second-hand listings; test coupons and cart thresholds; account for packs, bundles, shipping, taxes, duties, rebates, and delivery risk; or compare the cheapest, simplest, and deadline-safe baskets.
---

# Shopping

## Mandate

Turn a bill of materials into an evidence-backed purchase plan. Hold the
specification fixed, search broadly, normalize actual offers, and optimize
whole carts rather than choosing each line independently.

Report the best observed plan as of a stated time. Internet-wide optimality is
not provable; never call a bounded search the global minimum.

## Lock The Procurement Contract

Before asking for reusable buyer facts, read `~/documents/INDEX.md` when it
exists. Use only entries explicitly marked current or default. Follow its
explicit links when a required fact is absent or its provenance matters; do not
search the documents tree blindly. Ask when no current, unambiguous fact can be
resolved. The index supplies facts, not authorization to order, and unrelated
contents must not enter the procurement report.

Recover or obtain:

- destination country and postal code
- each required specification, part number or model, variant, and quantity
- whether equivalent brands or functional substitutes are admissible
- allowed condition: new, open-box, refurbished, and/or used
- local-pickup radius or exclusion
- arrive-by deadline, if any, and whether it is hard or preferred
- memberships, payment instruments, store credit, loyalty balances, and
  coupons already available
- whether account creation, first-order offers, subscriptions, rebates, or
  cashback portals are acceptable

Treat a generic specification as freedom within that specification, not
permission to weaken it. Treat a named model or part number as exact unless
the user authorizes substitutes. Put useful out-of-spec alternatives in a
separate annex rather than silently changing the bill.

Unless instructed otherwise:

- allow split orders
- compare new and second-hand plans separately
- assign no resale value to surplus items
- do not open a membership, subscription, financing product, or credit card
- include applicable sales or use tax whether or not the merchant collects it
- exclude rewards tied to payment instruments the user does not already hold

Begin searching while resolving immaterial gaps. Ask before proceeding only
when different answers could change product identity, feasibility, or the
winning plan.

## Define Cost

For each plan, compute:

```text
landed cost =
  merchandise
  + order-level shipping and handling
  + applicable tax, duty, brokerage, payment, foreign-exchange, recycling,
    core, and mandatory fees
  + any newly required membership
  - discounts applied at checkout
  - certain post-purchase rebates
```

Report immediate checkout outlay and net certain cost separately. Keep
uncertain, delayed, illiquid, or effortful value outside the certain total:

- untested coupon codes
- card-linked offers not yet activated
- cashback portals
- mail-in or approval-contingent rebates
- loyalty points
- price matches not yet granted
- speculative resale value

Quantify this conditional upside when useful, with its conditions and expiry.
Do not treat a free trial as free if forgetting to cancel creates a liability.

Count the full price of unwanted filler used to cross a shipping threshold.
Allow overbuying or a larger pack when it lowers total cost, but disclose the
surplus. For international offers, include lawful import costs or state a
defensible range when checkout cannot determine them. For local pickup, include
unavoidable fares, fuel, and tolls; do not invent an hourly value for the
buyer's time.

## Build The Offer Ledger

Search exact model numbers, manufacturer part numbers, UPCs, dimensions, and
decisive specification phrases. Cover the channels the goods warrant:

- manufacturer and authorized-dealer pages
- category specialists and independent retailers
- major general retailers and warehouse clubs
- marketplaces and reputable third-party sellers
- manufacturer-refurbished, open-box, outlet, and liquidation inventory
- eBay, Mercari, Craigslist, Facebook Marketplace, OfferUp, and
  category-specific second-hand markets
- local inventory and pickup
- Freecycle, Buy Nothing, and other lawful free or community reuse channels
  when condition and availability can be verified
- multi-item kits, lots, and bundles that cover several bill lines

Use search engines and price aggregators for discovery. Use the merchant
listing, seller listing, promotion terms, and actual cart as evidence.
Affiliate pages, coupon aggregators, and search snippets do not prove price,
stock, eligibility, or delivery.

Search official promotions, merchant banners, newsletters, first-order
offers, loyalty pricing, bundle discounts, price matching, price adjustment,
cashback portals, and reputable discounted gift-card channels when the
procurement contract permits them. Test a coupon in the cart before treating
it as real. Do not consume a single-use offer until the candidate plan merits
it.

When the purchase may be delayed, consult reliable price history and known sale
cadence where available. Present waiting as a separate contingent strategy,
not as a purchasable current offer.

Record each offer with:

- exact covered bill lines and quantities
- merchant, marketplace, and actual seller
- model, variant, pack size, and included accessories
- condition and material defects
- item price and order-level promotion rules
- shipping threshold, shipping charge, and pickup cost
- tax, duties, and mandatory fees, or a stated bound
- stock status and quantity limit
- destination-specific delivery window
- return policy, warranty, and authorized-seller status
- seller rating and counterfeit or fulfillment risk where material
- direct evidence URL and observation time

For second-hand goods, inspect the actual listing, photographs, completeness,
wear, seller history, returnability, shipping origin, and compatibility.
Never collapse used, refurbished, open-box, and new into one undifferentiated
price list.

Discard offers that are out of stock, variant-mismatched, subscription-priced
without authorization, geographically infeasible, expired, or dependent on an
unverified condition. Deduplicate mirrored and affiliate listings.

## Optimize The Basket

Model packs, bundles, lots, shipping thresholds, cart-wide coupons, merchant
limits, and surplus explicitly. A locally cheapest line can make the complete
basket more expensive.

For a small bill, enumerate plausible merchant-cart combinations. For a
nontrivial bill, write a disposable exact solver or integer program. Tooling is
expendable; arithmetic is not. Require every bill quantity to be covered and
charge each order-level cost exactly once.

Prune a candidate only when another covers at least the same requirements with
no greater certain cost and no worse condition, delivery, warranty, or risk.
Retain a dominated-looking offer when it enables a shipping threshold,
cart-wide promotion, price match, or deadline-safe backup.

Produce, when distinct:

1. the lowest net-certain-cost plan
2. the lowest deadline-feasible plan
3. the lowest second-hand or mixed-condition plan
4. a lower-friction plan when the mathematical minimum fragments the purchase
   across many sellers for a trivial saving

The first plan remains the cost optimum. State the exact premium paid by any
simpler alternative rather than silently monetizing convenience.

Compare against the best single-merchant basket. This exposes whether splitting
orders actually earns its ceremony.

## Adjudicate Delivery

Prefer a destination-specific checkout estimate over generic product-page
copy. Distinguish:

- guaranteed arrival
- retailer-estimated arrival
- seller handling time plus carrier estimate
- stock or backorder date
- ship-by date

An arrive-by constraint concerns possession, not dispatch. The complete bill
arrives when its last required line arrives. Account for weekends, holidays,
customs, marketplace handling, local-pickup availability, and the probability
that a used listing is no longer available.

Assign concise confidence to each deadline claim and explain the decisive
evidence. For a hard deadline, reject plans with no credible margin and retain
a backup for critical or failure-prone lines when its cost is materially
justified.

## Validate At Checkout

Stage the recommended carts without submitting them. Recheck:

- exact item, variant, condition, quantity, and seller
- coupon acceptance and stacking
- merchandise subtotal
- shipping and mandatory fees
- destination tax and import charges
- stock and purchase limits
- final delivery window
- return and warranty terms

Prices and stock decay quickly. Revalidate immediately before an authorized
purchase. Use a dedicated email alias for any newly created commercial account
unless the service has a legitimate identity-bound reason to require the
canonical address.

Never submit an order, create a financial or recurring obligation, or consume a
single-use entitlement without explicit authorization for that action.

## Deliver The Plan

State the observation time, destination, deadline, condition scope, and
material assumptions. Then give:

| Order | Merchant and seller | Bill lines | Condition | Merchandise | Discounts | Shipping and fees | Tax and duty | Net certain cost | Arrival |
|---|---|---|---|---:|---:|---:|---:|---:|---|

Follow the table with:

- immediate checkout outlay and net certain total
- direct links supporting every recommended offer and promotion
- savings against the best single-merchant basket
- surplus quantities, conditional upside, and unresolved tax ranges
- delivery confidence and material return, warranty, seller, or counterfeit
  risks
- the exact cost difference for each useful alternative
- the remaining action required to buy

If the search is incomplete, say which channels or facts remain unresolved.
If no admissible plan meets the deadline, say so and present the nearest
feasible alternatives without relabeling them compliant.
