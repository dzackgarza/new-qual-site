---
schema: qual/card@1
id: P-BERK90S-02
kind: problem
title: Every finite-order complex matrix is diagonalizable
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-22
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: >-
    Used the minimal polynomial: it divides x^k-1, whose complex roots are
    simple, so the minimal polynomial splits into distinct linear factors.
---

::: {.problem}
Let $A$ be a complex $n\times n$ matrix of finite order, so that
$$
A^k=I
$$
for some positive integer $k$. Prove that $A$ is diagonalizable.
:::

::: {.solution}
<1>1. The minimal polynomial $m_A(x)$ divides $x^k-1$ in $\CC[x]$.

::: {.proof}
The hypothesis $A^k=I$ says precisely that
$$
(x^k-1)(A)=0.
$$
By the defining divisibility property of the minimal polynomial, $m_A(x)$
divides every polynomial that annihilates $A$. Hence $m_A(x)\mid x^k-1$.
:::

<1>2. The polynomial $x^k-1$ has no repeated root in $\CC$.

::: {.proof}
Its derivative is $kx^{k-1}$. A repeated root would therefore be a common
root of $x^k-1$ and $kx^{k-1}$. Every root of the latter polynomial is $0$,
whereas $(0)^k-1=-1$. Thus the two polynomials have no common root, so
$x^k-1$ has only simple roots.
:::

<1>3. The minimal polynomial $m_A(x)$ splits over $\CC$ as a product of
distinct linear factors.

::: {.proof}
By step <1>1, every root and every irreducible factor of $m_A(x)$ occurs in
$x^k-1$. The latter splits into distinct linear factors over $\CC$ by the
fundamental theorem of algebra and step <1>2. Therefore its divisor
$m_A(x)$ is also a product of distinct linear factors.
:::

<1>4. The matrix $A$ is diagonalizable over $\CC$.

::: {.proof}
A complex matrix is diagonalizable if and only if its minimal polynomial
splits into distinct linear factors. Step <1>3 verifies this criterion for
$A$.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required conclusion.
:::
:::
