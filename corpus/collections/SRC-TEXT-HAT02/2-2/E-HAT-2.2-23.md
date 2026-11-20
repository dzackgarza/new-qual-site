---
schema: qual/card@1
id: E-HAT-2.2-23
kind: problem
title: If $M_g$ covers $M_h$ then $g = n(h-1)+1$
classification:
  areas:
  - topology
  topics:
  - Euler Characteristic
  - Covering Spaces
  - Surfaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.2, Exercise 23; the stored statement matches the current Cornell text.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Complete cellular/Euler-characteristic computation checked.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the computation: $\chi(M_g)=2-2g$, multiplicativity under an $n$-sheeted covering gives
    $2-2g=n(2-2h)$, and dividing by $-2$ gives $g=n(h-1)+1$ with $n$ the number of sheets.
- event: solution-reviewed
  by: claude
  date: 2026-11-08
  note: >-
    Statement matches Exercise 23 as printed on p. 157, bracketed converse included. The
    argument is correct; chi(M_g) = 2-2g is now cited as the cell count of the standard structure
    of Example 2.36 p. 141 read through the definition of chi on p. 146, the multiplicativity is
    Exercise 22 p. 157, and the converse is explicitly marked as quoted from Example 1.41 p. 73
    rather than proved. What is not covered: the converse construction, and no certificate.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the computation into numbered steps, and supplied the hypothesis the argument uses
    but the prose left implicit: that the covering is finite-sheeted, because the fibre is a
    discrete closed subspace of the compact surface M_g, so the number of sheets n is a positive
    integer and multiplicativity applies. The three cited inputs are kept as cited rather than
    re-proved: chi(M_g) = 2 - 2g from the cell count of Example 2.36 read through the definition,
    Exercise 22 for multiplicativity, and Example 1.41 for the converse, which the card states is
    quoted and not proved. Not re-read this session: printed pp. 141, 146, 157 and 73.
---

::: {.problem}
Show that if the closed orientable surface $M_g$ of genus $g$ is a covering space of $M_h$, then $g = n(h-1)+1$ for some $n$, namely, $n$ is the number of sheets in the covering.
[Conversely, if $g = n(h-1)+1$ then there is an $n$ sheeted covering $M_g \to M_h$, as we saw in Example 1.41.]
:::

::: {.solution}

The computation is the card's own, from the three cited inputs. The statement was checked against Hatcher, *Algebraic Topology* (2002), §2.2 Exercise 23, including the bracketed converse.

Write $\chi(K)=\sum_{k}(-1)^{k}(\text{number of }k\text{-cells})$ for a finite CW complex $K$.

::: pf

::: {.pf-step #chi}
$\chi(M_{g})=2-2g$.

::: pf-proof
The standard CW structure of Example 2.36 has one $0$-cell, $2g$ $1$-cells and one $2$-cell; the alternating sum of those numbers, which is the definition of $\chi$ for a finite CW complex, is $1-2g+1=2-2g$.
:::

:::

::: {.pf-step #finite}
A covering $p\colon M_{g}\to M_{h}$ of closed surfaces is finite-sheeted.

::: pf-proof
A fibre $p^{-1}(y)$ is discrete: each of its points has an open neighbourhood on which $p$ is a homeomorphism, and that neighbourhood meets the fibre only in that point. It is closed, and $M_{g}$ is compact, so the fibre is finite. The cardinality is independent of $y$ because it is locally constant and $M_{h}$ is connected. Call it $n\geq1$.
:::

:::

::: {.pf-step #multiplicative}
$\chi(M_{g})=n\,\chi(M_{h})$.

::: pf-proof
This is Exercise 22 of §2.2, multiplicativity of the Euler characteristic in finite-sheeted coverings: the covering restricts to a covering of each open cell of $M_{h}$ by $n$ open cells of $M_{g}$ of the same dimension, so the alternating cell count of $M_{g}$ is $n$ times that of $M_{h}$.
:::

:::

::: {.pf-step #formula}
$g=n(h-1)+1$.

::: pf-proof
Substituting steps [](#chi){.pf-ref} and [](#multiplicative){.pf-ref} gives $2-2g=n(2-2h)$, that is $2g-2=2n(h-1)$. Dividing by $2$ over the integers gives $g-1=n(h-1)$, hence $g=n(h-1)+1$.
:::

:::

::: {.pf-step}
If $M_{g}$ is an $n$-sheeted covering space of $M_{h}$, then $g=n(h-1)+1$.

::: pf-proof
Steps [](#finite){.pf-ref}, [](#multiplicative){.pf-ref} and [](#formula){.pf-ref}. The bracketed converse in the printed exercise is not proved here: it is the construction of Example 1.41, in which a free action of a cyclic group of order $n$ on $M_{n(h-1)+1}$ produces the $n$-sheeted covering of $M_{h}$, and the card quotes it.
:::

:::

:::

:::
