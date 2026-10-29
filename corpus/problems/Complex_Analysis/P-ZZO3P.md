---
schema: qual/card@1
id: P-ZZO3P
kind: problem
title: The fundamental theorem of algebra
classification:
  areas:
  - complex-analysis
  topics:
  - Liouville's Theorem
  - Polynomials
  - Zeros
  - Entire Functions
relations: []
review: draft
---

::: {.problem}
Prove the Fundamental Theorem of Algebra (using complex analysis).
:::

::: {.hint}
Argue by contradiction: if a nonconstant polynomial had no roots, $1/p$ would be a bounded entire function, and Liouville's theorem applies.
:::

::: {.solution}
Let $p(z)=a_nz^n+\cdots+a_0$ with $n\ge1$ and $a_n\ne0$, and suppose, toward a contradiction, that $p$ has no root in $\CC$.

::: pf

::: {.pf-step #far}
There is $R>0$ such that $\abs{p(z)}\ge\frac{\abs{a_n}}{2}R^n$ for $\abs{z}>R$.

::: pf-proof
For $z\ne0$,
$$
\frac{p(z)}{z^n}=a_n+\qty(\frac{a_{n-1}}{z}+\cdots+\frac{a_0}{z^n}),
$$
and the term in parentheses tends to $0$ as $\abs{z}\to\infty$. Choose $R\ge1$ with that term of modulus at most $\abs{a_n}/2$ for $\abs{z}>R$; then $\abs{p(z)}\ge\frac{\abs{a_n}}{2}\abs{z}^n\ge\frac{\abs{a_n}}{2}R^n$.
:::

:::

::: {.pf-step #bounded}
$1/p$ is a bounded entire function.

::: pf-proof
$1/p$ is entire because $p$ has no roots. On the compact disk $\abs{z}\le R$, the continuous function $\abs{p}$ has a positive minimum, and step [](#far){.pf-ref} bounds $\abs{p}$ below for $\abs{z}>R$.
:::

:::

::: pf-step
$p$ is constant, a contradiction.

::: pf-proof
By step [](#bounded){.pf-ref} and Liouville's theorem, $1/p$ is constant, so $p$ is constant, contrary to $n\ge1$ and $a_n\ne0$.
:::

:::

:::

:::
