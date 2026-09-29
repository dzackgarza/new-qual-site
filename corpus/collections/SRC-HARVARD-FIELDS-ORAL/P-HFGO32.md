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

::: {.problem}
Let $t$ be transcendental over $k$, and set
$$
x=\frac{t^3+2}{t^2+3}.
$$
Is $x$ algebraic over $k$?
Justify your answer.
:::

::: {.solution}
No. The element $x$ is transcendental over $k$.

::: pf

::: {.pf-step #s1}

The element $t$ is algebraic over $k(x)$.

::: pf-proof

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

:::

::: {.pf-step #s2}

The element $x$ cannot be algebraic over $k$.

::: pf-proof

Suppose that $x$ were algebraic over $k$. Then the extension $k(x)/k$ would
be algebraic. By step [](#s1){.pf-ref}, $t$ is algebraic over $k(x)$. Algebraicity is transitive,
so $t$ would be algebraic over $k$, contradicting the hypothesis that $t$ is
transcendental over $k$.

:::

:::

::: pf-step

Therefore $x$ is transcendental over $k$.

::: pf-proof

This is the negation of the impossible assumption in step [](#s2){.pf-ref}.

:::

:::

:::

:::
