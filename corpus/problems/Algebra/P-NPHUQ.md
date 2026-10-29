---
schema: qual/card@1
id: P-NPHUQ
kind: problem
title: $x^{p^n}-x$ is the product of all monic irreducibles of degree dividing $n$
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
  - Factorization
  - Irreducibility Criteria
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.problem}
Show that over $\FF_p$,
$$
x^{p^n}-x
$$
is the product of all monic irreducible polynomials whose degrees divide $n$, each occurring once.
:::

::: {.solution}
Fix an algebraic closure $\bar\FF_p$, and write $F(x)=x^{p^n}-x$.

::: pf

::: {.pf-step #roots}
The roots of $F$ in $\bar\FF_p$ are the elements of the subfield $\FF_{p^n}$, and $F$ is squarefree.

::: pf-proof
$F'=-1$ has no roots, so $F$ has $p^n$ distinct roots and is squarefree.
They form a field, the fixed field of the $n$-th power of Frobenius, of order $p^n$.
:::

:::

::: {.pf-step #divides}
A monic irreducible $f\in\FF_p[x]$ of degree $d$ divides $F$ if and only if $d\mid n$.

::: pf-proof
Let $\alpha\in\bar\FF_p$ be a root of $f$, so $\FF_p(\alpha)$ is the subfield $\FF_{p^d}$ of $\bar\FF_p$.
Since $f$ is the minimal polynomial of $\alpha$, $f\mid F$ exactly when $F(\alpha)=0$, which by step [](#roots){.pf-ref} means $\alpha\in\FF_{p^n}$, that is, $\FF_{p^d}\subseteq\FF_{p^n}$.
A subfield of order $p^d$ lies in $\FF_{p^n}$ exactly when $d\mid n$.
:::

:::

::: pf-step
$F=\prod f$, the product over the monic irreducible $f\in\FF_p[x]$ with $\deg f\mid n$.

::: pf-proof
$F$ is monic, its irreducible factors are the $f$ of step [](#divides){.pf-ref}, and by step [](#roots){.pf-ref} each occurs once.
:::

:::

:::

:::
