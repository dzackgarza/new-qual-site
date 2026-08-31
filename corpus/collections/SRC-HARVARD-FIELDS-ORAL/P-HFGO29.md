---
schema: qual/card@1
id: P-HFGO29
kind: problem
title: A finite simple field extension is algebraic
classification:
  areas: [algebra]
  topics: [Field Theory]
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
If $F(a)/F$ is a finite field extension, prove that $a$ is algebraic over $F$.
:::

::: {.solution}
**Goal.** Prove that a finite field extension $F(a)/F$ forces $a$ to be algebraic over $F$.

<1>1. $F(a)$ is a finite-dimensional $F$-vector space.
::: {.proof}
$F(a)/F$ is finite by hypothesis, so $[F(a) : F] = n < \infty$.
:::

<1>2. The set $\theset{1, a, a^2, \dots, a^n}$ is linearly dependent over $F$.
::: {.proof}
it has $n+1$ elements in an $n$-dimensional vector space.
:::

<1>3. There is a nonzero polynomial $p \in F[x]$ with $p(a) = 0$.
::: {.proof}
linear dependence gives $c_0 + c_1 a + \cdots + c_n a^n = 0$ with not all $c_i = 0$; take $p(x) = c_0 + c_1 x + \cdots + c_n x^n$.
:::

<1>4. $a$ is algebraic over $F$.
::: {.proof}
by definition, $a$ is algebraic over $F$ iff it is a root of some nonzero polynomial in $F[x]$, which is <1>3.
:::

<1>5. Q.E.D.
::: {.proof}
<1>4 is the claim.
:::
:::
