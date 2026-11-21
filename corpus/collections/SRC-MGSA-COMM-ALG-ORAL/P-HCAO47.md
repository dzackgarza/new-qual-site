---
schema: qual/card@1
id: P-HCAO47
kind: problem
title: A base-ring element invertible in an integral extension is already invertible
classification:
  areas:
  - algebra
  topics:
  - Integral Extensions
  - Unit Groups
  - Rings
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard Commutative Algebra oral-question extraction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured as a Lamport proof of the same argument. The one place the prose ran two computations
    together is the multiplication by x^{n-1}: the card now states separately that x^{n-1} y^k equals
    x^{n-1-k}(xy)^k, which is what turns each term into an element of A, and covers the two boundary cases
    k = n-1 (giving a_(n-1)) and k = n (giving y) where the formula would otherwise show a negative power.
    No published solution located; the card keeps its own argument and says so.
---

::: {.problem}
Let $A\subseteq B$ be commutative rings, with $B$ integral over $A$.
If $x\in A$ is a unit in $B$, show that $x$ is a unit in $A$.
:::

::: {.solution}

No published solution was located for this oral question; the argument is the card's own, and it is the standard one: a negative power of $x$ is turned into a nonnegative one by multiplying the integral relation through by a power of $x$.

The statement was checked against the preserved Harvard Commutative Algebra oral-question extraction. Throughout, $A\subseteq B$ are commutative rings with $B$ integral over $A$ — every element of $B$ satisfies a monic polynomial with coefficients in $A$ — and $x\in A$ is a unit in $B$, with inverse $y\coloneqq x^{-1}\in B$.

::: pf

::: {.pf-step #integral}

$y$ is integral over $A$, so there are $n\geq1$ and $a_{0},\dots,a_{n-1}\in A$ with $y^{n}+a_{n-1}y^{n-1}+\cdots+a_{1}y+a_{0}=0$.

::: pf-proof

Every element of $B$ is integral over $A$, because $B$ is integral over $A$; applied to $y\in B$ this gives a monic polynomial over $A$ of some degree $n\geq1$ vanishing at $y$, which is the displayed relation.

:::

:::

::: {.pf-step #powers}

For $0\leq k\leq n-1$ one has $x^{n-1}y^{k}=x^{n-1-k}(xy)^{k}=x^{n-1-k}$, and $x^{n-1}y^{n}=y$.

::: pf-proof

$xy=1$, so $(xy)^{k}=1$ for every $k\geq0$, and therefore $x^{n-1}y^{k}=x^{n-1-k}(xy)^{k}=x^{n-1-k}$ for $0\leq k\leq n-1$, the exponent $n-1-k$ being nonnegative there. For $k=n$ the same computation reads $x^{n-1}y^{n}=x^{-1}(xy)^{n}=x^{-1}=y$, and this is the term the relation is solved for, so no negative power of $x$ remains in the other summands.

:::

:::

::: {.pf-step #multiplied}

Multiplying the relation of step [](#integral){.pf-ref} by $x^{n-1}$ gives $y+a_{n-1}+a_{n-2}x+\cdots+a_{1}x^{n-2}+a_{0}x^{n-1}=0$.

::: pf-proof

Multiply $y^{n}+a_{n-1}y^{n-1}+\cdots+a_{0}=0$ by $x^{n-1}$ and apply step [](#powers){.pf-ref} term by term: the first term becomes $x^{n-1}y^{n}=y$, the term $a_{n-1}y^{n-1}$ becomes $a_{n-1}(xy)^{n-1}=a_{n-1}$, and for $0\leq k\leq n-2$ the term $a_{k}y^{k}$ becomes $a_{k}x^{n-1-k}(xy)^{k}=a_{k}x^{n-1-k}$. Collecting the powers of $x$ in increasing order gives the displayed relation.

:::

:::

::: {.pf-step #in-base}

$y\in A$.

::: pf-proof

The relation of step [](#multiplied){.pf-ref} reads $y=-\big(a_{n-1}+a_{n-2}x+\cdots+a_{0}x^{n-1}\big)$, and the right-hand side is an element of $A$, being a sum of products of elements of $A$ and powers of $x\in A$.

:::

:::

::: pf-step

$x$ is a unit of $A$.

::: pf-proof

$y\in A$ by step [](#in-base){.pf-ref} and $xy=1$ by the definition of $y$, so $y$ is an inverse of $x$ inside $A$; that is, $x\in A^{\times}$.

:::

:::

:::

:::
