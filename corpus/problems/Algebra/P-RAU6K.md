---
schema: qual/card@1
id: P-RAU6K
kind: problem
title: A cubic with Galois group $S_3$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Polynomials
  - Permutations
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: openai-gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Give an example of a cubic polynomial over $\QQ$ with Galois group $S_3$, and prove that its Galois group is indeed $S_3$.
:::

::: {.solution}
Let $f(x)\coloneqq x^3-2$.

::: pf

::: {.pf-step #irreducible}
$f$ is irreducible over $\QQ$.

::: pf-proof
Eisenstein's criterion applies at the prime $2$.
:::

:::

::: {.pf-step #disc}
The discriminant $\Delta(f)=-108$ is not a square in $\QQ$.

::: pf-proof
For $x^3+px+q$ the discriminant is $-4p^3-27q^2$; with $p=0$, $q=-2$ this is $-108<0$.
:::

:::

::: pf-step
$\Gal(f/\QQ)\cong\boxed{S_3}$.

::: pf-proof
By step [](#irreducible){.pf-ref}, the Galois group acts transitively on the three roots, so it is $A_3$ or $S_3$. It lies in $A_3$ exactly when $\Delta(f)$ is a square in $\QQ$, which step [](#disc){.pf-ref} excludes. As a check, the splitting field $\QQ(\sqrt[3]2,\zeta_3)$ has degree $6$: $[\QQ(\sqrt[3]2):\QQ]=3$, and this real field does not contain the nonreal $\zeta_3$, which has degree $2$ over it.
:::

:::

:::
:::
