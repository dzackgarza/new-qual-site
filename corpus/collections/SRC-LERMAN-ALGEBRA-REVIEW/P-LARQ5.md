---
schema: qual/card@1
id: P-LARQ5
kind: problem
title: Quotient of a bivariate polynomial ring by (x)
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
Prove that $\mathbb R[x,y]/(x)\cong\mathbb R[y]$.
Use this isomorphism to decide whether $(x)$ is prime and whether it is maximal in $\mathbb R[x,y]$.
:::

::: {.solution}
<1>1. Evaluation at $x=0$ induces the required quotient isomorphism.
::: {.proof}
Define
$$
\Phi:\mathbb R[x,y]\to\mathbb R[y],\qquad
\Phi(f(x,y))=f(0,y).
$$
This is a surjective ring homomorphism, since every polynomial $g(y)$ is the image of the same polynomial viewed in $\mathbb R[x,y]$.

Its kernel consists exactly of the polynomials divisible by $x$. Indeed, write
$$
f(x,y)=a_0(y)+a_1(y)x+\cdots+a_n(y)x^n.
$$
Then $\Phi(f)=a_0(y)$, so $\Phi(f)=0$ if and only if $a_0(y)=0$, which is equivalent to $f\in(x)$. Thus $\ker\Phi=(x)$.

The first isomorphism theorem therefore gives
$$
\mathbb R[x,y]/(x)\cong\mathbb R[y].
$$
:::

<1>2. The ideal $(x)$ is prime but not maximal.
::: {.proof}
An ideal $I$ in a commutative ring is prime exactly when the quotient by $I$ is an integral domain, and maximal exactly when that quotient is a field. The ring $\mathbb R[y]$ is an integral domain because $\mathbb R$ is a field, so $(x)$ is prime.

However, $\mathbb R[y]$ is not a field: the nonconstant polynomial $y$ has no multiplicative inverse in $\mathbb R[y]$. Hence $(x)$ is not maximal.
:::
:::
