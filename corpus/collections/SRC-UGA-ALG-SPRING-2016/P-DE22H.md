---
schema: qual/card@1
id: P-DE22H
kind: problem
title: Elementary divisors and invariant factors of a given $\QQ[x]$-module
classification:
  areas:
  - algebra
  topics:
  - Structure Theorem
  - Modules
  - Canonical Forms
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: problem
Let $D = \QQ[x]$ and let $M$ be a $\QQ[x]\dash$module such that
\[
M \cong \frac{\mathbb{Q}[x]}{(x-1)^{3}} \oplus \frac{\mathbb{Q}[x]}{\left(x^{2}+1\right)^{3}} \oplus \frac{\mathbb{Q}[x]}{(x-1)\left(x^{2}+1\right)^{5}} \oplus \frac{\mathbb{Q}[x]}{(x+2)\left(x^{2}+1\right)^{2}}
.\]

Determine the elementary divisors and invariant factors of $M$.
:::

::: solution
Set
\[
a=x-1,
\qquad
b=x+2,
\qquad
q=x^2+1.
\]
These are pairwise coprime irreducibles in $\mathbb Q[x]$. By the Chinese remainder theorem,
\[
D/(aq^5)\cong D/(a)\oplus D/(q^5)
\]
and
\[
D/(bq^2)\cong D/(b)\oplus D/(q^2).
\]
Therefore the elementary divisors of $M$ are
\[
a^3,\quad a,\quad b,\quad q^5,\quad q^3,\quad q^2,
\]
i.e.
\[
(x-1)^3,\quad x-1,\quad x+2,\quad
(x^2+1)^5,\quad(x^2+1)^3,\quad(x^2+1)^2.
\]

To form invariant factors, align the powers of each irreducible from the right. For $a$ the exponent lists are $1,3$; for $q$ they are $2,3,5$; for $b$ there is one exponent $1$. This yields three invariant factors
\[
d_1=q^2,
\qquad
d_2=a q^3,
\qquad
d_3=a^3bq^5.
\]
Explicitly,
\[
\boxed{
\begin{aligned}
d_1&=(x^2+1)^2,\\
d_2&=(x-1)(x^2+1)^3,\\
d_3&=(x-1)^3(x+2)(x^2+1)^5.
\end{aligned}}
\]
They satisfy $d_1\mid d_2\mid d_3$, and their product is the product of the original cyclic annihilators, confirming the invariant-factor decomposition.
:::
