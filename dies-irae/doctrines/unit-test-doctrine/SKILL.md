---
name: unit-test-doctrine
description: Apply the house unit-test doctrine whenever designing, adding, changing, reviewing, or deleting unit tests. Use it during ordinary forward implementation to prevent test-per-change accretion and reserve permanent unit tests for carefully selected, durable interactions.
---

# Unit Test Doctrine

Most unit tests you instinctively want to write are useless, full stop.

This is not a point of moral blame, but merely an unfortunate fact about your
training as a model that must be corrected for.

The most damaging pattern you may find yourself tempted to engage in is the
"potemkin test": some feature was removed, or narrowed, or altered, so you feel
the need to add a test to assert the new behavior. This test will likely be
*nowhere close to the Pareto front of usefulness*. If the entire test suite was
wiped clean and regenerated such a test would likely not come close to being
featured.

Please, I'm begging you, catch yourself before you write tests like this.

*It is OK to leave code untested*

*Most code should not be tested*

Only truly nontrivial interactions deserve tests; those tests must be carefully
selected and planned to reflect *durable behavior* rather than accidents of
implementation or, worse, mere history.

Nontrivial bugs also probably deserve tests; such tests should have a comment
noting the subtlety or non-obviousness that led to the problem being missed on
first impl.

Many bugs do not merit a test because once fixed it's impossible to imagine
them getting un-fixed, so the test earns nothing; only bugs where someone with
a fresh context can come in and repeat the error deserve a regression.

As the user I will be much less frustrated by missing or sparse tests than by
an ever-accumulating wall of slop tests. If the wall of slop tests accumulates
too much I will have them wiped, and they will have been useless anyway!

Look for good proptest opportunities. Property testing is great -- but don't
shoehorn it.
