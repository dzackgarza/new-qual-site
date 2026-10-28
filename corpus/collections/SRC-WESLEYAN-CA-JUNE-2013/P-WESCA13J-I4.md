---
schema: qual/card@1
id: P-WESCA13J-I4
kind: problem
title: 'Define an essential singularity'
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Theorems and Definitions, item 4 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md.
---

::: {.problem}
Define an essential singularity of an analytic function.
:::

::: {.solution}

::: pf

::: pf-step

Let
$$
f
$$
be holomorphic on a punctured neighborhood
$$
0<|z-a|<r.
$$
Then
$$
a
$$
is an isolated singularity of
$$
f.
$$


::: pf-proof

This is the standard ambient situation in which removable singularities, poles, and essential singularities are defined.

:::

:::

::: {.pf-step #s1-2}

The point
$$
a
$$
is called an essential singularity of
$$
f
$$
if it is neither a removable singularity nor a pole.


::: pf-proof

Equivalently:

1. there is no holomorphic extension of
$$
f
$$
to
$$
a;
$$
2. there is no positive integer
$$
m
$$
such that
$$
(z-a)^m f(z)
$$
extends holomorphically to
$$
a
$$
with nonzero value there.

These two exclusions distinguish an essential singularity from the other two possible types of isolated singularity.

:::

:::

::: {.pf-step #s1-3}

In terms of the Laurent expansion
$$
f(z)
=
\sum_{n=-\infty}^{\infty}
c_n(z-a)^n,
$$
the singularity at
$$
a
$$
is essential if and only if infinitely many negative-power coefficients
$$
c_{-1},c_{-2},\ldots
$$
are nonzero.


::: pf-proof

If every negative-power coefficient vanishes, the Laurent series is a Taylor series and the singularity is removable.

If only finitely many negative-power coefficients are nonzero, then the principal part has a highest negative power
$$
c_{-m}(z-a)^{-m},
\qquad
c_{-m}\ne0,
$$
so
$$
a
$$
is a pole of order
$$
m.
$$

Thus the remaining case, namely infinitely many nonzero negative-power terms, is exactly the essential case.

:::

:::

::: pf-step

Therefore the requested definition is
$$
\boxed{
a\text{ is essential for }f
\iff
a\text{ is an isolated singularity that is neither removable nor a pole}.}
$$


::: pf-proof

Step [](#s1-2){.pf-ref} gives the definition, and step [](#s1-3){.pf-ref} gives the standard equivalent Laurent-series criterion.

:::

:::

:::

:::
