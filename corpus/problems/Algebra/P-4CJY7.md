---
schema: qual/card@1
id: P-4CJY7
kind: problem
title: Characteristic and minimal polynomials of the Frobenius automorphism
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
  - Minimal and Characteristic Polynomials
  - Galois Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
What are the characteristic and minimal polynomial of the Frobenius automorphism?
:::

::: {.solution}
<1>1. Let $F = \FF_{p^n}$ and let $\operatorname{Frob}: F \to F$, $x \mapsto x^p$, be the Frobenius automorphism, viewed as an $\FF_p$-linear operator on the $n$-dimensional $\FF_p$-vector space $F$.
Proof: setup.

<1>2. $\operatorname{Frob}^n = \id_F$.
Proof: for $x \in \FF_{p^n}$, $x^{p^n} = x$ (the multiplicative group has order $p^n - 1$, and $0$ is fixed).

<1>3. $\operatorname{Frob}^k \neq \id_F$ for $0 < k < n$.
Proof: if $x^{p^k} = x$ for all $x \in F$, then every element of $F$ is a root of $X^{p^k} - X$, which has at most $p^k$ roots, contradicting $|F| = p^n > p^k$.

<1>4. Hence the minimal polynomial of $\operatorname{Frob}$ is $X^n - 1$.
Proof: $\operatorname{Frob}$ satisfies $X^n - 1$ (<1>2) and no lower-degree polynomial (since $\operatorname{Frob}^0, \ldots, \operatorname{Frob}^{n-1}$ are linearly independent over $\FF_p$ by <1>3 and the fact that $\operatorname{Gal}(\FF_{p^n}/\FF_p)$ has order $n$).

<1>5. The characteristic polynomial of $\operatorname{Frob}$ is $X^n - 1$.
Proof: the minimal polynomial has degree $n = \dim_{\FF_p} F$, so it equals the characteristic polynomial.

<1>6. Q.E.D.
Proof: <1>4 and <1>5.
:::
