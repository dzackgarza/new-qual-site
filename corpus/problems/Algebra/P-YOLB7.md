---
schema: qual/card@1
id: P-YOLB7
kind: problem
title: Cayley-Hamilton theorem
classification:
  areas:
  - algebra
  topics:
  - Minimal and Characteristic Polynomials
  - Linear Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
State and prove the Cayley–Hamilton Theorem for an $n \times n$ matrix $A$ over a commutative ring $R$.
:::

::: {.solution}
Let $p(t)=\det(tI-A)=t^n+c_{n-1}t^{n-1}+\cdots+c_0\in R[t]$.
The theorem states that $p(A)=A^n+c_{n-1}A^{n-1}+\cdots+c_0I=0$ in $M_n(R)$.

::: pf

::: {.pf-step #adjugate}
There are $B_0,\ldots,B_{n-1}\in M_n(R)$ with $B_{n-1}=I$, $B_{k-1}-AB_k=c_kI$ for $1\le k\le n-1$, and $-AB_0=c_0I$.

::: pf-proof
Over the commutative ring $R[t]$, the adjugate satisfies $(tI-A)\operatorname{adj}(tI-A)=p(t)I$.
The entries of $\operatorname{adj}(tI-A)$ are polynomials of degree at most $n-1$, so $\operatorname{adj}(tI-A)=\sum_{k=0}^{n-1}B_kt^k$ with $B_k\in M_n(R)$.
Comparing the coefficients of $t^n,t^k$ for $1\le k\le n-1$, and $t^0$ gives the three identities.
:::

:::

::: pf-step
$\boxed{p(A)=0}$.

::: pf-proof
Multiply the identity for the coefficient of $t^k$ in step [](#adjugate){.pf-ref} on the left by $A^k$ and add over $k=0,\ldots,n$.
The right side is $p(A)$.
The left side is $A^nB_{n-1}+\sum_{k=1}^{n-1}\left(A^kB_{k-1}-A^{k+1}B_k\right)-AB_0$, whose middle sum telescopes to $AB_0-A^nB_{n-1}$, so the left side is $0$.
:::

:::

:::

:::
