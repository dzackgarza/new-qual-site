---
schema: qual/card@1
id: P-C2ZOD
kind: problem
title: No finite field is algebraically closed
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
  - Fields
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved UGA problem-set reproduction, including the stated product-polynomial hint.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against the printed exercise, Hungerford, Algebra (1974), section V.3,
    exercise 8, book page 267, read from the page image: "No finite field K is
    algebraically closed. [Hint: If K = {a_0, ..., a_n} consider
    a_1 + (x - a_0)(x - a_1)···(x - a_n) ∈ K[x], where a_1 ≠ 0.]" The card keeps
    the printed hint and the printed condition a_1 ≠ 0; the checked-in extraction
    renders the subscript as a_i, and the page image shows a_1, so the card is
    right and the extraction is not. The proof was checked: the polynomial has
    degree n + 1 > 0 because adding the constant does not touch the leading term,
    and f(a_j) = a_1 ≠ 0 at every element of K because the factor x - a_j
    vanishes. Complete; no defect.
---

::: {.problem}
Show that no finite field is algebraically closed.

*Hint: if $K = \{a_i\}_{i=0}^n$, consider*
$$
f(x) = a_1 + \prod_{i=0}^n (x - a_i) \in K[x]
$$
*where $a_1 \neq 0$.*
:::

::: {.solution}
Let
$$
K=\{a_0,a_1,\ldots,a_n\}
$$
be finite, with $a_1\ne0$, and define
$$
f(x)=a_1+\prod_{i=0}^n(x-a_i)\in K[x].
$$

::: pf

::: {.pf-step #s1}

The polynomial $f$ is nonconstant.

::: pf-proof

The product has degree $n+1$, so adding the constant $a_1$ does not change its
leading term. Hence $\deg f=n+1>0$.

:::

:::

::: {.pf-step #s2}

The polynomial $f$ has no root in $K$.

::: pf-proof

Every $a\in K$ equals $a_j$ for some $j$. Substituting $a_j$ gives
$$
f(a_j)=a_1+\prod_{i=0}^n(a_j-a_i)=a_1,
$$
because the factor with $i=j$ is zero. Since $a_1\ne0$, one has
$f(a_j)\ne0$. Thus no element of $K$ is a root.

:::

:::

::: pf-step

Therefore $K$ is not algebraically closed.

::: pf-proof

An algebraically closed field has a root for every nonconstant polynomial over
it. By steps [](#s1){.pf-ref} and [](#s2){.pf-ref}, $f\in K[x]$ is nonconstant and has no root in $K$.

:::

:::

:::

:::
