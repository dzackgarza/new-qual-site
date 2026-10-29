---
schema: qual/card@1
id: P-LARQ5
kind: problem
title: $\RR[x,y]/(x)\cong\RR[y]$, so $(x)$ is prime but not maximal
classification:
  areas: [algebra]
  topics: [Ring Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the quotient, primality and maximality requests with Lerman practice problem 5."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Used evaluation at x=0, identified its kernel as (x), and applied the quotient criteria for prime and maximal ideals."
---

::: {.problem}
Prove that $\RR[x,y]/(x)\cong\RR[y]$.
Use this isomorphism to decide whether $(x)$ is prime and whether it is maximal in $\RR[x,y]$.
:::

::: {.solution}

::: pf

::: pf-step

Evaluation at $x=0$ induces the required quotient isomorphism.

::: pf-proof

Define
$$
\Phi:\RR[x,y]\to\RR[y],\qquad
\Phi(f(x,y))=f(0,y).
$$
This is a surjective ring homomorphism, since every polynomial $g(y)$ is the image of the same polynomial viewed in $\RR[x,y]$.

Its kernel consists exactly of the polynomials divisible by $x$. Indeed, write
$$
f(x,y)=a_0(y)+a_1(y)x+\cdots+a_n(y)x^n.
$$
Then $\Phi(f)=a_0(y)$, so $\Phi(f)=0$ if and only if $a_0(y)=0$, which is equivalent to $f\in(x)$. Thus $\ker\Phi=(x)$.

The first isomorphism theorem therefore gives
$$
\RR[x,y]/(x)\cong\RR[y].
$$

:::

:::

::: pf-step

The ideal $(x)$ is prime but not maximal.

::: pf-proof

An ideal $I$ in a commutative ring is prime exactly when the quotient by $I$ is an integral domain, and maximal exactly when that quotient is a field. The ring $\RR[y]$ is an integral domain because $\RR$ is a field, so $(x)$ is prime.

However, $\RR[y]$ is not a field: the nonconstant polynomial $y$ has no multiplicative inverse in $\RR[y]$. Hence $(x)$ is not maximal.

:::

:::

:::

:::
