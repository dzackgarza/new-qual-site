---
schema: qual/card@1
id: P-HFGO32
kind: problem
title: A rational function of a transcendental element
classification:
  areas: [algebra]
  topics: [Field Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard Fields and Galois Theory oral-question extraction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Let $t$ be transcendental over $k$, and set
$$
x=\frac{t^3+2}{t^2+3}.
$$
Is $x$ algebraic over $k$?
Justify your answer.
:::

::: solution
No. The element $x$ is transcendental over $k$.

<1>1. The element $t$ is algebraic over $k(x)$.
::: proof
From
\[
x=\frac{t^3+2}{t^2+3}
\]
we obtain
\[
t^3-xt^2+(2-3x)=0.
\]
Thus $t$ satisfies the monic polynomial
\[
T^3-xT^2+(2-3x)\in k(x)[T],
\]
so $t$ is algebraic over $k(x)$.
:::

<1>2. The element $x$ cannot be algebraic over $k$.
::: proof
Suppose that $x$ were algebraic over $k$. Then the extension $k(x)/k$ would
be algebraic. By <1>1, $t$ is algebraic over $k(x)$. Algebraicity is transitive,
so $t$ would be algebraic over $k$, contradicting the hypothesis that $t$ is
transcendental over $k$.
:::

<1>3. Therefore $x$ is transcendental over $k$.
::: proof
This is the negation of the impossible assumption in <1>2.
:::
:::
