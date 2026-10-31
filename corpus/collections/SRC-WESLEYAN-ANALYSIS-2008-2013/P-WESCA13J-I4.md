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

Let $f$ be holomorphic on a punctured neighborhood $0<\abs{z-a}<r$.
Then $a$ is an isolated singularity of $f$, with Laurent expansion
$$
f(z)
=
\sum_{n=-\infty}^{\infty}
c_n(z-a)^n.
$$

::: pf-proof

This is the standard ambient situation in which removable singularities, poles, and essential singularities are defined.
A function holomorphic on an annulus has a Laurent expansion converging there.

:::

:::

::: {.pf-step #laurent-types}

The point $a$ is a removable singularity exactly when every $c_{-n}$, $n\ge1$, vanishes, and a pole of order $m$ exactly when $c_{-m}\ne0$ and $c_{-n}=0$ for $n>m$.

::: pf-proof

If every negative-power coefficient vanishes, the Laurent series is a Taylor series, which extends $f$ holomorphically to $a$; conversely a holomorphic extension has a Taylor series, and the Laurent expansion is unique.
If the principal part ends at $c_{-m}(z-a)^{-m}$ with $c_{-m}\ne0$, then $(z-a)^m f(z)$ extends holomorphically to $a$ with value $c_{-m}\ne0$, so $a$ is a pole of order $m$; conversely, if $(z-a)^m f(z)=g(z)$ with $g$ holomorphic and $g(a)\ne0$, the Taylor series of $g$ divided by $(z-a)^m$ is the Laurent series of $f$.

:::

:::

::: pf-step

The point $a$ is an essential singularity of $f$ if it is neither a removable singularity nor a pole:
$$
\boxed{
a\text{ is essential for }f
\iff
a\text{ is an isolated singularity that is neither removable nor a pole},}
$$
equivalently, infinitely many of the coefficients $c_{-1},c_{-2},\ldots$ are nonzero.

::: pf-proof

The first form is the definition.
By step [](#laurent-types){.pf-ref}, the removable and pole cases are exactly the cases in which only finitely many negative-power coefficients are nonzero, so the remaining case is exactly the case of infinitely many nonzero negative-power coefficients.

:::

:::

:::

:::
