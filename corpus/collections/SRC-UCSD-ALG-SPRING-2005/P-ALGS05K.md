---
schema: qual/card@1
id: P-ALGS05K
kind: problem
title: "In a ring where every element satisfies x^n = x, every prime ideal is maximal"
classification:
  areas:
  - algebra
  topics:
  - Commutative Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
Let $R$ be a commutative ring with identity element.
Suppose that for each $x \in R$ there is an $n(x) > 1$ such that $x^{n(x)} = x$.
Show that every prime ideal of $R$ is maximal.
:::

::: {.solution}
<1>1. Let $P$ be a prime ideal of $R$, and consider the integral domain $D = R/P$.
Proof: the quotient of a ring by a prime ideal is an integral domain.

<1>2. For each $\bar x \in D$ (with $\bar x \neq 0$), there is $n > 1$ with $\bar x^n = \bar x$.
Proof: the condition $x^{n(x)} = x$ descends to the quotient.

<1>3. Hence $\bar x^{n-1} = 1$ in $D$ (since $\bar x \neq 0$ and $D$ is a domain, we can cancel $\bar x$).
Proof: $\bar x^n = \bar x$ gives $\bar x(\bar x^{n-1} - 1) = 0$; since $\bar x \neq 0$ and $D$ is a domain, $\bar x^{n-1} = 1$.

<1>4. Hence every nonzero element of $D$ is a unit.
Proof: <1>3 shows $\bar x$ has inverse $\bar x^{n-2}$.

<1>5. Therefore $D$ is a field.
Proof: an integral domain in which every nonzero element is a unit is a field.

<1>6. Hence $P$ is maximal.
Proof: $R/P$ is a field iff $P$ is maximal.

<1>7. Q.E.D.
Proof: <1>6.
:::
