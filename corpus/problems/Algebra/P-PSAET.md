---
schema: qual/card@1
id: P-PSAET
kind: problem
title: Orders of $\GL_n(\FF_p)$ and $\SL_n(\FF_p)$
classification:
  areas:
  - algebra
  topics:
  - Matrix Groups
  - Finite Fields
  - Determinants
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
Determine the orders $\abs{\GL_n(\FF_p)}$ and $\abs{\SL_n(\FF_p)}$ for any prime $p$ and integer $n \ge 1$.
:::

::: {.solution}

::: pf

::: {.pf-step #gl}
$\abs{\GL_n(\FF_p)}=\boxed{\prod_{k=0}^{n-1}(p^n-p^k)=p^{n(n-1)/2}\prod_{j=1}^n(p^j-1)}$.

::: pf-proof
A matrix is invertible exactly when its columns $c_1,\ldots,c_n$ form a basis of $\FF_p^n$, that is, when each $c_{k+1}$ lies outside the span of $c_1,\ldots,c_k$. That span has $p^k$ elements, so given $c_1,\ldots,c_k$ there are $p^n-p^k$ choices for $c_{k+1}$. The second form follows from $p^n-p^k=p^k(p^{n-k}-1)$ and $\sum_{k=0}^{n-1}k=n(n-1)/2$.
:::

:::

::: pf-step
$\abs{\SL_n(\FF_p)}=\boxed{\dfrac1{p-1}\prod_{k=0}^{n-1}(p^n-p^k)}$.

::: pf-proof
The determinant $\det:\GL_n(\FF_p)\to\FF_p^\times$ is a homomorphism with kernel $\SL_n(\FF_p)$. It is surjective, since $\det\diag(a,1,\ldots,1)=a$ for every $a\in\FF_p^\times$. So $\abs{\SL_n(\FF_p)}=\abs{\GL_n(\FF_p)}/(p-1)$, and step [](#gl){.pf-ref} gives the value.
:::

:::

:::

:::
