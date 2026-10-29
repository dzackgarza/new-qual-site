---
schema: qual/card@1
id: P-ZYJDF
kind: problem
title: A polynomial with Galois group $\ZZ/3\ZZ$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Cyclic Groups
  - Polynomials
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
Construct an explicit polynomial over $\QQ$ whose Galois group is the cyclic group of order 3:
$$\Gal(f/\QQ) \cong \ZZ/3\ZZ.$$
Prove that your polynomial satisfies this condition.
:::

::: {.solution}
Let $f(x)=x^3-3x+1$.

::: pf

::: {.pf-step #irreducible}

$f$ is irreducible over $\QQ$.

::: pf-proof

By the rational root test, the only possible rational roots are $\pm1$, and $f(1)=-1$, $f(-1)=3$. A cubic with no root in $\QQ$ is irreducible over $\QQ$.

:::

:::

::: {.pf-step #disc}

The discriminant of $f$ is $81=9^2$.

::: pf-proof

For $x^3+px+q$ the discriminant is $-4p^3-27q^2$; with $p=-3$ and $q=1$ this is $108-27=81$.

:::

:::

::: pf-step

$\Gal(f/\QQ)\cong\boxed{A_3\cong\ZZ/3\ZZ}$.

::: pf-proof

By step [](#irreducible){.pf-ref}, $f$ is separable and its Galois group is a transitive subgroup of $S_3$, so it is $A_3$ or $S_3$. It lies in $A_3$ exactly when the discriminant is a square in $\QQ$, which holds by step [](#disc){.pf-ref}.

:::

:::

:::

:::
