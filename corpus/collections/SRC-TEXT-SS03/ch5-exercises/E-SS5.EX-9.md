---
schema: qual/card@1
id: E-SS5.EX-9
kind: problem
title: $\prod_{k\ge0}(1+z^{2^k})=\frac1{1-z}$ for $\abs z<1$
classification:
  areas:
  - complex-analysis
  topics:
  - Infinite Products
  - Power Series
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured the prose solution into Lamport steps. The collection's provenance is the publisher's catalogue record only, with no retained text and no retained solution set, so the statement is taken as the card prints it; the argument is the card's own. Checked: the telescoping identity by induction, the vanishing of $z^{2^{N+1}}$ inside the unit disc, and that $1-z\neq0$ there so the division is legitimate.
---

::: {.exercise}
Prove that if $\abs{ z } < 1$ , then

$$
(1 + z) (1 + z ^ {2}) (1 + z ^ {4}) (1 + z ^ {8}) \dots = \prod_ {k = 0} ^ {\infty} (1 + z ^ {2 ^ {k}}) = \frac {1}{1 - z}.
$$
:::

::: {.solution}
No retained text and no retained solution set for this collection: its provenance is the publisher's catalogue record, so the statement is taken as the card prints it, and the argument is the card's own. The telescoping identity was checked for every $N$ and the limit taken inside the open unit disc.

::: pf

::: {.pf-step #finite}
For every $N\ge0$, $(1-z)\prod_{k=0}^{N}(1+z^{2^k})=1-z^{2^{N+1}}$.

::: pf-proof
Induction on $N$: for $N=0$ it is $1-w^2=(1-w)(1+w)$ with $w=z$; and multiplying the identity for $N-1$ by $1+z^{2^N}$ turns $1-z^{2^N}$ into $(1-z^{2^N})(1+z^{2^N})=1-z^{2^{N+1}}$.
:::
:::

::: {.pf-step #limit}
For $\abs z<1$ the right side tends to $1$ as $N\to\infty$.

::: pf-proof
$\abs{z^{2^{N+1}}}=\abs z^{2^{N+1}}$ and $2^{N+1}\to\infty$ with $\abs z<1$, so the power tends to $0$.
:::
:::

::: {.pf-step #product}
$\prod_{k=0}^{\infty}(1+z^{2^k})=\frac{1}{1-z}$ for $\abs z<1$, so the product converges there.

::: pf-proof
Divide the identity of step [](#finite){.pf-ref} by $1-z$, which is nonzero because $\abs z<1$, and let $N\to\infty$ using step [](#limit){.pf-ref}: the finite products converge to $1/(1-z)$, which is exactly convergence of the infinite product to that value.
:::
:::

:::
:::
