---
schema: qual/card@1
id: P-CASP07D
kind: problem
title: 'Roots of $z^n+z^{-m}=w$ in a disc by Rouché''s theorem'
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured the prose solution into a Lamport proof and checked it: clearing the
    denominator preserves multiplicities away from 0 and P(0) = 1 introduces no spurious
    zero, the boundary inequality uses 2^m + 1 < 2^(m+1) <= 2^(m+n) for n >= 1, and
    Rouche on B(0,2) gives m+n zeros. The correspondence between zeros of P and roots of
    the original equation is now a step. The collection's provenance is the examination
    paper only, so no retained solution set covers the exercise and the argument is the
    card's own.
---

::: {.problem}
Let $n$ and $m$ be positive integers.
Fix $w$ with $\abs{w} \leq 1$ and consider the equation $$z^n + \frac{1}{z^m} = w.$$ How many roots (counting multiplicities) are there in $B(0, 2)$?
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own.

::: pf

::: {.pf-step #clearing}
For $z\ne0$ the equation $z^n+z^{-m}=w$ holds if and only if $P(z)\coloneqq z^{m+n}-wz^m+1$ vanishes, and the zeros of $P$ in $B(0,2)$ are exactly the roots there of the original equation, with the same multiplicities.

::: pf-proof
Multiply by $z^m$, which is nonzero at $z\ne0$ and holomorphic and zero-free near any such point, so it preserves the order of vanishing of $z^n+z^{-m}-w$ at every $z\ne0$. At $z=0$ the function $z^n+z^{-m}$ is not defined, and $P(0)=1\ne0$, so clearing denominators introduces no zero inside $B(0,2)$.
:::

:::

::: {.pf-step #inequality}
On the circle $\abs{z}=2$,
$$
\abs{-wz^m+1}\le\abs{w}2^m+1\le2^m+1<2^{m+n}=\abs{z^{m+n}} .
$$

::: pf-proof
The first inequality is the triangle inequality with $\abs{z^m}=2^m$, and $\abs{-wz^m+1}=\abs{1-wz^m}$; the second uses $\abs{w}\le1$. For the strict inequality, $n\ge1$ gives $2^{m+n}\ge2^{m+1}=2\cdot2^m>2^m+1$.
:::

:::

::: {.pf-step #rouche}
$P$ and $z\mapsto z^{m+n}$ have the same number of zeros in $B(0,2)$, counted with multiplicity, namely $m+n$.

::: pf-proof
Both are holomorphic on a neighbourhood of the closed disc $\overline{B(0,2)}$, and step [](#inequality){.pf-ref} shows that the perturbation $-wz^m+1$ is dominated on the boundary circle by $\abs{z^{m+n}}$, which is nowhere zero there. Rouché's theorem therefore gives equal zero counts in $B(0,2)$, and $z^{m+n}$ has the zero $0$ of multiplicity $m+n$ and no other.
:::

:::

::: {.pf-step}
The equation $z^n+z^{-m}=w$ has exactly $\boxed{m+n}$ roots in $B(0,2)$, counted with multiplicity.

::: pf-proof
Step [](#rouche){.pf-ref} counts the zeros of $P$ there and step [](#clearing){.pf-ref} identifies them with the roots of the original equation, multiplicities included.
:::

:::

:::
:::
